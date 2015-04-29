import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_connecteddevicedialog import Ui_ConnectedDeviceDialog

app = QApplication(sys.argv)

window = QWidget()
ui = Ui_ConnectedDeviceDialog()
ui.setupUi(window)
window.show()

sys.exit(app.exec_())