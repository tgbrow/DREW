from drew_util import *
import time

class BluetoothCommander:
	def __init__(self, systemState):
		self.systemState = systemState
		self.controllers = {}
		# physically connect the controllers --> do this here or beginning of run?
		self.connect()

	def connect(self):
		for device in self.systemState.dicts[TID_D].values():
			self.controllers[device.hwId] = BtController(device.hwId)
			self.controllers[device.hwId].connect()
			device.state = self.controllers[device.hwId].state

	def run(self):
		# do this here? or in constructor?
		# self.connect()
		while not self.systemState.stop:
			if self.systemState.systemIsPaused:

				if not self.systemState.threadsPaused[THREAD_BT]:
					# first time through after pausing the system
					self.systemState.threadsPaused[THREAD_BT] = True # necessary?
					# pausing thread, acquire queue lock, and finish any remaining actions
					while not self.systemState.actionQ.empty():
						performAction()

				self.systemState.threadsPaused[THREAD_BT] = True
				time.sleep(PAUSE_SLEEP_TIME)
			else:

				if self.systemState.threadsPaused[THREAD_BT]:
					# first time through after resuming the system
					self.resume()

				self.systemState.threadsPaused[THREAD_BT] = False
				if not self.systemState.actionQ.empty():
					performAction()


	def performAction(self):
		try:
			workItem = self.systemState.actionQ.get(True, 1) # lock until queue returns an item
			zone = workItem[0]
			action = workItem[1]
			for device in self.systemState.dicts[TID_D].values():
				if device.zone == zone.xmlId:
					if not self.controllers[device.hwId].connected:
						# device isn't connected, attempt to connect
						if not self.controllers[device.hwId].connect():
							# still not able to connect to device, skip device for action
							continue
					self.controllers[device.hwId].setState(device.exit if action == DIR_EXIT else device.enter)
					device.state = self.controllers[device.hwId].state
		except:
			print('ERROR: BluetoothCommander could not understand battle plans, WE SHOULD NEVER SEE THIS EXCEPTION ANYMORE')


	def resume(self):
		# Actions to perform when resuming from a system pause
		# 1: attempt to connect to any previously unavailable devices
		# 2: check all devices state with the state it should be in
		# 4: disconnect from any devices that were removed during pause
		
		print('BTCMD: resuming...')

		discardList = []

		print('BTCMD: checking for removed devices')
		# check for devices that were removed during pause
		for controlHwId in self.controllers:
			device = self.systemState.getHardwareObjectByHwId(TID_D, controlHwId)
			if device == None:
				# device is not in system state
				print('BTCMD: found a device to remove')
				discardList.append(controlHwId)
				# continue?

		print('BTCMD: checking all device state')
		# check that all devices are in the correct state
		for device in self.systemState.dicts[TID_D].values():
			zone = self.systemState.dicts[TID_Z].get(device.zone)
			numInZone = len(zone.wearablesInZone.keys())
			if numInZone > 0:
				# take the 'enter action'
				# self.controllers[device.hwId].setState(device.enter)
				action = device.enter
			else:
				# take the 'exit action'
				# self.controllers[device.hwId].setState(device.exit)
				action = device.exit
			# self.controllers[device.hwId].setState(action)

			control = self.controllers[device.hwId]
			if device.state != control.state:
				# mismatch, fix it
				print('BTCMD: found a device state mismatch')
				control.setState(action)

		print('BTCMD: attempting reconnect')
		# attempt to connect to any previously disconnected/unavailable devices
		for control in self.controllers.values():
			if not control.connected:
				print('BTCMD: found a disconnected device')
				control.connect()

