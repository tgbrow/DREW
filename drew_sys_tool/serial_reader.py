from drew_util import SerialMessage
from constants import *
import time
# import serial
# import re

class SerialReader():
	def __init__(self, systemState):
		self.systemState = systemState
		self.serialComm = systemState.serialComm

	def run(self):
		while(not self.systemState.stop):
			self.systemState.threadsPaused[THREAD_SR] = self.systemState.pause

			if (self.serialComm.inWaiting() > 0):
				msg = SerialMessage(self.serialComm.readline().decode())
				# print('msg: ', msg.msgType, ', ', msg.wearableId, ', ', msg.zoneId, ', ', msg.signalStrength)
				if (msg.msgType == MSG_TYPE_REG):
					if (self.systemState.pause):
						# if the system is paused, we throw out any msg besides "discovers"
						continue
					zone = self.systemState.getHardwareObjectByHwId(TID_Z, msg.zoneId)
					if (zone == None):
						continue
					wasInZone = zone.wearableInZone.contains(msg.wearableId)
					nowInZone = (msg.signalStrength - zone.threshold > 0)
					if (nowInZone != wasInZone):
						# debug print
						print("zone occupation change")
						# TODO -- update zoneOccupation table
						# TODO -- hand action info to bluetooth thread
						actionMsg = (zone, DIR_ENTER if nowInZone else DIR_EXIT)
						self.systemState.actionQ.put(actionMsg, True)
				elif (msg.msgType == MSG_TYPE_DISC_W):
					self.systemState.wearableIds.add(msg.wearableId)
				elif (msg.msgType == MSG_TYPE_DISC_Z):
					self.systemState.zoneIds.add(msg.zoneId)
				else:
					print('Invalid Serial Message: ', msg)

			else: # sleep a little bit if there's nothing to do
				time.sleep(0.5)