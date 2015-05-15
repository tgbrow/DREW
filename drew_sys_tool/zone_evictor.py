import time
from constants import *

class ZoneEvictor():
	def __init__(self, systemState):
		self.systemState = systemState

	def run(self):
		while (not self.systemState.stop):
			if (self.systemState.pause):
				self.systemState.threadsPaused[THREAD_ZE] = True
				time.sleep(PAUSE_SLEEP_TIME)
			else:
				self.systemState.threadsPaused[THREAD_ZE] = False
				currTime = time.time()

				for zone in self.systemState.dicts[TID_Z].values():
					for wearableId, signalData in zone.wearablesInZone.items():
						if (currTime - signalData.lastUpdated > EVICT_TIME):
							print('time dif: ', currTime - timeAdded)
							self.wearablesInZone.discard(wearableId)
							self.systemState.actionQ.put((zone, DIR_EXIT), True, None)

					# for wearableId, timeAdded in zone.wearablesInZone.getCopyAsList():
					# 	if (currTime - timeAdded > EVICT_TIME): 
					# 		print('time dif: ', currTime - timeAdded)
					# 		self.systemState.updateZoneOccupation(zone, wearableId, False)
					# 		self.systemState.actionQ.put((zone, DIR_EXIT), True, None)
					
				time.sleep(2.5)
