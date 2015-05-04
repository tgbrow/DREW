import xml.etree.ElementTree as ET
from drew_util import *

root = ET.parse('config_updated.xml').getroot()

print("hello world")

deviceDict = {}
for d in root.find('devices'):
  print(d.tag, d.attrib)
  name = d.find('name').text
  xml_id = d.get('d_id')
  mac = d.find('mac').text
  actions = {}
  for a in d.find('actions'):
    a_id = a.get('a_id')
    actions[a_id] = a.text
    deviceDict[xml_id] = Device(name, xml_id, mac, actions)
 
print(deviceDict)
print(deviceDict['d0'])

class XML_Reader():
  def __init__(self, root=None):
    self.root = root
    self.

  def parse():
    # parses the file from the root, but doesn't really return anything

  def get_dict():
    # gets an assoiated dictionary