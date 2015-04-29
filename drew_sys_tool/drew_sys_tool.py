import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui_mainscreen import Ui_MainScreen
from ui_wearabledialog import Ui_WearableDialog

app = QApplication(sys.argv)

window = QWidget()
ui = Ui_MainScreen()
ui.setupUi(window)

# window2 = QWidget()
# ui2 = Ui_WearableDialog()
# ui2.setupUi(window2)

window.show()
# window2.show()

sys.exit(app.exec_())