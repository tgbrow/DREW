from drew_util import *
import time

DEBUG_BTCMD = False

class BluetoothCommander:
	def __init__(self, systemState):
		self.systemState = systemState
		self.controllers = {}

	def connect(self):
		for device in self.systemState.dicts[TID_D].values():
			self.controllers[device.hwId] = BtController(device.hwId)
			self.controllers[device.hwId].connect()
			device.state = self.controllers[device.hwId].state

	def run(self):
		# connect or checkDeviceCreation?
		# self.connect()
		self.checkDeviceCreation()

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
					self.performAction()


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
			print('ERROR: BluetoothCommander perform error: workItem=', workItem)


	def resume(self):
		# Actions to perform when resuming from a system pause
		# 1: attempt to connect to any previously unavailable devices
		# 2: check all devices state with the state it should be in
		# 4: disconnect from any devices that were removed during pause
		# create new controllers for any device that was just added
		
		if DEBUG_BTCMD: print('BTCMD: resuming...')
		self.checkDeviceDeletion()
		self.checkDeviceCreation()
		self.attemptReconnect()
		self.checkDeviceState()


	def checkDeviceDeletion(self):
		if DEBUG_BTCMD: print('BTCMD: checking for a device deletion')
		discardList = [] # list of controllers to be discarded
		for controller in self.controllers.values():
			device = self.systemState.getHardwareObjectByHwId(TID_D, controller.hwId)
			if device == None:
				# device must have been deleted
				if DEBUG_BTCMD: print('\tBTCMD: found a device to remove with hwId ', controller.hwId)
				discardList.append(controller)
		for item in discardList:
			if DEBUG_BTCMD: print('\tBTCMD: removing controller with hwId ', item.hwId)
			item.disconnect()
			del self.controllers[item.hwId]


	# Checks all the devices that are currently in the controllers list. will skip controllers that are not connected
	# Should call all other methods that try to ensure connectivity before calling this --> mainly deletions
	def checkDeviceState(self):
		if DEBUG_BTCMD: print('BTCMD: checking intended device state against actual state')

		for controller in self.controllers.values():
			if not controller.connected:
				continue
			device = self.systemState.getHardwareObjectByHwId(TID_D, controller.hwId)
			device.state = controller.getState() # update the device state regardless
			zone = self.systemState.dicts[TID_Z].get(device.zone) #device.zone --> zone's xmlId
			if zone == None:
				continue #zone does not exist, most likely device is not connected to one
			numInZone = zone.wearablesInZone.getWearableCount()
			if numInZone > 0:
				intendedState = device.enter #some wearable in zone
			else:
				intendedState = device.exit #no wearables in zone
			if intendedState != 0 and intendedState != controller.state: # no need to get state, already did that recently
				controller.setState(intendedState)
				device.state = controller.state

		# for device in self.systemState.dicts[TID_D].values():
		# 	zone = self.systemState.dicts[TID_Z].get(device.zone) #device.zone --> zone's xmlId

		# 	if zone == None:
		# 		continue # zone does not exist, most likely device is not assigned to a zone

		# 	# determine the state the device should be in
		# 	numInZone = len(zone.wearablesInZone.keys())
		# 	if numInZone > 0:
		# 		# some wearable is in zone, state should be the 'enter' action
		# 		state = device.enter
		# 	else:
		# 		# no wearables in zone, state should be the 'exit' action
		# 		state = device.exit			

		# 	controller = self.controllers.get(device.hwId)
		# 	if controller == None:
		# 		if DEBUG_BTCMD: print('\tBTCMD: somehow got a controller of None. device not in controllers?')
		# 	elif state != controller.getState():
		# 		if DEBUG_BTCMD: print('\tBTCMD: found a device state mismatch')
		# 		controller.setState(state) # device should hold the correct state for device
		# 	device.state = controller.state

	def attemptReconnect(self):
		if DEBUG_BTCMD: print('BTCMD: attempting to connect to previously unavailable devices')
		for controller in self.controllers.values():
			if not controller.connected:
				if DEBUG_BTCMD: print('\tBTCMD: found a disconnected device, attempting reconnect...')
				controller.connect()
				if DEBUG_BTCMD: print('\tBTCMD: connection status after attempt ', controller.connected)

	def checkDeviceCreation(self):
		if DEBUG_BTCMD: print('BTCMD: checking for a any device creation')
		for device in self.systemState.dicts[TID_D].values():
			controller = self.controllers.get(device.hwId)
			if controller == None:
				# device has been added, but there is not controller yet
				self.controllers[device.hwId] = BtController(device.hwId)
				self.controllers[device.hwId].connect()
				device.state = self.controllers[device.hwId].state