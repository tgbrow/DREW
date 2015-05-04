# variable dump objects

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
    self.xml_id = xml_id
    self.wearables = wearables
    self.zones = zones