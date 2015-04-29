import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_profiledialog import Ui_ProfileDialog

app = QApplication(sys.argv)

window = QWidget()
ui = Ui_ProfileDialog()
ui.setupUi(window)
window.show()

sys.exit(app.exec_())