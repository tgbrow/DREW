# type IDs corresponding to different hardware types
TID_W = 0 # wearable
TID_Z = 1 # zone
TID_D = 2 # (connected) device
TID_C = 3 # (device) configuration

# tab indexes
TAB_STAT = 0 # status
TAB_HW   = 1 # hardware setup
TAB_SYS  = 2 # system setup

NUM_DIALOGS = 4

PLUGABLE_ACTIONS = {0: "Ignore", 1: "Turn Off", 2: "Turn On"}
PLUGABLE_STATES = {0: "Unavailable", 1: "Off", 2: "On"}

DEVICE_TYPES = {0: "Plugable Outlet Switch"}
DEVICE_ACTIONS = {0: PLUGABLE_ACTIONS}
DEVICE_STATES = {0: PLUGABLE_STATES}