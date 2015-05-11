import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_control import UiControl
from drew_util import SystemState

# create system state
systemState = SystemState("config_test.xml")

# first start BluetoothCommander
# then start ZoneEvictor
# and then start SerialReader

# set up GUI application
app = QApplication(sys.argv)
uiControl = UiControl(systemState)
app.exec_() # blocks until application is closed

systemState.stop = True
systemState.xml.save()