import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_control import UiControl
from drew_util import SystemState
import threading

# create system state
systemState = SystemState("config_test.xml")

# first start BluetoothCommander
commander = BluetoothCommander(systemState)
btThread = Thread(commander.run, args=())
btThread.start()

# then start ZoneEvictor
evictor = ZoneEvictor(systemState)
evictThread = Thread(evictor.run, args=())
evictThread.start()

# and then start SerialReader
serReader = SerialReader(systemState)
serialThread = Thread(serReader.run, args=())
serReader.start()

# set up GUI application
app = QApplication(sys.argv)
uiControl = UiControl(systemState)
app.exec_() # blocks until application is closed

systemState.stop = True
systemState.xml.save()