import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_zonedialog import Ui_ZoneDialog

app = QApplication(sys.argv)

window = QWidget()
ui = Ui_ZoneDialog()
ui.setupUi(window)
window.show()

sys.exit(app.exec_())