import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_control import UiControl
from classes import SystemState

# create system state
systemState = SystemState()
systemState.debugAddWearable("Test Wearable", 666)

# set up GUI application
app = QApplication(sys.argv)

uiControl = UiControl(systemState)

sys.exit(app.exec_())