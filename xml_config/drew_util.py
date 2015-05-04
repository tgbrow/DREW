import xml.etree.ElementTree as ET

class Zone():
  def __init__(self, name='default_zone', xml_id=None, hw_id=None, threshold=None):
    self.name = name
    self.xml_id = xml_id
    self.hw_id = hw_id
    self.threshold = threshold

class Device():
  def __init__(self, name='default_device', xml_id=None, mac=None, dev_type=0, enter=1, exit=0, zone=None):
    self.name = name
    self.xml_id = xml_id
    self.mac = mac
    self.dev_type = dev_type
    self.enter = enter
    self.exit = exit
    self.zone = zone

class Wearable():
  def __init__(self, name='default_wearable', xml_id=None, hw_id=None):
    self.name = name
    self.xml_id = xml_id
    self.hw_id = hw_id

class Profile():
  def __init__(self, name='default_profile', xml_id=None, wearables=None, zones=None):
    self.name = name
    self.xml_id = self
    self.wearables = wearables
    self.zones = zones

class XmlControl():
  def __init__(self, filename='config.xml'):
    self.filename = filename
    self.root =  ET.parse(filename).getroot()
    self.zones = {}
    self.devices = {}
    self.wearables = {}
    self.profiles = {}
    print("created XML_Reader")
    

  def load(self):
    # parses the file from the root, but doesn't really return anything
    # parse all the data for devices
    self.devices = {}
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
    self.zones = {}
    for z in self.root.find('zones'):
      print(z.tag, z.attrib)
      name = z.find('name').text
      xml_id = z.get('z_id')
      hw_id = z.find('hw_id').text
      threshold = int(z.find('threshold').text)
      self.zones[xml_id] = Zone(name, xml_id, hw_id, threshold)

    # parse wearable data
    self.wearables = {}
    for w in self.root.find('wearables'):
      print(w.tag, w.attrib)
      name = w.find('name').text
      xml_id = w.get('w_id')
      hw_id = w.find('hw_id').text
      self.wearables[xml_id] = Wearable(name, xml_id, hw_id)

    # parse profile data
    self.profiles = {}
    for p in self.root.find('profiles'):
      print(p.tag, p.attrib)
      name = p.find('name').text
      xml_id = p.get('p_id')
      # some wearables
      # some zones
      self.profiles[xml_id] = Profile(name, xml_id)