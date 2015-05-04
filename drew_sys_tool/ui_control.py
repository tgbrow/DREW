from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QDialog, QTableWidgetItem
from ui_mainscreen import Ui_MainScreen
from ui_wearabledialog import Ui_WearableDialog
from ui_zonedialog import Ui_ZoneDialog
from ui_devicedialog import Ui_DeviceDialog
from ui_configdialog import Ui_ConfigDialog

NUM_DIALOGS = 4

# table & dialog indexes
W_IDX = 0 # wearable
Z_IDX = 1 # zone
D_IDX = 2 # (connected) device
C_IDX = 3 # (device) configuration

class UiControl:
    def __init__(self, systemState):
        self.systemState = systemState

        self.mainWindow = QWidget()
        self.mainUi = Ui_MainScreen()
        self.mainUi.setupUi(self.mainWindow)

        self.dialogs = []
        for i in range(NUM_DIALOGS):
            self.dialogs.append(QDialog())

        self.dialogUis = []
        self.dialogUis.append(Ui_WearableDialog())
        self.dialogUis.append(Ui_ZoneDialog())
        self.dialogUis.append(Ui_DeviceDialog())
        self.dialogUis.append(Ui_ConfigDialog())
        for i in range(NUM_DIALOGS):
            self.dialogUis[i].setupUi(self.dialogs[i])

        self.tables = [self.mainUi.tableWearable, self.mainUi.tableZone, self.mainUi.tableDevice, self.mainUi.tableConfig]

        self.buttonGroups = []
        self.buttonGroups.append([self.mainUi.buttonEditWearable, self.mainUi.buttonDeleteWearable, self.mainUi.buttonNewWearable])
        self.buttonGroups.append([self.mainUi.buttonEditZone, self.mainUi.buttonDeleteZone, self.mainUi.buttonNewZone])
        self.buttonGroups.append([self.mainUi.buttonEditDevice, self.mainUi.buttonDeleteDevice, self.mainUi.buttonNewDevice])
        self.buttonGroups.append([self.mainUi.buttonEditConfig, self.mainUi.buttonClearConfig])

        self.connectButtons()

        # populate tables with current system info
        self.populateTables()

        # enable/disable buttons when table selection changes
        self.tables[W_IDX].itemSelectionChanged.connect(lambda: self.updateButtonAvailability(W_IDX))
        self.tables[Z_IDX].itemSelectionChanged.connect(lambda: self.updateButtonAvailability(Z_IDX))
        self.tables[D_IDX].itemSelectionChanged.connect(lambda: self.updateButtonAvailability(D_IDX))
        self.tables[C_IDX].itemSelectionChanged.connect(lambda: self.updateButtonAvailability(C_IDX))

        # set initial button enabled/disabled state
        for i in range(4):
            self.updateButtonAvailability(i)

        self.mainWindow.show()

    def connectButtons(self):
        # "New" buttons
        self.mainUi.buttonNewWearable.clicked.connect(lambda: self.editWearable(True))
        self.mainUi.buttonNewZone.clicked.connect(lambda: self.editZone(True))
        self.mainUi.buttonNewDevice.clicked.connect(lambda: self.editDevice(True))

        # "Edit" buttons
        self.mainUi.buttonEditWearable.clicked.connect(lambda: self.editWearable(False))
        self.mainUi.buttonEditZone.clicked.connect(lambda: self.editZone(False))
        self.mainUi.buttonEditDevice.clicked.connect(lambda: self.editDevice(False))
        self.mainUi.buttonEditConfig.clicked.connect(lambda: self.editConfig())

        # "Delete" buttons
        self.mainUi.buttonDeleteWearable.clicked.connect(lambda: self.deleteWearable())
        self.mainUi.buttonDeleteZone.clicked.connect(lambda: self.deleteZone())
        self.mainUi.buttonDeleteDevice.clicked.connect(lambda: self.deleteDevice())

        # dialog "Cancel" buttons
        self.dialogUis[W_IDX].buttonCancel.clicked.connect(lambda: self.dialogs[W_IDX].hide())
        self.dialogUis[Z_IDX].buttonCancel.clicked.connect(lambda: self.dialogs[Z_IDX].hide())
        self.dialogUis[D_IDX].buttonCancel.clicked.connect(lambda: self.dialogs[D_IDX].hide())
        self.dialogUis[C_IDX].buttonCancel.clicked.connect(lambda: self.dialogs[C_IDX].hide())

        # dialog "Save" buttons
        # self.dialogUis[W_IDX].buttonSave.clicked.connect(lambda: self.dialogs[W_IDX].hide())
        # self.dialogUis[Z_IDX].buttonSave.clicked.connect(lambda: self.dialogs[Z_IDX].hide())
        # self.dialogUis[D_IDX].buttonSave.clicked.connect(lambda: self.dialogs[D_IDX].hide())
        # self.dialogUis[C_IDX].buttonSave.clicked.connect(lambda: self.dialogs[C_IDX].hide())

    def editWearable(self, isNew):
        self.newFlag = isNew
        wearable = None
        if (isNew):
            wearable = self.systemState.newWearable()
        else:
            wearable = self.systemState.getWearableByName(self.tables[W_IDX].selectedItems()[0].text())
        self.dialogUis[W_IDX].inputName.setPlainText(wearable.name)
        self.refreshWearableDropdown()
        self.dialogs[W_IDX].show()

    def editZone(self, isNew):
        self.newFlag = isNew
        zone = None
        if (isNew):
            zone = self.systemState.newZone()
        else:
            zone = self.systemState.getZoneByName(self.tables[Z_IDX].selectedItems()[0].text())
        self.dialogUis[Z_IDX].inputName.setPlainText(zone.name)
        self.refreshZoneModuleDropdown()
        self.dialogs[Z_IDX].show()

    def editDevice(self, isNew):
        self.newFlag = isNew
        device = None
        if (isNew):
            device = self.systemState.newDevice()
        else:
            device = self.systemState.getDeviceByName(self.tables[D_IDX].selectedItems()[0].text())
        self.dialogUis[D_IDX].inputName.setPlainText(device.name)
        self.refreshDeviceDropdown()
        self.dialogs[D_IDX].show()

    def editConfig(self):
        self.dialogs[C_IDX].show()

    # def saveWearable(self):

    # def saveZone(self):

    # def saveDevice(self):

    # def saveConfig(self):

    def deleteWearable(self):
        self.systemState.deleteWearableByName(self.tables[W_IDX].selectedItems()[0].text())
        self.tables[W_IDX].removeRow(self.tables[W_IDX].currentRow())

    def deleteZone(self):
        self.systemState.deleteZoneByName(self.tables[Z_IDX].selectedItems()[0].text())
        self.tables[Z_IDX].removeRow(self.tables[Z_IDX].currentRow())

    def deleteDevice(self):
        self.systemState.deleteDeviceByName(self.tables[D_IDX].selectedItems()[0].text())
        self.tables[D_IDX].removeRow(self.tables[D_IDX].currentRow())

    def updateButtonAvailability(self, tableId):
        shouldEnable = ( len(self.tables[tableId].selectedIndexes()) != 0)
        buttons = self.buttonGroups[tableId]
        for i in range(2): # only update edit & delete buttons
            buttons[i].setEnabled(shouldEnable)

    def refreshWearableDropdown(self):
        # TODO
        if (self.dialogUis[W_IDX].dropdownWearable.count() == 0):
            self.dialogUis[W_IDX].dropdownWearable.addItem("< no unassigned wearables detected >", None)

    def refreshZoneModuleDropdown(self):
        # TODO
        if (self.dialogUis[Z_IDX].dropdownModule.count() == 0):
            self.dialogUis[Z_IDX].dropdownModule.addItem("< no unassigned modules detected >", None)

    def refreshDeviceDropdown(self):
        # TODO
        if (self.dialogUis[D_IDX].dropdownDevice.count() == 0):
            self.dialogUis[D_IDX].dropdownDevice.addItem("< no unassigned devices detected >", None)

    def refreshConfigDropdowns(self):
        # TODO
        if (self.dialogUis[C_IDX].dropdownZone.count() == 0):
            self.dialogUis[C_IDX].dropdownZone.addItem("< no zones exist >", None)

    def populateTables(self):
        for wearable in self.systemState.wearables:
            self.tables[W_IDX].insertRow(0)
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(wearable.name)
            self.tables[W_IDX].setItem(0, 0, item)
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(str(wearable.hwId))
            self.tables[W_IDX].setItem(0, 1, item)