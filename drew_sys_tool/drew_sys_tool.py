import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_control import UiControl
from drew_util import SystemState

# create system state
systemState = SystemState("config_test.xml")

# set up GUI application
app = QApplication(sys.argv)

uiControl = UiControl(systemState)

# sys.exit(app.exec_())
app.exec_()

systemState.xml.save()