import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_mainwindow import Ui_MainWindow

app = QApplication(sys.argv)
window = QWidget()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())