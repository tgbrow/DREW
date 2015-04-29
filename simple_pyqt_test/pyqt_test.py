import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_form import Ui_Form

app = QApplication(sys.argv)
window = QWidget()
ui = Ui_Form()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())