class Wearable:
	name = ""
	hwId = 0

	def __init__(self, name, hwId):
		self.name = name
		self.hwId = hwId


class SystemState:
	wearables = []
	zones = []
	devices = []
	configs = []

	def loadState(self):
		# load state in from XML file
		junk = 0

	def newWearable(self):
		wearable = Wearable("New Wearable", 0)
		self.wearables.append(wearable)
		return wearable

	def debugAddWearable(self, name, hwId):
		self.wearables.append(Wearable(name, hwId))

	def getWearableByName(self, name):
		for wearable in self.wearables:
			if wearable.name == name:
				return wearable

	def deleteWearableByName(self, name):
		for wearable in self.wearables:
			if wearable.name == name:
				self.wearables.remove(wearable)
				return
		print("Error: wearable \"" + name + "\" not found for deletion")

	def deleteZoneByName(self, name):
		for zone in self.zones:
			if zone.name == name:
				self.zones.remove(zone)
				return
		print("Error: zone \"" + name + "\" not found for deletion")

	def deleteDeviceByName(self, name):
		for device in self.devices:
			if device.name == name:
				self.devices.remove(device)
				return
		print("Error: device \"" + name + "\" not found for deletion")