import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_mainscreen import Ui_MainScreen

app = QApplication(sys.argv)

window = QWidget()
ui = Ui_MainScreen()
ui.setupUi(window)
window.show()

sys.exit(app.exec_())