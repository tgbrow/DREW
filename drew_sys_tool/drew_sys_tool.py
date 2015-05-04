import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_mainscreen import Ui_MainScreen
from classes import SystemState

# create system state
systemState = SystemState()
systemState.debugAddWearable("Test Wearable", 666)

# set up GUI application
app = QApplication(sys.argv)

window = QWidget()
ui = Ui_MainScreen()
ui.setupUi(window, systemState)
window.show()

sys.exit(app.exec_())