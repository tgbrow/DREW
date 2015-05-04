import xml.etree.ElementTree as ET

NUM_DIALOGS = 4

# table & dialog type IDs
W_TID = 0 # wearable
Z_TID = 1 # zone
D_TID = 2 # (connected) device
C_TID = 3 # (device) configuration

class Zone():
  def __init__(self, name='default_zone', xmlId=None, hwId=None, threshold=None):
    self.name = name
    self.xmlId = xmlId
    self.hwId = hwId
    self.threshold = threshold

class Device():
  def __init__(self, name='default_device', xmlId=None, hwId=None, dev_type=0, enter=1, exit=0, zone=None):
    self.name = name
    self.xmlId = xmlId
    self.hwId = hwId
    self.dev_type = dev_type
    self.enter = enter
    self.exit = exit
    self.zone = zone

class Wearable():
  def __init__(self, name='default_wearable', xmlId=None, hwId=None):
    self.name = name
    self.xmlId = xmlId
    self.hwId = hwId

class Profile():
  def __init__(self, name='default_profile', xmlId=None, wearables=None, zones=None):
    self.name = name
    self.xmlId = self
    self.wearables = wearables
    self.zones = zones

class XmlControl():
  def __init__(self, filename='config.xml'):
    self.filename = filename
    if (self.filename != None):
      self.root =  ET.parse(filename).getroot()
    self.zones = {}
    self.devices = {}
    self.wearables = {}
    self.profiles = {}
    print("created XML_Reader")

  def load(self):
    if (self.filename == None):
      return

    # parses the file from the root, but doesn't really return anything
    # parse all the data for devices
    self.devices = {}
    for d in self.root.find('devices'):
      print(d.tag, d.attrib)
      name = d.find('name').text
      xmlId = int(d.get('dId'))
      hwId = d.find('hwId').text
      dev_type = int(d.find('dev_type').text)
      enter = int(d.find('enter').text)
      exit = int(d.find('exit').text)
      zone = int(d.find('zId').text)
      self.devices[xmlId] = Device(name, xmlId, hwId, dev_type, enter, exit, zone)

    # parse data for zones
    self.zones = {}
    for z in self.root.find('zones'):
      print(z.tag, z.attrib)
      name = z.find('name').text
      xmlId = int(z.get('zId'))
      hwId = z.find('hwId').text
      threshold = int(z.find('threshold').text)
      self.zones[xmlId] = Zone(name, xmlId, hwId, threshold)

    # parse wearable data
    self.wearables = {}
    for w in self.root.find('wearables'):
      print(w.tag, w.attrib)
      name = w.find('name').text
      xmlId = int(w.get('wId'))
      hwId = w.find('hwId').text
      self.wearables[xmlId] = Wearable(name, xmlId, hwId)

    # parse profile data
    self.profiles = {}
    for p in self.root.find('profiles'):
      print(p.tag, p.attrib)
      name = p.find('name').text
      xmlId = int(p.get('pId'))
      # some wearables
      # some zones
      self.profiles[xmlId] = Profile(name, xmlId)


class SystemState:
  def __init__(self, filename):
    xml = XmlControl(filename)
    xml.load()
    self.dicts = [xml.wearables, xml.zones, xml.devices]
    self.nextIds = [0, 0, 0]
    for i in range(3):
      if (len(self.dicts[i].keys()) != 0):
        self.nextIds[i] = max(self.dicts[i].keys()) + 1

  def getXmlId(self, typeId):
    xmlId = self.nextIds[typeId]
    self.nextIds[typeId] += 1
    print("grabbed xmlId: " + str(xmlId))
    return xmlId

  def newWearable(self):
    xmlId = self.getXmlId(W_TID)
    wearable = Wearable("New Wearable", xmlId, 0)
    self.dicts[W_TID][xmlId] = wearable
    return wearable

  def getWearable(self, xmlId):
    return self.dicts[W_TID][xmlId]

  def deleteHardwareItem(self, typeId, xmlId):
    del self.dicts[typeId][xmlId]
    if (self.nextIds[typeId] == xmlId + 1):
      self.nextIds[typeId] = xmlId

#------Temporary stuff below

  def debugAddWearable(self, name, hwId):
    xmlId = self.getXmlId(W_TID)
    self.dicts[W_TID][xmlId] = Wearable(name, xmlId, hwId)