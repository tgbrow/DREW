from drew_util import SerialMessage
from constants import *
import time
# from time import sleep
# import serial
# import re

class SerialReader():
	def __init__(self, systemState):
		self.systemState = systemState
		self.serialComm = systemState.serialComm

	def run(self):
		if self.serialComm == None:
			print('exiting run because serialComm is none')
			return

		while(not self.systemState.stop):
			print('system not stopped')
			if (self.systemState.pause):
				self.systemState.threadsPaused[THREAD_SR] = True
				time.sleep(PAUSE_SLEEP_TIME)
			else:
				print('inside else!')
				msg = SerialMessage(self.serialComm.readline().decode())
				print('msg: ', msg)
				if (msg.msgType == MSG_TYPE_REG):
					zone = self.systemState.getHardwareObjectByHwId(TID_Z, msg.zoneId)
					wasInZone = self.systemState.zoneOccupation.lookup(msg.zoneId, msg.wearableId)
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
				else: # (msg.msgType == MSG_TYPE_DISC_Z)
					self.systemState.zoneIds.add(msg.zoneId)