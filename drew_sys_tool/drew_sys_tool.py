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
print('starting commander')
commander = BluetoothCommander(systemState)
btThread = Thread(target=commander.run, args=())
btThread.start()
print('started commander')

# then start ZoneEvictor
print('starting evictor')
evictor = ZoneEvictor(systemState)
evictThread = Thread(target=evictor.run, args=())
evictThread.start()
print('started evictor')

# and then start SerialReader
print('starting serReader')
serReader = SerialReader(systemState)
serialThread = Thread(target=serReader.run, args=())
serialThread.start()
print('started serReader')

# set up GUI application
print('launching GUI')
app = QApplication(sys.argv)
uiControl = UiControl(systemState)
app.exec_() # blocks until application is closed

systemState.stop = True

print("stopping system...") # debug

btThread.join()
evictThread.join()
serialThread.join()

print("system stopped") # debug

systemState.xml.save()

print("GOODBYE! :)")