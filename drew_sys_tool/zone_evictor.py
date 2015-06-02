import time
from constants import *
from drew_util import *

class ZoneEvictor():
	def __init__(self, systemState):
		self.systemState = systemState

	def run(self):
		while (not self.systemState.stop):
			if (self.systemState.systemIsPaused):
				self.systemState.threadsPaused[THREAD_ZE] = True
				time.sleep(PAUSE_SLEEP_TIME)
			else:
				self.systemState.threadsPaused[THREAD_ZE] = False
				currTime = time.time()

				for zone in self.systemState.dicts[TID_Z].values():
					# Exception occurs if wearable leaves zone by dropping below zone threshold,
					# since SerialReader will discard this entry in wearablesInZone while
					# ZoneEvictor iterates through it. This is okay; just move on to next zone.
					try:
						for wearableId, signalData in zone.wearablesInZone.items():
							if (currTime - signalData.lastUpdate > EVICT_TIME):
								# print('time dif: ', currTime - signalData.lastUpdate)
								zone.wearablesInZone.discard(wearableId)
								if (zone.wearablesInZone.getWearableCount() == 0):
									self.systemState.actionQ.put((zone, DIR_EXIT), True, None)
					except:
						# print('Wearable left zone while ZoneEvictor checking that zone.')
						continue
					
				time.sleep(EVICT_TIME/2.0)
