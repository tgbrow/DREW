import xml.etree.ElementTree as ET
from drew_util import *

tree = ET.parse('config.xml')
root = tree.getroot()

devices = []
modules = []
wearables = []
zones = []
configs = []

for device in root.find('devices'):
  d = Device()
  d.name = device.find('name').text
  d.XML_ID = device.get('id')
  d.MAC = device.find('mac').text
  devices.append(d)
  print(device.tag, device.attrib)

print(devices)


for module in root.find('modules'):
  m = Module()
  m.name = module.find('name').text
  m.XML_ID = module.get('id')
  m.RFID = module.find('RFID').text
  modules.append(m)
  print(module.tag, module.attrib)

print (modules)

for wearable in root.find('wearables'):
  w = Wearable()
  w.name = wearable.find('name').text
  w.XML_ID = wearable.get('id')
  w.RFID = wearable.find('RFID').text
  wearables.append(w)
  print(wearable.tag, wearable.attrib)

print(wearables)

for zone in root.find('zones'):
  z = Zone()
  z.name = zone.find('name').text
  z.XML_ID = zone.get('id')
  for device in zone.find('devices'):
    device_id = device.get('id')
    for i in range(len(devices)):
      if devices[i].XML_ID == device_id:
        z.devices.append(devices[i])
        break
  for module in zone.find('modules'):
    module_id = module.get('id')
    for i in range(len(modules)):
      if modules[i].XML_ID == module_id:
        z.modules.append(modules[i])
        break
  zones.append(z)
  print(zone.tag, zone.attrib)

print(zones)

for config in root.find('configs'):
  c = Config()
  c.name = config.find('name').text
  c.XML_ID = config.get('id')
  for wearable in config.find('wearables'):

    wearable_id = wearable.get('id')
    for i in range(len(wearables)):
      if wearables[i].XML_ID == wearable_id:
        config.wearables.append(wearables[i])
        break
  for zone in config.find('zones'):
    zone_id = zone.get('id')
    for i in range(len(wearables)):
      if zones[i].XML_ID == zone_id:
        config.zones.append(zones[i])
        break
  configs.append(c)
  print(config.tag, config.attrib)

print(configs)

print(configs[0].zones)
