from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QDialog, QTableWidgetItem
from ui_mainscreen import Ui_MainScreen
from ui_wearabledialog import Ui_WearableDialog
from ui_zonedialog import Ui_ZoneDialog
from ui_devicedialog import Ui_DeviceDialog
from ui_configdialog import Ui_ConfigDialog
from drew_util import *
from constants import *

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

        self.connectUiElements()

        # populate tables with current system info
        self.populateTables()

        # populate device type dropdown
        dropdown = self.dialogUis[TID_D].dropdownType
        for deviceType in DEVICE_TYPES.keys():
            dropdown.addItem(DEVICE_TYPES[deviceType], deviceType)

        # set initial button enabled/disabled state, etc
        for i in range(4):
            self.selectionUpdate(i)

        # let's go!
        self.mainWindow.show()

    def connectUiElements(self):
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
        self.mainUi.buttonDeleteWearable.clicked.connect(lambda: self.deleteTableEntry(TID_W))
        self.mainUi.buttonDeleteZone.clicked.connect(lambda: self.deleteTableEntry(TID_Z))
        self.mainUi.buttonDeleteDevice.clicked.connect(lambda: self.deleteTableEntry(TID_D))

        # dialog "Cancel" buttons
        self.dialogUis[TID_W].buttonCancel.clicked.connect(lambda: self.cancelWearable())
        self.dialogUis[TID_Z].buttonCancel.clicked.connect(lambda: self.dialogs[TID_Z].hide())
        self.dialogUis[TID_D].buttonCancel.clicked.connect(lambda: self.dialogs[TID_D].hide())
        self.dialogUis[TID_C].buttonCancel.clicked.connect(lambda: self.dialogs[TID_C].hide())

        # dialog "Save" buttons -- TODO
        self.dialogUis[TID_W].buttonSave.clicked.connect(lambda: self.saveWearable())
        self.dialogUis[TID_Z].buttonSave.clicked.connect(lambda: self.saveZone())
        self.dialogUis[TID_D].buttonSave.clicked.connect(lambda: self.saveDevice())

        # dialog "Refresh List" buttons -- TODO
        self.dialogUis[TID_W].buttonRefresh.clicked.connect(lambda: self.refreshWearableDropdown())
        self.dialogUis[TID_Z].buttonRefresh.clicked.connect(lambda: self.refreshZoneModuleDropdown())
        self.dialogUis[TID_D].buttonRefresh.clicked.connect(lambda: self.refreshDeviceDropdown())

        # enable/disable buttons when table selection changes, etc
        self.tables[TID_W].itemSelectionChanged.connect(lambda: self.selectionUpdate(TID_W))
        self.tables[TID_Z].itemSelectionChanged.connect(lambda: self.selectionUpdate(TID_Z))
        self.tables[TID_D].itemSelectionChanged.connect(lambda: self.selectionUpdate(TID_D))
        self.tables[TID_C].itemSelectionChanged.connect(lambda: self.selectionUpdate(TID_C))

        # link values of zone threshold slider & spinner 
        spinner = self.dialogUis[TID_Z].spinnerThreshold
        slider = self.dialogUis[TID_Z].sliderThreshold
        spinner.valueChanged.connect(lambda: slider.setValue(spinner.value()))
        slider.valueChanged.connect(lambda: spinner.setValue(slider.value()))

    def editWearable(self, isNew):
        self.newFlag = isNew
        if (isNew):
            wearable = self.systemState.newWearable()
            self.currXmlId = wearable.xmlId
        else:
            wearable = self.systemState.getHardwareObject(TID_W, self.currXmlId)
        self.dialogUis[TID_W].inputName.setPlainText(wearable.name)
        self.refreshWearableDropdown()
        self.dialogs[TID_W].show()

    def editZone(self, isNew):
        self.newFlag = isNew
        if (isNew):
            zone = self.systemState.newZone()
            self.currXmlId = zone.xmlId
        else:
            zone = self.systemState.getHardwareObject(TID_Z, self.currXmlId)
        self.dialogUis[TID_Z].inputName.setPlainText(zone.name)
        self.dialogUis[TID_Z].spinnerThreshold.setValue(zone.threshold)
        self.refreshZoneModuleDropdown()
        self.dialogs[TID_Z].show()

    def editDevice(self, isNew):
        self.newFlag = isNew
        if (isNew):
            device = self.systemState.newDevice()
            self.currXmlId = device.xmlId
        else:
            device = self.systemState.getHardwareObject(TID_D, self.currXmlId)
        self.dialogUis[TID_D].inputName.setPlainText(device.name)
        self.refreshDeviceDropdown()
        self.dialogs[TID_D].show()

    def editConfig(self):
        self.dialogs[TID_C].show()

    def cancelWearable(self):
        if (self.newFlag):
            self.systemState.deleteHardwareObject(TID_W, self.currXmlId)
        self.dialogs[TID_W].hide()

    def saveWearable(self):
        wearable = self.systemState.getHardwareObject(TID_W, self.currXmlId)
        wearable.name = self.dialogUis[TID_W].inputName.toPlainText()
        wearable.hwId = self.dialogUis[TID_W].dropdownWearable.currentData()
        self.updateWearableTable(wearable, self.newFlag)
        self.dialogs[TID_W].hide()
        # TODO -- disallow non-unique names and hwId of -1 (i.e. the "no wearables" option)

    def saveZone(self):
        zone = self.systemState.getHardwareObject(TID_Z, self.currXmlId)
        zone.name = self.dialogUis[TID_Z].inputName.toPlainText()
        zone.hwId = self.dialogUis[TID_Z].dropdownModule.currentData()
        zone.threshold = self.dialogUis[TID_Z].spinnerThreshold.value()
        self.updateZoneTable(zone, self.newFlag)
        self.dialogs[TID_Z].hide()
        # TODO -- disallow non-unique names and hwId of -1 (i.e. the "no modules" option)

    def saveDevice(self):
        device = self.systemState.getHardwareObject(TID_D, self.currXmlId)
        device.name = self.dialogUis[TID_D].inputName.toPlainText()
        device.hwId = self.dialogUis[TID_D].dropdownDevice.currentData()
        device.devType = self.dialogUis[TID_D].dropdownType.currentData()
        self.updateDeviceTable(device, self.newFlag)
        self.dialogs[TID_D].hide()

    def deleteTableEntry(self, typeId):
        self.systemState.deleteHardwareObject(typeId, self.currXmlId)
        self.tables[typeId].removeRow(self.tables[typeId].currentRow())

    def selectionUpdate(self, tableIdx):
        items = self.tables[tableIdx].selectedItems()
        if (len(items) > 0):
            self.currXmlId = items[0].data(1)
        shouldEnable = ( len(self.tables[tableIdx].selectedIndexes()) != 0)
        buttons = self.buttonGroups[tableIdx]
        for i in range(2): # only update edit & delete buttons
            buttons[i].setEnabled(shouldEnable)

    def refreshWearableDropdown(self):
        hwIdList = self.systemState.discoverHardware(TID_W)
        dropdown = self.dialogUis[TID_W].dropdownWearable
        dropdown.clear()

        if (len(hwIdList) == 0):
            dropdown.addItem("< no unassigned wearables detected >", -1)
        else:
            for hwId in hwIdList:
                dropdown.addItem(str(hwId), hwId)

        # add and select current hwId if editing existing wearable
        if (not self.newFlag):
            wearable = self.systemState.getHardwareObject(TID_W, self.currXmlId)
            dropdown.insertItem(0, str(wearable.hwId), int(wearable.hwId))
            dropdown.setCurrentIndex(0)

    def refreshZoneModuleDropdown(self):
        hwIdList = self.systemState.discoverHardware(TID_Z)
        dropdown = self.dialogUis[TID_Z].dropdownModule
        dropdown.clear()

        if (len(hwIdList) == 0):
            dropdown.addItem("< no unassigned modules detected >", -1)
        else:
            for hwId in hwIdList:
                dropdown.addItem(str(hwId), hwId)

        # add and select current hwId if editing existing zone
        if (not self.newFlag):
            zone = self.systemState.getHardwareObject(TID_Z, self.currXmlId)
            dropdown.insertItem(0, str(zone.hwId), int(zone.hwId))
            dropdown.setCurrentIndex(0)

    def refreshDeviceDropdown(self):
        hwIdList = self.systemState.discoverHardware(TID_D)
        dropdown = self.dialogUis[TID_D].dropdownDevice
        dropdown.clear()

        if (len(hwIdList) == 0):
            dropdown.addItem("< no unassigned devices detected >", None)
        else:
            for hwId in hwIdList:
                dropdown.addItem(str(hwId), hwId)

        # add and select current hwId if editing existing zone
        if (not self.newFlag):
            device = self.systemState.getHardwareObject(TID_D, self.currXmlId)
            dropdown.insertItem(0, str(device.hwId), int(device.hwId))
            dropdown.setCurrentIndex(0)

    def refreshConfigDropdowns(self):
        # TODO
        if (self.dialogUis[TID_C].dropdownZone.count() == 0):
            self.dialogUis[TID_C].dropdownZone.addItem("< no zones exist >", None)

    def populateTables(self):
        for wearable in self.systemState.dicts[TID_W].values():
            self.updateWearableTable(wearable, True)

        for zone in self.systemState.dicts[TID_Z].values():
            self.updateZoneTable(zone, True)

        for device in self.systemState.dicts[TID_D].values():
            self.updateDeviceTable(device, True)

        # TODO table of device configurations

    def updateWearableTable(self, wearable, isNew):
        if (isNew):
            self.tables[TID_W].insertRow(0)
            # "Name" item with xmlId data
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(wearable.name)
            item.setData(1, wearable.xmlId)
            self.tables[TID_W].setItem(0, 0, item)
            # "Wearable ID" item
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(str(wearable.hwId))
            self.tables[TID_W].setItem(0, 1, item)
        else:
            items = self.tables[TID_W].selectedItems()
            items[0].setText(wearable.name)
            items[1].setText(str(wearable.hwId))

    def updateZoneTable(self, zone, isNew):
        if (isNew):
            self.tables[TID_Z].insertRow(0)
            # "Name" item with xmlId data
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(zone.name)
            item.setData(1, zone.xmlId)
            self.tables[TID_Z].setItem(0, 0, item)
            # "Module ID" item
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(str(zone.hwId))
            self.tables[TID_Z].setItem(0, 1, item)
            # "Threshold" item
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(str(zone.threshold))
            self.tables[TID_Z].setItem(0, 2, item)
        else:
            items = self.tables[TID_Z].selectedItems()
            items[0].setText(zone.name)
            items[1].setText(str(zone.hwId))
            items[2].setText(str(zone.threshold))

    def updateDeviceTable(self, device, isNew):
        if (isNew):
            self.tables[TID_D].insertRow(0)
            # "Name" item with xmlId data
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(device.name)
            item.setData(1, device.xmlId)
            self.tables[TID_D].setItem(0, 0, item)
            # "Type" item
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(DEVICE_TYPES[device.devType])
            self.tables[TID_D].setItem(0, 1, item)
            # "State" item
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText("TODO")
            self.tables[TID_D].setItem(0, 2, item)
        else:
            items = self.tables[TID_D].selectedItems()
            items[0].setText(device.name)
            items[1].setText(DEVICE_TYPES[device.devType])
            items[2].setText("TODO")