import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_control import UiControl
from drew_util import SystemState

# create system state
systemState = SystemState("config_test.xml")

# spawn other threads here

# set up GUI application
app = QApplication(sys.argv)
uiControl = UiControl(systemState)
app.exec_() # blocks until application is closed

systemState.xml.save()