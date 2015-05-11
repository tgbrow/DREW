from drew_util import SerialMessage
from constants import *
from time import sleep
# import serial
# import re

class SerialReader():
	def __init__(self, systemState):
		self.systemState = systemState
		self.serialComm = systemState.serialComm

	def run(self):
		while(not self.systemState.stop):
			if (self.systemState.pause):
				self.systemState.threadsPaused[THREAD_SR] = True
				time.sleep(PAUSE_SLEEP_TIME)
			else:
				msg = SerialMessage(self.serialComm.readline().decode())
				if (msg.msgType == MSG_TYPE_REG):
					zone = self.systemState.getHardwareObjectByHwId(TID_Z, msg.zoneId)
					wasInZone = self.systemState.zoneOccupation.lookup(msg.zoneId, msg.wearableId)
					nowInZone = (msg.signalStrength - zone.threshold > 0)
					if (nowInZone != wasInZone):
						# debug print
						print("zone occupation change")
						# TODO -- update zoneOccupation table
						# TODO -- hand action info to bluetooth thread
				elif (msg.msgType == MSG_TYPE_DISC_W):
					self.systemState.wearableIds.add(msg.wearableId)
				else: # (msg.msgType == MSG_TYPE_DISC_Z)
					self.systemState.zoneIds.add(msg.zoneId)