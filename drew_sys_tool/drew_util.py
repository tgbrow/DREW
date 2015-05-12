import xml.etree.ElementTree as ET
from xml.dom import minidom
from constants import *
import sys
import libbtaps
import serial
import threading

class Zone():
  def __init__(self, name='default_zone', xmlId=None, hwId=None, threshold=None):
    self.name = name
    self.xmlId = xmlId
    self.hwId = hwId
    self.threshold = threshold
    self.wearablesInZone = LockedSet()

class Device():
  def __init__(self, name='default_device', xmlId=None, hwId=None, devType=0, enter=2, exit=1, zone=-1):
    self.name = name
    self.xmlId = xmlId
    self.hwId = hwId
    self.devType = devType
    self.enter = enter
    self.exit = exit
    self.zone = zone # note: this is the associated zone's XML ID

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
    f = open(self.filename, 'w')
    f.write(reparsed.toprettyxml(indent='\t'))
    f.close()


class SystemState:
  def __init__(self, filename):
    self.xml = XmlControl(filename)
    self.xml.load()
    self.dicts = [self.xml.wearables, self.xml.zones, self.xml.devices]
    self.nextIds = [0, 0, 0]
    for i in range(3):
      if (len(self.dicts[i].keys()) != 0):
        self.nextIds[i] = max(self.dicts[i].keys()) + 1
    self.serialComm = serial.Serial('COM8', 9600) # Establish the connection on a specific port
    self.wearableIds = LockedSet()
    self.zoneIds = LockedSet()
    self.stop = False
    self.pause = True
    self.threadsPaused = [False, False, False]

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
    device = Device("New Device", xmlId, 0, 0, 0, 0, -1)
    self.dicts[TID_D][xmlId] = device
    return device

  # TODO -- rename this method
  def getHardwareObject(self, typeId, xmlId):
    return self.dicts[typeId][xmlId]

  def getHardwareObjectByHwId(self, typeId, hwId):
    for hwObject in self.dicts[typeId].values():
      if (hwObject.hwId == hwId):
        return hwObject
    print("ERROR: hardward object with hwId ", hwId, " not found!")
    return None

  def deleteHardwareObject(self, typeId, xmlId):
    del self.dicts[typeId][xmlId]
    if (self.nextIds[typeId] == xmlId + 1):
      self.nextIds[typeId] = xmlId

  def discoverHardware(self, typeId):
    self.serialComm.write(SER_DISC_Z_CMD.encode()) # initiate zone discovery
    time.sleep(2.5) # wait for zones to send back messages + processing

    hwIdList = list(self.zoneIds) # *copy* the zone ID list

    for hwItem in self.dicts[typeId].values():
        if hwItem.hwId in hwIdList:
          hwIdList.remove(hwItem.hwId)
    return hwIdList

  def updateZoneOccupation(self, zone, wearableId, direction):
    if (direction == DIR_ENTER):
      zone.wearablesInZone.add( (wearableId, time.time()) )
    else:
      zone.wearablesInZone.discard(wearableId)

  def setSystemPause(self, pauseFlag):
    # debug begin
    if (pauseFlag):
      print("pausing system")
    else:
      print("resuming system")
    #debug end

    self.pause = pauseFlag
    while((not pauseFlag) in self.threadsPaused):
      time.sleep(0.25) # don't return until all threads have seen the pause command
    
    # debug begin
    if (pauseFlag):
      print("pause done")
    else:
      print("resume done")
    # debug end

class LockedSet:
  def __init__(self):
    self.lock = threading.Lock()
    self.set = Set()

  def add(self, item):
    try:
      self.lock.acquire()
      self.set.add(item)
    finally:
      self.lock.release()

  def discard(self, item):
    try:
      self.lock.acquire()
      self.set.discard(item)
    finally:
      self.lock.release()

  def clear(self):
    try:
      self.lock.acquire()
      self.set.clear()
    finally:
      self.lock.release()


# Class that controls bluetooth plugable devices
# connect and disconnect functions don't necessarily need to be public
class BtController():
  def __init__(self, hwId):
    self.hwId = hwId
    self.connected = False
    self.btaps = None

    self.connect() # connect to the device

  def connect(self):
    # connect to a the given bluetooth device
    self.btaps = libbtaps.BTaps(self.hwId)
    self.connected = self.btaps.connect()
    # if self.connected:
    #   print('Successfully connected to Bluetooth Device, hwId: ', hwId)
    # else:
    #   print('Failed to connect to the given Bluetooth Device, hwId: ', hwId)

  def disconnect(self):
    #disconnect from the current device
    if self.btaps != None:
      self.btaps.disconnect()
      self.connected = False
      self.btaps = None
      # print('Disconnected from Bluetooth Device, hwId: ', self.hwId)


  def setState(self, action):
    if action == 0 or not self.connected:
      #ignore the device or not connected
      return
    else:
      if action == 1:
        self.btaps.set_switch(False) #turn device off
      elif action == 2:
        self.btaps.set_switch(True) #turn device on
      #else: unknown action, do nothing

  def getState(self):
    if not self.connected:
      return
    state = -1
    if self.btaps.get_switch_state()[0]:
      state = 2
    else:
      state = 1
    return state

class SerialMessage():
  def __init__(self, data):
    data = data.replace('\r\n', '')
    splitData = re.split('\,', data)
    self.msgType = splitData[0]
    if (self.msgType == MSG_TYPE_REG):          
      self.wearableId = splitData[1]
      self.zoneId = splitData[2]
      self.signalStrength = int(splitData[3])
      # print('Wearable ID=', self.wearableId)
      # print('Zone ID=', self.zoneId)
      # print('Signal Strength=', self.signalStrength)
      # print()
    elif (self.msgType == MSG_TYPE_DISC_W):
      self.wearableId = splitData[1]
      self.zoneId = None
      self.signalStrength = None
      # print('Found wearable with id=', self.wearableId)
      # print()
    else: # (self.msgType == MSG_TYPE_DISC_Z):
      self.wearableId = None
      self.zoneId = splitData[1]
      self.signalStrength = None
      # print('Found zone with id=', self.zoneId)
      # print()
