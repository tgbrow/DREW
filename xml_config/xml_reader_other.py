import xml.etree.ElementTree as ET
from drew_util import *

root = ET.parse('config.xml').getroot()

deviceDict = {}
moduleDict = {}
wearableDict = {}
zoneDict = {}
profileDict = {}

# populate the deviceDict
for d in root.find('devices'):
  name = d.find('name').text
  xml_id = d.get('d_id')
  mac = d.find('mac').text
  deviceDict[xml_id] = Device(name, xml_id, mac)
  #deviceDict.append(Device(name, xml_id, mac))

# populate the moduleDict
for m in root.find('modules'):
  name = m.find('name').text
  xml_id = m.get('m_id')
  hw_id = m.find('hw_id').text
  moduleDict[xml_id] = Module(name, xml_id, hw_id)

# populate the wearableDict
for w in root.find('wearables'):
  name = w.find('name').text
  xml_id = w.get('w_id')
  hw_id = w.find('hw_id').text
  wearableDict[xml_id] = Wearable(name, xml_id, hw_id)

# populate the zoneDict
for z in root.find('zones'):
  name = z.find('name').text
  xml_id = z.get('z_id')
  z_ms = []
  for m in z.find('modules'):
    z_ms.append(m.find('m_id').text)
  zoneDict[xml_id] = Zone(name, xml_id, z_ms)

# now populate profileDict
for p in root.find('profiles'):
  name = p.find('name').text
  xml_id = p.get('p_id')
  p_ws = []
  for w in p.find('wearables'):
    p_ws.append(w.find('w_id').text)
  p_rs = []
  for r in p.find('rooms'):
    
  
