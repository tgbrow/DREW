import xml.etree.ElementTree as ET
from drew_util import *

class XML_Reader():
  def __init__(self, root=None):
    self.root = root
    self.zones = {}
    self.devices = {}
    self.weareables = {}
    self.profiles = {}
    print("created XML_Reader")
    self.__parse()

  def __parse(self):
    # parses the file from the root, but doesn't really return anything
    # parse all the data for devices
    for d in self.root.find('devices'):
      print(d.tag, d.attrib)
      name = d.find('name').text
      xml_id = d.get('d_id')
      mac = d.find('mac').text
      dev_type = int(d.find('dev_type').text)
      enter = int(d.find('enter').text)
      exit = int(d.find('exit').text)
      zone = d.find('z_id').text
      self.devices[xml_id] = Device(name, xml_id, mac, dev_type, enter, exit, zone)

    # parse data for zones
    for z in self.root.find('zones'):
      print(z.tag, z.attrib)
      name = z.find('name').text
      xml_id = z.get('z_id')
      hw_id = z.find('hw_id').text
      threshold = int(z.find('threshold').text)
      self.zones[xml_id] = Zone(name, xml_id, hw_id, threshold)

    # parse wearable data
    for w in self.root.find('wearables'):
      print(w.tag, w.attrib)
      name = w.find('name').text
      xml_id = w.get('w_id')
      hw_id = w.find('hw_id').text
      self.weareables[xml_id] = Wearable(name, xml_id, hw_id)

    # parse profile data
    for p in self.root.find('profiles'):
      print(p.tag, p.attrib)
      name = p.find('name').text
      xml_id = p.get('p_id')
      # some wearables
      # some zones
      self.profiles[xml_id] = Profile(name, xml_id)

"""
just testing basic use case

print('this is garbage')
root = ET.parse('config_updated.xml').getroot()
reader = XML_Reader(root)
ds = reader.devices
for d_id in ds:
  d = ds[d_id]
  print('d_id: ', d.name, ', ', d.xml_id, ', ', d.mac, ', ', d.dev_type, ', ', d.enter, ', ', d.exit, ', ', d.zone)
  print('d.enter + d.exit: ',  d.enter + d.exit)
"""