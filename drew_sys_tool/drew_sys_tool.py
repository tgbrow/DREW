import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_control import UiControl
from drew_util import SystemState
from threading import Thread
from bluetooth_commander import *
from serial_reader import *
from zone_evictor import *

comPort = 'COM1'
if (len(sys.argv) > 1):
	comPort = sys.argv[1]

# create system state
systemState = SystemState("config_test.xml", comPort)

# first start BluetoothCommander
print('\nstarting commander...')
commander = BluetoothCommander(systemState)
btThread = Thread(target=commander.run, args=())
btThread.start()
print('commander online\n')

# then start ZoneEvictor
print('starting evictor...')
evictor = ZoneEvictor(systemState)
evictThread = Thread(target=evictor.run, args=())
evictThread.start()
print('evictor online\n')

# and then start SerialReader
print('starting serial reader...')
serReader = SerialReader(systemState)
serialThread = Thread(target=serReader.run, args=())
serialThread.start()
print('serial reader online\n')

# set up GUI application
print('starting GUI...\n')
app = QApplication(sys.argv)
uiControl = UiControl(systemState)
app.exec_() # blocks until application is closed

systemState.stop = True

print("stopping system...") # debug

btThread.join()
evictThread.join()
serialThread.join()

print("system stopped\n") # debug

systemState.xml.save()

print("GOODBYE! :)")