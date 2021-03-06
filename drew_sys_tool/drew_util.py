import xml.etree.ElementTree as ET
from xml.dom import minidom
from constants import *
import sys
import libbtaps
import serial
import threading
from queue import Queue
import re
import time
from bluetooth import *

class Zone():
  def __init__(self, name='default_zone', xmlId=None, hwId=None, threshold=None):
    self.name = name
    self.xmlId = xmlId
    self.hwId = hwId
    self.threshold = threshold
    self.wearablesInZone = LockedDict() # note: keys are the wearable hwId, not xmlId

class Device():
  def __init__(self, name='default_device', xmlId=None, hwId=None, devType=0, enter=2, exit=1, zone=-1, listName="listName"):
    self.name = name
    self.xmlId = xmlId
    self.hwId = hwId
    self.devType = devType
    self.enter = enter
    self.exit = exit
    self.zone = zone # note: this is the associated zone's XML ID
    self.state = 0 # default to unavailable
    self.listName = listName

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
    devicesTag = self.root.find('devices')
    if (devicesTag != None):
      for d in devicesTag:
        name = d.find('name').text
        xmlId = int(d.get('dId'))
        hwId = d.find('hwId').text
        devType = int(d.find('devType').text)
        enter = int(d.find('enter').text)
        exit = int(d.find('exit').text)
        zone = int(d.find('zId').text)
        listName = d.find('listName').text
        self.devices[xmlId] = Device(name, xmlId, hwId, devType, enter, exit, zone, listName)

    # parse data for zones
    self.zones = {}
    zonesTag = self.root.find('zones')
    if (zonesTag != None):
      for z in zonesTag:
        name = z.find('name').text
        xmlId = int(z.get('zId'))
        hwId = int(z.find('hwId').text)
        threshold = int(z.find('threshold').text)
        self.zones[xmlId] = Zone(name, xmlId, hwId, threshold)

    # parse wearable data
    self.wearables = {}
    wearablesTag = self.root.find('wearables')
    if (wearablesTag != None):
      for w in wearablesTag:
        name = w.find('name').text
        xmlId = int(w.get('wId'))
        hwId = int(w.find('hwId').text)
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
      listName = ET.SubElement(device, 'listName')
      listName.text = str(d.listName)

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
  def __init__(self, filename, comPort):
    self.xml = XmlControl(filename)
    self.xml.load()
    self.dicts = [self.xml.wearables, self.xml.zones, self.xml.devices]
    self.nextIds = [0, 0, 0]
    for i in range(3):
      if (len(self.dicts[i].keys()) != 0):
        self.nextIds[i] = max(self.dicts[i].keys()) + 1
    
    self.serialComm = None
    while (self.serialComm == None):
      try:
        self.serialComm = serial.Serial(comPort, 9600) # Establish the connection on a specific port
      except:
        self.serialComm = None
        print('D.R.E.W. USB module not detected. Please connect now.')
        time.sleep(5)

    self.wearableIds = LockedSet()
    self.zoneIds = LockedSet()
    self.stop = False
    self.systemIsPaused = True
    self.threadsPaused = [False, False, False]
    self.actionQ = Queue(ACTION_QUEUE_MAX)

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

  def getHardwareObjectByXmlId(self, typeId, xmlId):
    return self.dicts[typeId][xmlId]

  def getHardwareObjectByHwId(self, typeId, hwId):
    for hwObject in self.dicts[typeId].values():
      if (hwObject.hwId == hwId):
        return hwObject
    return None

  def deleteHardwareObject(self, typeId, xmlId):
    # if deleting zone, update all devices using that zone
    if (typeId == TID_Z):
      for device in self.dicts[TID_D].values():
        if (device.zone == xmlId):
          device.zone = -1

    del self.dicts[typeId][xmlId]
    if (self.nextIds[typeId] == xmlId + 1):
      self.nextIds[typeId] = xmlId

  def discoverHardware(self, typeId):
    if (typeId == TID_Z):
      self.serialComm.write(SER_DISC_Z_CMD.encode()) # initiate zone discovery
      time.sleep(2.5) # wait for zones to send back messages + processing
      hwIdList = self.zoneIds.getCopyAsList() # *copy* the zone ID list
    elif (typeId == TID_W):
      hwIdList = self.wearableIds.getCopyAsList() # *copy* the wearable ID list
    else:
      # scan for bluetooth devices
      hwTupleList = discover_devices(lookup_names=True)

    if (typeId == TID_D):
      for hwItem in self.dicts[typeId].values():
        hwTupleList = [(hwId, listName) for (hwId, listName) in hwTupleList if hwId != hwItem.hwId]
      return hwTupleList
    else:
      for hwItem in self.dicts[typeId].values():
          if hwItem.hwId in hwIdList:
            hwIdList.remove(hwItem.hwId)
      return hwIdList

  def nameInUse(self, typeId, givenName, currXmlId):
    givenName = givenName.lower()
    for hwObject in self.dicts[typeId].values():
      if (hwObject.xmlId == currXmlId):
        continue
      name = hwObject.name.lower()
      if (name == givenName):
        return True
    return False

  def setSystemPause(self, pauseFlag):
    self.systemIsPaused = pauseFlag
    while((not pauseFlag) in self.threadsPaused):
      time.sleep(0.25) # don't return until all threads have seen the pause command

  def isKnownWearable(self, wearableId):
    for wearable in self.dicts[TID_W].values():
      if (wearable.hwId == wearableId):
        return True
    return False
    
class LockedDict:
  def __init__(self):
    self.count = 0
    self.lock = threading.Lock()
    self.dict = {}

  def add(self, key, value):
    try:
      self.lock.acquire()
      self.dict[key] = value
    finally:
      self.lock.release()

  def contains(self, key):
    try:
      self.lock.acquire()
      containsKey = key in self.dict
    finally:
      self.lock.release()
      return containsKey

  def discard(self, key):
    try:
      self.lock.acquire()
      if (key in self.dict):
        if (self.dict[key].isInZone):
          self.count -= 1
        del self.dict[key]
    finally:
      self.lock.release()

  def keys(self):
    try:
      self.lock.acquire()
      keyList = self.dict.keys()
    finally:
      self.lock.release()
      return keyList

  def values(self):
    try:
      self.lock.acquire()
      valueList = self.dict.values()
    finally:
      self.lock.release()
      return valueList

  def items(self):
    try:
      self.lock.acquire()
      itemsList = self.dict.items()
    finally:
      self.lock.release()
      return itemsList

  def get(self, key):
    try:
      self.lock.acquire()
      value = self.dict.get(key)
    finally:
      self.lock.release()
      return value

  def incrementWearableCount(self, delta):
    try:
      self.lock.acquire()
      self.count += delta
    finally:
      self.lock.release()

  def getWearableCount(self):
    try:
      self.lock.acquire()
      ret = self.count
    finally:
      self.lock.release()
      print("wearable count: " + str(ret))
      return ret


class LockedSet:
  def __init__(self):
    self.lock = threading.Lock()
    self.set = set()

  def add(self, item):
    try:
      self.lock.acquire()
      self.set.add(item)
    finally:
      self.lock.release()

  def discard(self, item, isTupleSet=False):
    try:
      self.lock.acquire()
      if (isTupleSet):
        for theTuple in self.set:
          if theTuple[0] == item:
            self.set.discard(theTuple)
            break
      else:
        self.set.discard(item)
    finally:
      self.lock.release()

  def clear(self):
    try:
      self.lock.acquire()
      self.set.clear()
    finally:
      self.lock.release()

  def contains(self, item, isTupleSet=False):
    isPresent = False
    try:
      self.lock.acquire()
      if (isTupleSet):
        for theTuple in self.set:
          if theTuple[0] == item:
            isPresent = True
      else:
        isPresent = item in self.set
    finally:
      self.lock.release()
    return isPresent

  def getCopyAsList(self):
    try:
      self.lock.acquire()
      listCopy = [] if (len(self.set) == 0) else list(self.set)
    finally:
      self.lock.release()
    return listCopy


# Class that controls bluetooth plugable devices
# connect and disconnect functions don't necessarily need to be public
class BtController():
  def __init__(self, hwId):
    self.hwId = hwId
    self.connected = False
    self.btaps = None
    self.state = 0 # 0 is unavailable (connected = false)
    # self.connect() # connect to the device

  def connect(self):
    # connect to a the given bluetooth device
    if not self.connected:
      try:
        self.btaps = libbtaps.BTaps(self.hwId)
        self.connected = self.btaps.connect()
        self.getState()
      except:
        print('WARNING: failed to connect to bt device:', self.hwId)
        self.connected = False
        self.state = 0 # unavailable
      # print('BtController hwId:', self.hwId, ', connected:', self.connected)
    return self.connected

  def disconnect(self):
    if self.btaps != None:
      self.btaps.disconnect()
      self.connected = False
      self.btaps = None
      self.state = 0
      # print('Disconnected from Bluetooth Device, hwId: ', self.hwId)

  def setState(self, action):
    if action == 0: # ignore action
      return
    elif not self.connected:
      print('ERROR: cannot set device state, not connected: ', self.hwId)
      self.state = 0
      return
    else:
      if action == 1:
        self.btaps.set_switch(False) #turn device off
        self.state = 1
      elif action == 2:
        self.btaps.set_switch(True) #turn device on
        self.state = 2

  def getState(self):
    if not self.connected:
      self.state = 0 #unavailable
    elif self.btaps.get_switch_state()[0]:
      self.state = 2 #device is on
    else:
      self.state = 1 #device is off
    return self.state


class SerialMessage():
  def __init__(self, data):
    data = data.replace('\r\n', '')
    splitData = re.split('\,', data)
    self.msgType = splitData[0]
    if (self.msgType == MSG_TYPE_REG):          
      self.wearableId = int(splitData[1])
      self.zoneId = int(splitData[2])
      self.signalStrength = int(splitData[3])
    elif (self.msgType == MSG_TYPE_DISC_W):
      self.wearableId = int(splitData[1])
      self.zoneId = None
      self.signalStrength = None
    else: # (self.msgType == MSG_TYPE_DISC_Z):
      self.wearableId = None
      self.zoneId = int(splitData[1])
      self.signalStrength = None


# averaging version
class SignalData():
  def __init__(self, signalStrength, lastUpdate=None, sampleCount=1):
    self.avgStrength = signalStrength
    self.lastUpdate = time.time() if lastUpdate == None else lastUpdate
    self.sampleCount = sampleCount

  def addSample(self, signalStrength):
    if (self.sampleCount < MAX_SAMPLES):
      self.sampleCount += 1
    self.avgStrength += (signalStrength - self.avgStrength) / self.sampleCount
    self.lastUpdate = time.time()
    return self.avgStrength

# three samples to change version
class SignalDataV2():
  def __init__(self, zoneThreshold):
    self.zoneThreshold = zoneThreshold
    self.lastUpdate = time.time()
    self.samples = []
    self.sampleCount = 0
    self.currIndex = 0
    self.isInZone = False

  def addSample(self, signalStrength):
    self.lastUpdate = time.time()

    if (self.sampleCount < MAX_SAMPLES):
      # add sample to list
      self.samples.append(signalStrength > self.zoneThreshold)
      self.sampleCount += 1
    else:
      # overwirte oldest sample
      self.samples[self.currIndex] = (signalStrength > self.zoneThreshold)
      self.currIndex = (self.currIndex + 1) % MAX_SAMPLES

    if (self.sampleCount == MAX_SAMPLES):
      # only change zone occupation status if the
      # last MAX_SAMPLES samples are all the same
      if (False not in self.samples):
        self.isInZone = True
      elif (True not in self.samples):
        self.isInZone = False

    return self.isInZone


# three samples to change version WITH OFFSET
class SignalDataV3():
  def __init__(self, zone):
    self.containingDict = zone.wearablesInZone
    self.zoneThreshold = zone.threshold
    self.lastUpdate = time.time()
    self.samples = []
    self.sampleCount = 0
    self.currIndex = 0
    self.isInZone = False

  def addSample(self, signalStrength):
    self.lastUpdate = time.time()
    diff = signalStrength - self.zoneThreshold
    newVal = BETWEEN
    if (diff > OFFSET):
      newVal = INSIDE
    elif (diff < (-1 * OFFSET)):
      newVal = OUTSIDE

    if (self.sampleCount < MAX_SAMPLES):
      # add sample to list
      self.samples.append(newVal)
      self.sampleCount += 1
    else:
      # overwirte oldest sample
      self.samples[self.currIndex] = newVal
      self.currIndex = (self.currIndex + 1) % MAX_SAMPLES

    oldIsInZone = self.isInZone
    if (self.sampleCount == MAX_SAMPLES):
      # only change zone occupation status if the
      # last MAX_SAMPLES samples are all the same
      if (BETWEEN not in self.samples):
        if (OUTSIDE not in self.samples):
          self.isInZone = True
        elif (INSIDE not in self.samples):
          self.isInZone = False

    if (oldIsInZone != self.isInZone):
      if (self.isInZone):
        self.containingDict.incrementWearableCount(1)
      else:
        self.containingDict.incrementWearableCount(-1)

    return self.isInZone