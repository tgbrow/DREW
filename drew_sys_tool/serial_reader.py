from drew_util import SerialMessage, SignalData, SignalDataV2
from constants import *
import time

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

					if (self.systemState.systemIsPaused or (not self.systemState.isKnownWearable(msg.wearableId))):
						# if the system is paused, we throw out any msg besides "discovers"
						# also throw out message from wearables that haven't been assigned (i.e. not "known")
						continue

					zone = self.systemState.getHardwareObjectByHwId(TID_Z, msg.zoneId)
					if (zone == None):
						continue # zone not assigned (i.e. not "known") -- throw out message

					print("\n** Regular Message Received **")
					print("   Wearable Id:     " + str(msg.wearableId))
					print("   Zone Id:         " + str(msg.zoneId))
					print("   Signal Strength: " + str(msg.signalStrength))
					print("")

					wasInZone = False
					nowInZone = False
					signalData = zone.wearablesInZone.get(msg.wearableId)

					if (signalData != None): # wearable has been seen in zone recently
						# --- version 1 ---
						# wasInZone = (signalData.sampleCount == MAX_SAMPLES) and (signalData.avgStrength > zone.threshold)
						# newAvgStrength = signalData.addSample(msg.signalStrength)
						# nowInZone = (signalData.sampleCount == MAX_SAMPLES) and (newAvgStrength > zone.threshold)
						
						# --- version 2 ---
						# wasInZone = signalData.isInZone
						# nowInZone = signalData.addSample(msg.signalStrength)

						# --- version 3 ---
						wasInZone = signalData.isInZone
						nowInZone = signalData.addSample(msg.signalStrength)
					else: # wearable has NOT been seen in zone recently
						# --- version 1 ---
						# signalData = SignalData(msg.signalStrength)

						# --- version 2 ---
						# signalData = SignalDataV2(zone.threshold)
						# signalData.addSample(msg.signalStrength)

						# --- version 3 ---
						signalData = SignalDataV3(zone.threshold)
						signalData.addSample(msg.signalStrength)

						zone.wearablesInZone.add(msg.wearableId, signalData)

					if (nowInZone != wasInZone): # wearable has entered or exited zone
						if (not nowInZone):
							zone.wearablesInZone.discard(msg.wearableId)

						actionMsg = (zone, DIR_ENTER if nowInZone else DIR_EXIT)
						self.systemState.actionQ.put(actionMsg, True, None)

				elif (msg.msgType == MSG_TYPE_DISC_W):
					# print("\n** Wearable Discovery Message Received **")
					# print("   Wearable Id:     " + str(msg.wearableId))
					# print("")
					self.systemState.wearableIds.add(msg.wearableId)
				elif (msg.msgType == MSG_TYPE_DISC_Z):
					print("\n** Zone Discovery Message Received **")
					print("   Zone Id:     " + str(msg.zoneId))
					print("")
					self.systemState.zoneIds.add(msg.zoneId)
				else:
					print('Invalid Serial Message: ', msg)

			else: # sleep a little bit if there's nothing to do
				time.sleep(0.5)