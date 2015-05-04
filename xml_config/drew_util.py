
class DREW_Object:
  def __init__(self, name='drew_obj', xml_id=None):
    self.name = name
    self.xml_id = xml_id

class Zone(DREW_Object):
  def __init__(self, name='default_zone', xml_id=None, module=None, threshold=None, devices=None):
    DREW_Object.__init__(self, name, xml_id)
    self.module = module
    self.threshold = threshold
    self.devices = devices

class Module(DREW_Object):
  def __init__(self, name='default_module', xml_id=None, hw_id=None):
    DREW_Object.__init__(self, name, xml_id)
    self.hw_id = hw_id

class Device(DREW_Object):
  def __init__(self, name='default_module', xml_id=None, mac=None, actions=None):
    DREW_Object.__init__(self, name, xml_id)
    self.mac = mac
    self.actions = actions

class Wearable(DREW_Object):
  def __init__(self, name='default_module', xml_id=None, hw_id=None):
    DREW_Object.__init__(self, name, xml_id)
    self.hw_id = hw_id

class Profile(DREW_Object):
  def __init__(self, name='default_module', xml_id=None, wearables=None, zones=None):
    DREW_Object.__init__(self, name, xml_id)
    self.wearables = wearables
    self.zones = zones

#class Room(DREW_Object):
#  def __init__(self, name='default_module', xml_id=None, threshold=None, zone=None, devices=None):
#    DREW_Object.__init__(self, name, xml_id)
#    self.threshold = threshold
#    self.zone = zone
#    self.devices = devices