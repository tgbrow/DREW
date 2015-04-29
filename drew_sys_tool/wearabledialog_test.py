import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_wearabledialog import Ui_WearableDialog

app = QApplication(sys.argv)

window = QWidget()
ui = Ui_WearableDialog()
ui.setupUi(window)
window.show()

sys.exit(app.exec_())