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
				currTime = time.time()
				for zone in self.systemState.zones.values():
					for wearableId, timeAdded in zone.wearablesInZone:
						if (currTime - timeAdded > EVICT_TIME): 
							zone.wearablesInZone.discard(wearableId)
							# TODO -- hand action info to bluetooth thread
							self.systemState.actionQ.put( (zone, DIR_EXIT) )
				time.sleep(2.5)
