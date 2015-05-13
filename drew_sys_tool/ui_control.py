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
        self.currXmlId = [-1, -1, -1, -1]

        self.mainWindow = QWidget()
        self.mainUi = Ui_MainScreen()
        self.mainUi.setupUi(self.mainWindow)

        self.dialogs = []
        for i in range(NUM_DIALOGS):
            dialog = QDialog()
            dialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint|QtCore.Qt.WindowTitleHint)
            self.dialogs.append(dialog)

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
        self.populateHardwareTables()

        # populate device type dropdown
        dropdown = self.dialogUis[TID_D].dropdownType
        for deviceType in DEVICE_TYPES.keys():
            dropdown.addItem(DEVICE_TYPES[deviceType], deviceType)

        # set initial button enabled/disabled state, etc
        for i in range(4):
            self.selectionUpdate(i)

        self.systemState.setSystemPause(RESUME)

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
        self.mainUi.buttonClearConfig.clicked.connect(lambda: self.clearConfig())

        # dialog "Cancel" buttons -- TODO
        self.dialogUis[TID_W].buttonCancel.clicked.connect(lambda: self.cancelHardwareDialog(TID_W))
        self.dialogUis[TID_Z].buttonCancel.clicked.connect(lambda: self.cancelHardwareDialog(TID_Z))
        self.dialogUis[TID_D].buttonCancel.clicked.connect(lambda: self.cancelHardwareDialog(TID_D))
        self.dialogUis[TID_C].buttonCancel.clicked.connect(lambda: self.cancelHardwareDialog(TID_C))

        # dialog "Save" buttons
        self.dialogUis[TID_W].buttonSave.clicked.connect(lambda: self.saveWearable())
        self.dialogUis[TID_Z].buttonSave.clicked.connect(lambda: self.saveZone())
        self.dialogUis[TID_D].buttonSave.clicked.connect(lambda: self.saveDevice())
        self.dialogUis[TID_C].buttonSave.clicked.connect(lambda: self.saveConfig())

        # dialog "Refresh List" buttons
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

        # 
        tabs = self.mainUi.tabWidget
        tabs.currentChanged.connect(lambda: self.tabChange(tabs.currentIndex()))

    def tabChange(self, tabNum):
        if (tabNum == TAB_STAT):
            return # TODO -- update status table
        elif (tabNum == TAB_HW):
            return # TODO -- (maybe do nothing, actually)
        else: # tabNum == TAB_SYS 
            self.createConfigTable()

    def editWearable(self, isNew):
        self.systemState.setSystemPause(PAUSE)
        self.newFlag = isNew
        if (isNew):
            wearable = self.systemState.newWearable()
            self.currXmlId[TID_W] = wearable.xmlId
        else:
            wearable = self.systemState.getHardwareObject(TID_W, self.currXmlId[TID_W])
        self.dialogUis[TID_W].inputName.setText(wearable.name)
        self.refreshWearableDropdown()
        self.dialogs[TID_W].show()

    def editZone(self, isNew):
        self.systemState.setSystemPause(PAUSE)
        self.newFlag = isNew
        if (isNew):
            zone = self.systemState.newZone()
            self.currXmlId[TID_Z] = zone.xmlId
        else:
            zone = self.systemState.getHardwareObject(TID_Z, self.currXmlId[TID_Z])
        self.dialogUis[TID_Z].inputName.setText(zone.name)
        self.dialogUis[TID_Z].spinnerThreshold.setValue(zone.threshold)
        self.refreshZoneModuleDropdown()
        self.dialogs[TID_Z].show()

    def editDevice(self, isNew):
        self.systemState.setSystemPause(PAUSE)
        self.newFlag = isNew
        if (isNew):
            device = self.systemState.newDevice()
            self.currXmlId[TID_D] = device.xmlId
        else:
            device = self.systemState.getHardwareObject(TID_D, self.currXmlId[TID_D])
        self.dialogUis[TID_D].inputName.setText(device.name)
        self.refreshDeviceDropdown()
        self.dialogs[TID_D].show()

    def editConfig(self):
        self.systemState.setSystemPause(PAUSE)
        device = self.systemState.getHardwareObject(TID_D, self.currXmlId[TID_C])
        self.dialogUis[TID_C].labelConfig.setText("Configuration for \"" + device.name + "\"")
        self.populateConfigDropdowns(device)
        self.dialogs[TID_C].show()

    def cancelHardwareDialog(self, typeId):
        if (typeId != TID_C):
            if (self.newFlag):
                self.systemState.deleteHardwareObject(typeId, self.currXmlId[typeId])
            self.selectionUpdate(typeId)

        self.systemState.setSystemPause(RESUME)
        self.dialogs[typeId].hide()

    def saveWearable(self):
        print('saveWearable: ', self.currXmlId)
        wearable = self.systemState.getHardwareObject(TID_W, self.currXmlId[TID_W])
        wearable.name = self.dialogUis[TID_W].inputName.text()
        wearable.hwId = self.dialogUis[TID_W].dropdownWearable.currentData()
        self.updateWearableTable(wearable, self.newFlag)
        self.selectionUpdate(TID_W)
        self.systemState.setSystemPause(RESUME)
        self.dialogs[TID_W].hide()
        # TODO -- disallow non-unique names and hwId of -1 (i.e. the "no wearables" option)

    def saveZone(self):
        zone = self.systemState.getHardwareObject(TID_Z, self.currXmlId[TID_Z])
        zone.name = self.dialogUis[TID_Z].inputName.text()
        zone.hwId = self.dialogUis[TID_Z].dropdownModule.currentData()
        zone.threshold = self.dialogUis[TID_Z].spinnerThreshold.value()
        self.updateZoneTable(zone, self.newFlag)
        self.selectionUpdate(TID_Z)
        self.systemState.setSystemPause(RESUME)
        self.dialogs[TID_Z].hide()
        # TODO -- disallow non-unique names and hwId of -1 (i.e. the "no modules" option)

    def saveDevice(self):
        device = self.systemState.getHardwareObject(TID_D, self.currXmlId[TID_D])
        device.name = self.dialogUis[TID_D].inputName.text()
        device.hwId = self.dialogUis[TID_D].dropdownDevice.currentData()
        device.devType = self.dialogUis[TID_D].dropdownType.currentData()
        self.updateDeviceTable(device, self.newFlag)
        self.selectionUpdate(TID_D)
        self.systemState.setSystemPause(RESUME)
        self.dialogs[TID_D].hide()
        # TODO -- disallow non-unique names and hwId of -1 (i.e. the "no devices" option)

    def saveConfig(self):
        configUi = self.dialogUis[TID_C]
        device = self.systemState.getHardwareObject(TID_D, self.currXmlId[TID_C])
        device.zone = configUi.dropdownZone.currentData()
        device.enter = configUi.dropdownEntryAction.currentData()
        device.exit = configUi.dropdownExitAction.currentData()
        self.updateConfigTableEntry(device)
        self.selectionUpdate(TID_C)
        self.systemState.setSystemPause(RESUME)
        self.dialogs[TID_C].hide()

    def deleteTableEntry(self, typeId):
        # TODO -- handle (attempted) deletion of a zone used by device config(s)
        self.systemState.setSystemPause(PAUSE)
        self.systemState.deleteHardwareObject(typeId, self.currXmlId[typeId])
        self.tables[typeId].removeRow(self.tables[typeId].currentRow())
        self.systemState.setSystemPause(RESUME)

    def clearConfig(self):
        self.systemState.setSystemPause(PAUSE)
        device = self.systemState.getHardwareObject(TID_D, self.currXmlId[TID_C])
        device.zone = -1
        device.enter = 0
        device.exit = 0
        self.updateConfigTableEntry(device)
        self.systemState.setSystemPause(RESUME)

    def selectionUpdate(self, tableIdx):
        items = self.tables[tableIdx].selectedItems()
        if (len(items) > 0):
            self.currXmlId[tableIdx] = items[0].data(1)
        else:
            self.currXmlId[tableIdx] = -1
        shouldEnable = ( len(self.tables[tableIdx].selectedIndexes()) != 0)
        buttons = self.buttonGroups[tableIdx]
        for i in range(2): # only update edit & delete buttons
            buttons[i].setEnabled(shouldEnable)

    def refreshWearableDropdown(self):
        hwIdList = self.systemState.discoverHardware(TID_W)
        dropdown = self.dialogUis[TID_W].dropdownWearable
        dropdown.clear()

        if (len(hwIdList) == 0):
            dropdown.addItem("[no unassigned wearables detected]", -1)
        else:
            for hwId in hwIdList:
                dropdown.addItem(str(hwId), hwId)

        # add and select current hwId if editing existing wearable
        if (not self.newFlag):
            wearable = self.systemState.getHardwareObject(TID_W, self.currXmlId[TID_W])
            dropdown.insertItem(0, str(wearable.hwId), int(wearable.hwId))
            dropdown.setCurrentIndex(0)

    def refreshZoneModuleDropdown(self):
        hwIdList = self.systemState.discoverHardware(TID_Z)
        dropdown = self.dialogUis[TID_Z].dropdownModule
        dropdown.clear()

        if (len(hwIdList) == 0):
            dropdown.addItem("[no unassigned modules detected]", -1)
        else:
            for hwId in hwIdList:
                dropdown.addItem(str(hwId), hwId)

        # add and select current hwId if editing existing zone
        if (not self.newFlag):
            zone = self.systemState.getHardwareObject(TID_Z, self.currXmlId[TID_Z])
            dropdown.insertItem(0, str(zone.hwId), int(zone.hwId))
            dropdown.setCurrentIndex(0)

    def refreshDeviceDropdown(self):
        hwIdList = self.systemState.discoverHardware(TID_D)
        dropdown = self.dialogUis[TID_D].dropdownDevice
        dropdown.clear()

        if (len(hwIdList) == 0):
            dropdown.addItem("[no unassigned devices detected]", -1)
        else:
            for hwId in hwIdList:
                dropdown.addItem(str(hwId), hwId)

        # add and select current hwId if editing existing zone
        if (not self.newFlag):
            device = self.systemState.getHardwareObject(TID_D, self.currXmlId[TID_D])
            dropdown.insertItem(0, str(device.hwId), device.hwId)
            dropdown.setCurrentIndex(0)

    def populateConfigDropdowns(self, device):
        configUi = self.dialogUis[TID_C]
        dropdown = configUi.dropdownZone
        dropdown.clear()

        for zone in self.systemState.dicts[TID_Z].values():
            dropdown.addItem(zone.name, zone.xmlId)
            if (zone.xmlId == device.zone):
                dropdown.setCurrentIndex(dropdown.count()-1)

        if (dropdown.count() == 0):
            dropdown.addItem("[no zones exist]", -1)

        actions = DEVICE_ACTIONS[device.devType]
        dropdown = configUi.dropdownEntryAction
        dropdown.clear()
        dropdown2 = configUi.dropdownExitAction
        dropdown2.clear()

        for actionId in DEVICE_ACTIONS[device.devType].keys():
            dropdown.addItem(actions[actionId], actionId)
            if (actionId == device.enter):
                dropdown.setCurrentIndex(dropdown.count()-1)
            dropdown2.addItem(actions[actionId], actionId)
            if (actionId == device.exit):
                dropdown2.setCurrentIndex(dropdown2.count()-1)

    def populateHardwareTables(self):
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

    def createConfigTable(self):
        configTable = self.tables[TID_C]
        configTable.clearContents()
        for i in range(configTable.rowCount()):
            configTable.removeRow(0)
        for device in self.systemState.dicts[TID_D].values():
            configTable.insertRow(0)
            # "Device" item with xmlId data
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(device.name)
            item.setData(1, device.xmlId)
            configTable.setItem(0, 0, item)
            # "Containing Zone" item
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            if (device.zone == -1):
                text = "[unassigned]"
            else:
                text = self.systemState.dicts[TID_Z][device.zone].name
            item.setText(text)
            item.setData(1, device.zone)
            configTable.setItem(0, 1, item)
            # "Entry Action" item
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(DEVICE_ACTIONS[device.devType][device.enter])
            configTable.setItem(0, 2, item)
            # "Exit Action" item
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(DEVICE_ACTIONS[device.devType][device.exit])
            configTable.setItem(0, 3, item)

    def updateConfigTableEntry(self, device):
        items = self.tables[TID_C].selectedItems()
        if (device.zone == -1):
            text = "[unassigned]"
        else:
            text = self.systemState.dicts[TID_Z][device.zone].name
        items[1].setText(text)
        items[1].setData(1, device.zone)
        items[2].setText(DEVICE_ACTIONS[device.devType][device.enter])
        items[3].setText(DEVICE_ACTIONS[device.devType][device.exit])