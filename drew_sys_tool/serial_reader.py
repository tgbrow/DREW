from drew_util import SerialMessage, SignalData
from constants import *
import time

# TODO -- throw out messages from wearables that aren't assigned in the system

class SerialReader():
	def __init__(self, systemState):
		self.systemState = systemState
		self.serialComm = systemState.serialComm

	def run(self):
		while(not self.systemState.stop):
			self.systemState.threadsPaused[THREAD_SR] = self.systemState.systemIsPaused

			if (self.serialComm.inWaiting() > 0): # if a message is available
				msg = SerialMessage(self.serialComm.readline().decode())

				if (msg.msgType == MSG_TYPE_REG):
					print('msg: ', msg.msgType, ', ', msg.wearableId, ', ', msg.zoneId, ', ', msg.signalStrength)

					if (self.systemState.systemIsPaused):
						# if the system is paused, we throw out any msg besides "discovers"
						continue

					zone = self.systemState.getHardwareObjectByHwId(TID_Z, msg.zoneId)
					if (zone == None):
						continue

					wasInZone = False
					nowInZone = False
					signalData = zone.wearablesInZone.get(msg.wearableId)

					if (signalData != None): # wearable has been seen in zone recently
						wasInZone = (signalData.sampleCount == MAX_SAMPLES) and (signalData.avgStrength > zone.threshold)
						newAvgStrength = signalData.addSample(msg.signalStrength)
						nowInZone = (signalData.sampleCount == MAX_SAMPLES) and (newAvgStrength > zone.threshold)
					else: # wearable has NOT been seen in zone recently
						signalData = SignalData(msg.signalStrength)
						zone.wearablesInZone.add(msg.wearableId, signalData)

					if (nowInZone != wasInZone): # wearable has entered or exited zone
						if (not nowInZone):
							zone.wearablesInZone.discard(msg.wearableId)

						actionMsg = (zone, DIR_ENTER if nowInZone else DIR_EXIT)
						self.systemState.actionQ.put(actionMsg, True, None)

				elif (msg.msgType == MSG_TYPE_DISC_W):
					self.systemState.wearableIds.add(msg.wearableId)
				elif (msg.msgType == MSG_TYPE_DISC_Z):
					self.systemState.zoneIds.add(msg.zoneId)
				else:
					print('Invalid Serial Message: ', msg)

			else: # sleep a little bit if there's nothing to do
				time.sleep(0.5)