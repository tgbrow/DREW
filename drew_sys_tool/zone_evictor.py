import time
from constants import *

class ZoneEvictor():
	def __init__(self, systemState):
		self.systemState = systemState

	def run:
		while (not self.systemState.stop):
			currTime = time.time()
			for zone in self.systemState.zones.values():
				for wearableId, timeAdded in zone.wearablesInZone:
					if (currTime - timeAdded > EVICT_TIME): 
						zone.wearablesInZone.discard(wearableId)
						# TODO -- hand action info to bluetooth thread
			time.sleep(2.5)
