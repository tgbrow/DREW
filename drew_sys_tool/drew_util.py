import xml.etree.ElementTree as ET
from xml.dom import minidom
from constants import *
import sys
import libbtaps

class Zone():
  def __init__(self, name='default_zone', xmlId=None, hwId=None, threshold=None):
    self.name = name
    self.xmlId = xmlId
    self.hwId = hwId
    self.threshold = threshold

class Device():
  def __init__(self, name='default_device', xmlId=None, hwId=None, devType=0, enter=2, exit=1, zone=None):
    self.name = name
    self.xmlId = xmlId
    self.hwId = hwId
    self.devType = devType
    self.enter = enter
    self.exit = exit
    self.zone = zone

class Wearable():
  def __init__(self, name='default_wearable', xmlId=None, hwId=None):
    self.name = name
    self.xmlId = xmlId
    self.hwId = hwId

class XmlControl():
  def __init__(self, filename='config.xml'):
    self.filename = filename
    if (self.filename != None):
      self.root =  ET.parse(filename).getroot()
    self.zones = {}
    self.devices = {}
    self.wearables = {}

  def load(self):
    if (self.filename == None):
      return

    # parse all the data for devices
    self.devices = {}
    for d in self.root.find('devices'):
      name = d.find('name').text
      xmlId = int(d.get('dId'))
      hwId = d.find('hwId').text
      devType = int(d.find('devType').text)
      enter = int(d.find('enter').text)
      exit = int(d.find('exit').text)
      zone = int(d.find('zId').text)
      self.devices[xmlId] = Device(name, xmlId, hwId, devType, enter, exit, zone)

    # parse data for zones
    self.zones = {}
    for z in self.root.find('zones'):
      name = z.find('name').text
      xmlId = int(z.get('zId'))
      hwId = z.find('hwId').text
      threshold = int(z.find('threshold').text)
      self.zones[xmlId] = Zone(name, xmlId, hwId, threshold)

    # parse wearable data
    self.wearables = {}
    for w in self.root.find('wearables'):
      name = w.find('name').text
      xmlId = int(w.get('wId'))
      hwId = w.find('hwId').text
      self.wearables[xmlId] = Wearable(name, xmlId, hwId)

  def save(self):
    if self.filename == None:
      return

    configuration = ET.Element('configuration')
    devices = ET.SubElement(configuration, 'devices')
    for d in self.devices.values():
      device = ET.SubElement(devices, 'device')
      device.set('dId', str(d.xmlId))
      name = ET.SubElement(device, 'name')
      name.text = str(d.name)
      hwId = ET.SubElement(device, 'hwId')
      hwId.text = str(d.hwId)
      devType = ET.SubElement(device, 'devType')
      devType.text = str(d.devType)
      enter = ET.SubElement(device, 'enter')
      enter.text = str(d.enter)
      exit = ET.SubElement(device, 'exit')
      exit.text = str(d.exit)
      zId = ET.SubElement(device, 'zId')
      zId.text = str(d.zone)

    wearables = ET.SubElement(configuration, 'wearables')
    for w in self.wearables.values():
      wearable = ET.SubElement(wearables, 'wearable')
      wearable.set('wId', str(w.xmlId))
      name = ET.SubElement(wearable, 'name')
      name.text = str(w.name)
      hwId = ET.SubElement(wearable, 'hwId')
      hwId.text = str(w.hwId)

    zones = ET.SubElement(configuration, 'zones')
    for z in self.zones.values():
      zone = ET.SubElement(zones, 'zone')
      zone.set('zId', str(z.xmlId))
      name = ET.SubElement(zone, 'name')
      name.text = str(z.name)
      hwId = ET.SubElement(zone, 'hwId')
      hwId.text = str(z.hwId)
      threshold = ET.SubElement(zone, 'threshold')
      threshold.text = str(z.threshold)

    # do the actual writing
    rough_string = ET.tostring(configuration, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    f = open(filename, 'w')
    f.write(reparsed.toprettyxml(indent='\t'))
    f.close()


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
    return xmlId

  def newWearable(self):
    xmlId = self.getXmlId(TID_W)
    wearable = Wearable("New Wearable", xmlId, 0)
    self.dicts[TID_W][xmlId] = wearable
    return wearable

  def newZone(self):
    xmlId = self.getXmlId(TID_Z)
    zone = Zone("New Zone", xmlId, 0, 0)
    self.dicts[TID_Z][xmlId] = zone
    return zone

  def newDevice(self):
    xmlId = self.getXmlId(TID_D)
    device = Device("New Device", xmlId, 0, 0, 0, None)
    self.dicts[TID_D][xmlId] = device
    return device

  def getHardwareObject(self, typeId, xmlId):
    return self.dicts[typeId][xmlId]

  def deleteHardwareObject(self, typeId, xmlId):
    del self.dicts[typeId][xmlId]
    if (self.nextIds[typeId] == xmlId + 1):
      self.nextIds[typeId] = xmlId

  def discoverHardware(self, typeId):
    # TODO -- get a legit list of hwIds
    hwIdList = [111, 222, 333, 444, 555, 666, 777]

    for hwItem in self.dicts[typeId].values():
        if hwItem.hwId in hwIdList:
          hwIdList.remove(hwItem.hwId)
    return hwIdList


#------Temporary stuff below

  def debugAddWearable(self, name, hwId):
    xmlId = self.getXmlId(TID_W)
    self.dicts[TID_W][xmlId] = Wearable(name, xmlId, hwId)

# Class that controls bluetooth plugable devices
# connect and disconnect functions don't necessarily need to be public
class BtControl():
  def __init__(self):
    self.currentDevice = None
    self.busy = False
    self.connected = False
    self.btaps = None

  def connect(self, hwId):
    # connect to a the given bluetooth device
    self.currentDevice = hwId
    self.btaps = libbtaps.BTaps(hwId)
    self.connected = self.btaps.connect()
    if self.connected:
      print('Successfully connected to Bluetooth Device, hwId: ', hwId)
    else:
      print('Failed to connect to the given Bluetooth Device, hwId: ', hwId)

  def disconnect(self):
    #disconnect from the current device
    if self.btaps != None:
      self.btaps.disconnect()
      self.connected = False
      self.btaps = None
      print('Disconnected from Bluetooth Device, hwId: ', self.currentDevice)


  def setDeviceState(self, hwId, action):
    if action == 0:
      #ignore the device
      return
    else:
      self.connect(hwId)
      if action == 1:
        #turn device off
        #print('Turning off Bluetooth Device, hwId: ', hwId)
        self.btaps.set_switch(False)
      elif action == 2:
        #turn device on
        #print('Turning on Bluetooth Device, hwId: ', hwId)
        self.btaps.set_switch(True)
      #else:
      #  #unknown action, do nothing
      #  print('Unknown action for Bluetooth Device, hwId: ', hwId)
      self.disconnect()