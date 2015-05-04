import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_control import UiControl
from drew_util import SystemState

# create system state
systemState = SystemState("config_test.xml")
systemState.debugAddWearable("Test Wearable", 666)

# set up GUI application
app = QApplication(sys.argv)

uiControl = UiControl(systemState)

sys.exit(app.exec_())