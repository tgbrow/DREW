from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QDialog, QTableWidgetItem
from ui_mainscreen import Ui_MainScreen
from ui_wearabledialog import Ui_WearableDialog
from ui_zonedialog import Ui_ZoneDialog
from ui_devicedialog import Ui_DeviceDialog
from ui_configdialog import Ui_ConfigDialog
from ui_pausechangedialog import Ui_PauseChangeDialog
from drew_util import *
from constants import *

# TODO -- "Discovering..." with waiting GIF on dropdown refresh

class UiControl:
    def __init__(self, systemState):
        self.systemState = systemState
        self.currXmlId = [-1, -1, -1, -1]

        self.iconPause = QtGui.QIcon("./images/pause.png")
        self.iconActivate = QtGui.QIcon("./images/play.png")
        self.iconWait = QtGui.QIcon("./images/wait.png")

        self.mainWindow = QWidget()
        self.mainUi = Ui_MainScreen()
        self.mainUi.setupUi(self.mainWindow)

        self.pauseChangeDialog = QDialog()
        self.pauseChangeDialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint|QtCore.Qt.WindowTitleHint|QtCore.Qt.WindowStaysOnTopHint)
        self.pauseChangeDialogUi = Ui_PauseChangeDialog()
        self.pauseChangeDialogUi.setupUi(self.pauseChangeDialog)
        self.pauseChangeGif = QtGui.QMovie("./images/waiting.gif")
        self.pauseChangeGif.setScaledSize(QtCore.QSize(130, 130))
        self.pauseChangeDialogUi.labelGIF.setMovie(self.pauseChangeGif)
        self.pauseChangeThread = PauseChangeThread(self.systemState)

        self.statusRefreshThread1 = StatusRefreshThread()
        self.statusRefreshThread2 = StatusRefreshThread()
        self.statuRefreshThreadSelect = False 

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
        self.createZoneOccupationTable()
        self.createDeviceStateTable()

        # populate device type dropdown
        dropdown = self.dialogUis[TID_D].dropdownType
        for deviceType in DEVICE_TYPES.keys():
            dropdown.addItem(DEVICE_TYPES[deviceType], deviceType)

        # set initial button enabled/disabled state, etc
        for i in range(4):
            self.selectionUpdate(i)

        # initially, system should be unpaused
        self.mainUi.labelPauseStatus.setText("<b>System Active<b>")
        self.mainUi.buttonPause.setIcon(self.iconPause)
        self.manuallyPaused = False

        # now that everything is set up, let the other threads start doing their thing
        self.systemState.setSystemPause(RESUME)

        # since we start in the status tab, we want to make sure it's updating when we begin
        self.statusRefresh()

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

        # dialog "Cancel" buttons
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

        # manual system pause/resume button
        self.mainUi.buttonPause.clicked.connect(lambda: self.beginPauseChange((not self.systemState.systemIsPaused), True))
        self.pauseChangeThread.doneSignal.connect(lambda: self.finishPauseChange())

        self.statusRefreshThread1.refreshSignal.connect(lambda: self.statusRefresh())
        self.statusRefreshThread2.refreshSignal.connect(lambda: self.statusRefresh())

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
            self.statusRefresh()
        elif (tabNum == TAB_SYS):
            self.createConfigTable()
        # other cases -> do nothing 

    def beginPauseChange(self, desiredAction, isManualChange):
        if (desiredAction == self.systemState.systemIsPaused):
            return # system is already in the desired state

        # manual changes are initiated by pressing the pause/resume button
        # automatic changes are initiated when editing any part of the system
        if (isManualChange):
            self.manuallyPaused = (desiredAction == PAUSE)

        if (desiredAction == PAUSE):
            waitText = "Pausing System..."
        else:
            waitText = "Resuming System... "
        self.mainUi.labelPauseStatus.setText(waitText)
        self.mainUi.buttonPause.setIcon(self.iconWait)

        self.pauseChangeDialog.setWindowTitle(waitText)
        self.pauseChangeGif.start()
        self.pauseChangeDialog.show()

        self.pauseChangeThread.setAction(desiredAction)
        self.pauseChangeThread.start()

    def finishPauseChange(self):
        if (self.systemState.systemIsPaused):
            doneText = "<b>System Paused</b>"
            newIcon = self.iconActivate 
        else:
            doneText = "<b>System Active<b>"
            newIcon = self.iconPause

        self.mainUi.buttonPause.setIcon(newIcon)
        self.mainUi.labelPauseStatus.setText(doneText)

        self.pauseChangeGif.stop()
        self.pauseChangeDialog.hide()

    def statusRefresh(self):
        zoTable = self.mainUi.tableZoneOccupation
        # update each row (zone) in zone occupation table
        for row in range(zoTable.rowCount()):
            items = [zoTable.item(row, 0), zoTable.item(row, 1)]
            zone = self.systemState.getHardwareObject(TID_Z, items[0].data(5))
            self.updateZoneOccupationTableRow(zone, items)

        dsTable = self.mainUi.tableDeviceState
        # update each row (zone) in zone occupation table
        for row in range(dsTable.rowCount()):
            items = [dsTable.item(row, 0), dsTable.item(row, 1)]
            device = self.systemState.getHardwareObject(TID_D, items[0].data(5))
            self.updateDeviceStateTableRow(device, items)

        # if still in status tab, need to keep refreshing
        if (self.mainUi.tabWidget.currentIndex() == TAB_STAT):
            # alternate between two refresh threads so signal emits don't "overlap"
            if (self.statuRefreshThreadSelect):
                self.statusRefreshThread1.start()
            else:
                self.statusRefreshThread2.start()
            self.statuRefreshThreadSelect = (not self.statuRefreshThreadSelect)

    def editWearable(self, isNew, isAfterPause=False):
        self.beginPauseChange(PAUSE, False)
        self.dialogUis[TID_W].labelInvalidName.setVisible(False)
        self.dialogUis[TID_W].labelInvalidWearable.setVisible(False)
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
        self.beginPauseChange(PAUSE, False)
        self.dialogUis[TID_Z].labelInvalidName.setVisible(False)
        self.dialogUis[TID_Z].labelInvalidModule.setVisible(False)
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
        self.beginPauseChange(PAUSE, False)
        self.dialogUis[TID_D].labelInvalidName.setVisible(False)
        self.dialogUis[TID_D].labelInvalidDevice.setVisible(False)
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
        self.beginPauseChange(PAUSE, False)
        self.dialogUis[TID_C].labelInvalidZone.setVisible(False)
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

        if (not self.manuallyPaused):
            self.beginPauseChange(RESUME, False)
        self.dialogs[typeId].hide()

    def saveWearable(self):
        givenName = (self.dialogUis[TID_W].inputName.text()).strip()
        if (self.systemState.nameInUse(TID_W, givenName, self.currXmlId[TID_W])):
            self.dialogUis[TID_W].labelInvalidName.setVisible(True)
            return
        else:
            self.dialogUis[TID_W].labelInvalidName.setVisible(False)

        selectedHwId = self.dialogUis[TID_W].dropdownWearable.currentData()
        if (selectedHwId == -1):
            self.dialogUis[TID_W].labelInvalidWearable.setVisible(True)
            return
        else:
            self.dialogUis[TID_W].labelInvalidWearable.setVisible(False)

        wearable = self.systemState.getHardwareObject(TID_W, self.currXmlId[TID_W])
        wearable.name = givenName
        wearable.hwId = selectedHwId
        self.updateWearableTable(wearable, self.newFlag)
        self.selectionUpdate(TID_W)
        if (not self.manuallyPaused):
            self.beginPauseChange(RESUME, False)
        self.dialogs[TID_W].hide()

    def saveZone(self):
        # disallow duplicate names
        givenName = (self.dialogUis[TID_Z].inputName.text()).strip()
        if (self.systemState.nameInUse(TID_Z, givenName, self.currXmlId[TID_Z])):
            self.dialogUis[TID_Z].labelInvalidName.setVisible(True)
            return
        else:
            self.dialogUis[TID_Z].labelInvalidName.setVisible(False)

        # disallow invalid hardware IDs
        selectedHwId = self.dialogUis[TID_Z].dropdownModule.currentData()
        if (selectedHwId == -1):
            self.dialogUis[TID_Z].labelInvalidModule.setVisible(True)
            return
        else:
            self.dialogUis[TID_Z].labelInvalidModule.setVisible(False)

        # input validated -- do the save operation
        zone = self.systemState.getHardwareObject(TID_Z, self.currXmlId[TID_Z])
        zone.name = givenName
        zone.hwId = selectedHwId
        zone.threshold = self.dialogUis[TID_Z].spinnerThreshold.value()
        self.updateZoneTable(zone, self.newFlag)
        self.selectionUpdate(TID_Z)

        # update zone occupation table in status tab
        if (self.newFlag):
            self.updateZoneOccupationTableRow(zone)
        else:
            zoTable = self.mainUi.tableZoneOccupation
            for row in range(zoTable.rowCount()):
                if (zoTable.item(row, 0).data(5) == zone.xmlId):
                    items = [zoTable.item(row, 0), zoTable.item(row, 1)]
                    self.updateZoneOccupationTableRow(zone, items)
                    break

        self.updateDeviceStateTableRow
        if (not self.manuallyPaused):
            self.beginPauseChange(RESUME, False)
        self.dialogs[TID_Z].hide()

    def saveDevice(self):
        # disallow duplicate names
        givenName = (self.dialogUis[TID_D].inputName.text()).strip()
        if (self.systemState.nameInUse(TID_D, givenName, self.currXmlId[TID_D])):
            self.dialogUis[TID_D].labelInvalidName.setVisible(True)
            return
        else:
            self.dialogUis[TID_D].labelInvalidName.setVisible(False)
        
        # disallow invalid hardware IDs
        selectedHwId = self.dialogUis[TID_D].dropdownDevice.currentData()
        if (selectedHwId == 'INVALID'):
            self.dialogUis[TID_D].labelInvalidDevice.setVisible(True)
            return
        else:
            self.dialogUis[TID_D].labelInvalidDevice.setVisible(False)

        # input validated -- do the save operation
        device = self.systemState.getHardwareObject(TID_D, self.currXmlId[TID_D])
        device.name = givenName
        device.hwId = selectedHwId
        device.devType = self.dialogUis[TID_D].dropdownType.currentData()
        self.updateDeviceTable(device, self.newFlag)
        self.selectionUpdate(TID_D)

        # update device state table in status tab
        if (self.newFlag):
            self.updateDeviceStateTableRow(zone)
        else:
            dsTable = self.mainUi.tableDeviceState
            for row in range(dsTable.rowCount()):
                if (dsTable.item(row, 0).data(5) == device.xmlId):
                    items = [dsTable.item(row, 0), dsTable.item(row, 1)]
                    self.updateDeviceStateTableRow(zone, items)
                    break

        if (not self.manuallyPaused):
            self.beginPauseChange(RESUME, False)
        self.dialogs[TID_D].hide()

    def saveConfig(self):
        configUi = self.dialogUis[TID_C]
        selectedZone = configUi.dropdownZone.currentData()
        if (selectedZone == -1):
            self.dialogUis[TID_C].labelInvalidZone.setVisible(True)
            return
        else:
            self.dialogUis[TID_C].labelInvalidZone.setVisible(False)

        device = self.systemState.getHardwareObject(TID_D, self.currXmlId[TID_C])
        device.zone = selectedZone
        device.enter = configUi.dropdownEntryAction.currentData()
        device.exit = configUi.dropdownExitAction.currentData()
        self.updateConfigTableEntry(device)
        self.selectionUpdate(TID_C)
        if (not self.manuallyPaused):
            self.beginPauseChange(RESUME, False)
        self.dialogs[TID_C].hide()

    # TODO -- if zone is deleted, remove it from status tab table
    # TODO -- if device is deleted, remove it from status tab table
    def deleteTableEntry(self, typeId):
        # TODO -- handle (attempted) deletion of a zone used by device config(s)
        self.systemState.setSystemPause(PAUSE)
        self.systemState.deleteHardwareObject(typeId, self.currXmlId[typeId])
        self.tables[typeId].removeRow(self.tables[typeId].currentRow())
        if (not self.manuallyPaused):
            self.beginPauseChange(RESUME, False)

    def clearConfig(self):
        self.systemState.setSystemPause(PAUSE)
        device = self.systemState.getHardwareObject(TID_D, self.currXmlId[TID_C])
        device.zone = -1
        device.enter = 0
        device.exit = 0
        self.updateConfigTableEntry(device)
        if (not self.manuallyPaused):
            self.beginPauseChange(RESUME, False)

    def selectionUpdate(self, tableIdx):
        items = self.tables[tableIdx].selectedItems()
        if (len(items) > 0):
            self.currXmlId[tableIdx] = items[0].data(5)
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

        for hwId in hwIdList:
            dropdown.addItem(str(hwId), hwId)

        if (not self.newFlag): # add and select current hwId if editing existing wearable
            wearable = self.systemState.getHardwareObject(TID_W, self.currXmlId[TID_W])
            dropdown.insertItem(0, str(wearable.hwId), int(wearable.hwId))
            dropdown.setCurrentIndex(0)
        elif (len(hwIdList) == 0):
            dropdown.addItem("[no unassigned wearables detected]", -1)

    def refreshZoneModuleDropdown(self):
        hwIdList = self.systemState.discoverHardware(TID_Z)
        dropdown = self.dialogUis[TID_Z].dropdownModule
        dropdown.clear()

        for hwId in hwIdList:
            dropdown.addItem(str(hwId), hwId)

        if (not self.newFlag): # add and select current hwId if editing existing zone
            zone = self.systemState.getHardwareObject(TID_Z, self.currXmlId[TID_Z])
            dropdown.insertItem(0, str(zone.hwId), int(zone.hwId))
            dropdown.setCurrentIndex(0)
        elif (len(hwIdList) == 0):
            dropdown.addItem("[no unassigned modules detected]", -1)

    def refreshDeviceDropdown(self):
        hwIdList = self.systemState.discoverHardware(TID_D)
        dropdown = self.dialogUis[TID_D].dropdownDevice
        dropdown.clear()

        for hwId, name in hwIdList:
            dropdown.addItem(hwId + " - " + name, hwId)

        # add and select current hwId if editing existing zone
        if (not self.newFlag):
            device = self.systemState.getHardwareObject(TID_D, self.currXmlId[TID_D])
            dropdown.insertItem(0, str(device.hwId), device.hwId)
            dropdown.setCurrentIndex(0)
        elif (len(hwIdList) == 0):
            dropdown.addItem("[no unassigned devices detected]", 'INVALID')

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

    def updateWearableTable(self, wearable, isNew):
        if (isNew):
            self.tables[TID_W].insertRow(0)
            # "Name" item with xmlId data
            item = QTableWidgetItem()
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
            item.setText(wearable.name)
            item.setData(5, wearable.xmlId)
            self.tables[TID_W].setItem(0, 0, item)
            # "Wearable ID" item
            item = QTableWidgetItem()
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
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
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
            item.setText(zone.name)
            item.setData(5, zone.xmlId)
            self.tables[TID_Z].setItem(0, 0, item)
            # "Module ID" item
            item = QTableWidgetItem()
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
            item.setText(str(zone.hwId))
            self.tables[TID_Z].setItem(0, 1, item)
            # "Threshold" item
            item = QTableWidgetItem()
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
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
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
            item.setText(device.name)
            item.setData(5, device.xmlId)
            self.tables[TID_D].setItem(0, 0, item)
            # "Bluetooth Address" item
            item = QTableWidgetItem()
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
            item.setText(device.hwId)
            self.tables[TID_D].setItem(0, 1, item)
            # "Type" item
            item = QTableWidgetItem()
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
            item.setText(DEVICE_TYPES[device.devType])
            self.tables[TID_D].setItem(0, 2, item)
        else:
            items = self.tables[TID_D].selectedItems()
            items[0].setText(device.name)
            items[2].setText(device.hwId)
            items[2].setText(DEVICE_TYPES[device.devType])

    def createConfigTable(self):
        configTable = self.tables[TID_C]
        configTable.clearContents()
        for i in range(configTable.rowCount()):
            configTable.removeRow(0)
        for device in self.systemState.dicts[TID_D].values():
            configTable.insertRow(0)
            # "Device" item with xmlId data
            item = QTableWidgetItem()
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
            item.setText(device.name)
            item.setData(5, device.xmlId)
            configTable.setItem(0, 0, item)
            # "Containing Zone" item
            item = QTableWidgetItem()
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
            if (device.zone == -1):
                text = "[unassigned]"
            else:
                text = self.systemState.dicts[TID_Z][device.zone].name
            item.setText(text)
            item.setData(5, device.zone)
            configTable.setItem(0, 1, item)
            # "Entry Action" item
            item = QTableWidgetItem()
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
            item.setText(DEVICE_ACTIONS[device.devType][device.enter])
            configTable.setItem(0, 2, item)
            # "Exit Action" item
            item = QTableWidgetItem()
            item.setTextAlignment(ITEM_ALIGN_FLAGS)
            item.setFlags(ITEM_INTERACT_FLAGS)
            item.setText(DEVICE_ACTIONS[device.devType][device.exit])
            configTable.setItem(0, 3, item)

    def updateConfigTableEntry(self, device):
        items = self.tables[TID_C].selectedItems()
        if (device.zone == -1):
            text = "[unassigned]"
        else:
            text = self.systemState.dicts[TID_Z][device.zone].name
        items[1].setText(text)
        items[1].setData(5, device.zone)
        items[2].setText(DEVICE_ACTIONS[device.devType][device.enter])
        items[3].setText(DEVICE_ACTIONS[device.devType][device.exit])

    def createZoneOccupationTable(self):
        for zone in self.systemState.dicts[TID_Z].values():
            self.updateZoneOccupationTableRow(zone)

    def updateZoneOccupationTableRow(self, zone, tableItems=None):
        zoTable = self.mainUi.tableZoneOccupation

        if (tableItems == None):
            tableItems = []
            for i in range(2):
                item = QTableWidgetItem()
                item.setTextAlignment(ITEM_ALIGN_FLAGS)
                item.setFlags(ITEM_INTERACT_FLAGS)
                tableItems.append(item)
            zoTable.insertRow(0)
            zoTable.setItem(0, 0, tableItems[0])
            zoTable.setItem(0, 1, tableItems[1])

        tableItems[0].setText(zone.name)
        tableItems[0].setData(5, zone.xmlId)

        wearablesPresent = ""
        firstOneFlag = True
        wearableIds = zone.wearablesInZone.keys()

        if (len(wearableIds) == 0):
            wearablesPresent = "[none]"
        else:
            for wearbleId in wearableIds:
                wearable = self.systemState.getHardwareObjectByHwId(TID_W, wearbleId)
                if (firstOneFlag):
                    firstOneFlag = False
                else:
                    wearablesPresent = wearablesPresent + ", "
                wearablesPresent = wearablesPresent + wearable.name

        tableItems[1].setText(wearablesPresent)

    def createDeviceStateTable(self):
        for device in self.systemState.dicts[TID_D].values():
            self.updateDeviceStateTableRow(device)

    def updateDeviceStateTableRow(self, device, tableItems=None):
        dsTable = self.mainUi.tableDeviceState

        if (tableItems == None):
            tableItems = []
            for i in range(2):
                item = QTableWidgetItem()
                item.setTextAlignment(ITEM_ALIGN_FLAGS)
                item.setFlags(ITEM_INTERACT_FLAGS)
                tableItems.append(item)
            dsTable.insertRow(0)
            dsTable.setItem(0, 0, tableItems[0])
            dsTable.setItem(0, 1, tableItems[1])

        tableItems[0].setText(device.name)
        tableItems[0].setData(5, device.xmlId)
        tableItems[1].setText(DEVICE_STATES[device.devType][device.state])

class PauseChangeThread(QtCore.QThread):
    isDone = False
    doneSignal = QtCore.pyqtSignal()
    action = RESUME

    def __init__(self, systemState):
        super().__init__()
        self.systemState = systemState

    def setAction(self, action):
        self.action = action

    def run(self):
        self.isDone = False
        self.systemState.setSystemPause(self.action)
        self.doneSignal.emit()
        self.isDone = True

class StatusRefreshThread(QtCore.QThread):
    refreshSignal = QtCore.pyqtSignal()

    def run(self):
        time.sleep(2)
        self.refreshSignal.emit()