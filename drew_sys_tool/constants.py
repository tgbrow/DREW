from PyQt5 import QtCore

# type IDs corresponding to different hardware types
TID_W = 0 # wearable
TID_Z = 1 # zone
TID_D = 2 # (connected) device
TID_C = 3 # (device) configuration

# map typeId to strings for hardware objects
HW_STR_DICT = {TID_W:"wearable", TID_Z:"zone", TID_D:"device"}

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

MSG_TYPE_DISC_W = '1' # wearable discovery message
MSG_TYPE_DISC_Z = '4' # zone discovery message
MSG_TYPE_REG    = '2' # "regular" message (wearable/zone signal strength)

# directions
DIR_EXIT = 0
DIR_ENTER = 1

# time before a wearable is "evicted" from a zone (when no signals are seen)
EVICT_TIME = 5 # seconds

# when system is paused (i.e. being configured), this is how long each thread will sleep
# before checking again if the system is still paused
PAUSE_SLEEP_TIME = 2 # seconds

# IDs for threads
THREAD_BT = 0 # bluetooth commander
THREAD_ZE = 1 # zone evictor
THREAD_SR = 2 # serial reader

# command to send over serial to initiate zone module discovery
SER_DISC_Z_CMD = '1'

# system pause / resume boolean flags
PAUSE = True
RESUME = False

# maximum size of the queue to pass actions to the bluetooth commander
ACTION_QUEUE_MAX = 25 

# maximum number of samples to average
MAX_SAMPLES = 3

# sets alignment for text of entries in tables
ITEM_ALIGN_FLAGS = QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter
ITEM_INTERACT_FLAGS = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled

# deletion confrim text
DEL_STR = "Are you sure you want to delete "

# tasks IDs
TASK_NONE = 0
TASK_CLEAR_CONFIG = 1
TASK_DELETE_TABLE_ENTRY = 2

INSIDE = 1
BETWEEN = 0
OUTSIDE = -1
OFFSET = 10