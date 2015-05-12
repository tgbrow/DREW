from drew_util import *
import time

class BluetoothCommander:
	def __init__(self, systemState):
		self.systemState = systemState
		self.controllers = {}
		for device in self.systemState.dicts[TID_D].values():
			self.controllers[device.hwId] = BtController(device.hwId)

	def run(self):
		while not self.systemState.stop:
			if self.systemState.pause:
				self.systemState.threadsPaused[THREAD_BT] = True
				time.sleep(PAUSE_SLEEP_TIME)
			else:
				if not self.systemState.actionQ.empty():
					try:
						workItem = self.systemState.actionQ.get(True) # lock until queue returns an item
						zone = workItem[0]
						action = workItem[1]
						print('commander received zone: ', zone, ' and action: ', aciton)
						for device in self.systemState.dicts[TID_D].values():
							# for each device in system state, check if in zone
							if device.zone == zone.xmlId:
								self.controllers[device.hwId].setState(device.exit if action == DIR_EXIT else device.enter)
					except:
						# exception raised when removing work item from queue
						print('ERROR: BluetoothCommander has no battle orders to execute')