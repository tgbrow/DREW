# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QTableWidgetItem
from ui_wearabledialog import Ui_WearableDialog
from ui_zonedialog import Ui_ZoneDialog
from ui_devicedialog import Ui_DeviceDialog
from ui_configdialog import Ui_ConfigDialog
from classes import Wearable

BUT_EDIT    = 0
BUT_DELETE  = 1
BUT_NEW     = 2

TABLE_WEARABLE  = 0
TABLE_ZONE      = 1
TABLE_DEVICE    = 2
TABLE_CONFIG    = 3

class Ui_MainScreen(object):
    def setupUi(self, MainScreen, systemState):
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(500, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainScreen.sizePolicy().hasHeightForWidth())
        MainScreen.setSizePolicy(sizePolicy)
        MainScreen.setMinimumSize(QtCore.QSize(500, 650))
        MainScreen.setMaximumSize(QtCore.QSize(500, 650))
        self.tabWidget = QtWidgets.QTabWidget(MainScreen)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 480, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tabStatus = QtWidgets.QWidget()
        self.tabStatus.setAccessibleName("")
        self.tabStatus.setObjectName("tabStatus")
        self.tableStatus = QtWidgets.QTableWidget(self.tabStatus)
        self.tableStatus.setGeometry(QtCore.QRect(10, 10, 450, 580))
        self.tableStatus.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableStatus.setAlternatingRowColors(False)
        self.tableStatus.setObjectName("tableStatus")
        self.tableStatus.setColumnCount(2)
        self.tableStatus.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableStatus.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStatus.setHorizontalHeaderItem(1, item)
        self.tableStatus.horizontalHeader().setDefaultSectionSize(224)
        self.tableStatus.horizontalHeader().setSortIndicatorShown(False)
        self.tableStatus.horizontalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.tabStatus, "")
        self.tabHardware = QtWidgets.QWidget()
        self.tabHardware.setObjectName("tabHardware")
        self.tableWearable = QtWidgets.QTableWidget(self.tabHardware)
        self.tableWearable.setGeometry(QtCore.QRect(10, 30, 450, 130))
        self.tableWearable.setObjectName("tableWearable")
        self.tableWearable.setColumnCount(2)
        self.tableWearable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWearable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWearable.setHorizontalHeaderItem(1, item)
        self.tableWearable.horizontalHeader().setDefaultSectionSize(224)
        self.tableWearable.horizontalHeader().setStretchLastSection(True)
        self.layoutWidget = QtWidgets.QWidget(self.tabHardware)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 170, 451, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.buttonGroupWearable = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.buttonGroupWearable.setContentsMargins(0, 0, 0, 0)
        self.buttonGroupWearable.setObjectName("buttonGroupWearable")
        self.buttonEditWearable = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonEditWearable.setObjectName("buttonEditWearable")
        self.buttonGroupWearable.addWidget(self.buttonEditWearable)
        self.buttonDeleteWearable = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonDeleteWearable.setObjectName("buttonDeleteWearable")
        self.buttonGroupWearable.addWidget(self.buttonDeleteWearable)
        self.buttonNewWearable = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonNewWearable.setObjectName("buttonNewWearable")
        self.buttonGroupWearable.addWidget(self.buttonNewWearable)
        self.labelWearable = QtWidgets.QLabel(self.tabHardware)
        self.labelWearable.setGeometry(QtCore.QRect(10, 10, 90, 15))
        self.labelWearable.setObjectName("labelWearable")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tabHardware)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 570, 451, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.buttonGroupDevice = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.buttonGroupDevice.setContentsMargins(0, 0, 0, 0)
        self.buttonGroupDevice.setObjectName("buttonGroupDevice")
        self.buttonEditDevice = QtWidgets.QPushButton(self.layoutWidget_2)
        self.buttonEditDevice.setObjectName("buttonEditDevice")
        self.buttonGroupDevice.addWidget(self.buttonEditDevice)
        self.buttonDeleteDevice = QtWidgets.QPushButton(self.layoutWidget_2)
        self.buttonDeleteDevice.setObjectName("buttonDeleteDevice")
        self.buttonGroupDevice.addWidget(self.buttonDeleteDevice)
        self.buttonNewDevice = QtWidgets.QPushButton(self.layoutWidget_2)
        self.buttonNewDevice.setObjectName("buttonNewDevice")
        self.buttonGroupDevice.addWidget(self.buttonNewDevice)
        self.labelZone = QtWidgets.QLabel(self.tabHardware)
        self.labelZone.setGeometry(QtCore.QRect(10, 410, 111, 16))
        self.labelZone.setObjectName("labelZone")
        self.tableDevice = QtWidgets.QTableWidget(self.tabHardware)
        self.tableDevice.setGeometry(QtCore.QRect(10, 430, 450, 130))
        self.tableDevice.setObjectName("tableDevice")
        self.tableDevice.setColumnCount(3)
        self.tableDevice.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableDevice.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDevice.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDevice.setHorizontalHeaderItem(2, item)
        self.tableDevice.horizontalHeader().setDefaultSectionSize(149)
        self.tableDevice.horizontalHeader().setStretchLastSection(True)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tabHardware)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 370, 451, 25))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.buttonGroupZone = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.buttonGroupZone.setContentsMargins(0, 0, 0, 0)
        self.buttonGroupZone.setObjectName("buttonGroupZone")
        self.buttonEditZone = QtWidgets.QPushButton(self.layoutWidget_3)
        self.buttonEditZone.setObjectName("buttonEditZone")
        self.buttonGroupZone.addWidget(self.buttonEditZone)
        self.buttonDeleteZone = QtWidgets.QPushButton(self.layoutWidget_3)
        self.buttonDeleteZone.setObjectName("buttonDeleteZone")
        self.buttonGroupZone.addWidget(self.buttonDeleteZone)
        self.buttonNewZone = QtWidgets.QPushButton(self.layoutWidget_3)
        self.buttonNewZone.setObjectName("buttonNewZone")
        self.buttonGroupZone.addWidget(self.buttonNewZone)
        self.labelDevice = QtWidgets.QLabel(self.tabHardware)
        self.labelDevice.setGeometry(QtCore.QRect(10, 210, 91, 16))
        self.labelDevice.setObjectName("labelDevice")
        self.tableZone = QtWidgets.QTableWidget(self.tabHardware)
        self.tableZone.setGeometry(QtCore.QRect(10, 230, 450, 130))
        self.tableZone.setObjectName("tableZone")
        self.tableZone.setColumnCount(2)
        self.tableZone.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableZone.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableZone.setHorizontalHeaderItem(1, item)
        self.tableZone.horizontalHeader().setDefaultSectionSize(224)
        self.tableZone.horizontalHeader().setStretchLastSection(True)
        self.tabWidget.addTab(self.tabHardware, "")
        self.tabConfig = QtWidgets.QWidget()
        self.tabConfig.setObjectName("tabConfig")
        self.tableConfig = QtWidgets.QTableWidget(self.tabConfig)
        self.tableConfig.setGeometry(QtCore.QRect(10, 10, 450, 551))
        self.tableConfig.setObjectName("tableConfig")
        self.tableConfig.setColumnCount(4)
        self.tableConfig.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableConfig.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableConfig.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableConfig.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableConfig.setHorizontalHeaderItem(3, item)
        self.tableConfig.horizontalHeader().setDefaultSectionSize(112)
        self.tableConfig.horizontalHeader().setStretchLastSection(True)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tabConfig)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 570, 451, 25))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.buttonGroupConfig = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.buttonGroupConfig.setContentsMargins(0, 0, 0, 0)
        self.buttonGroupConfig.setObjectName("buttonGroupConfig")
        self.buttonEditConfig = QtWidgets.QPushButton(self.layoutWidget_4)
        self.buttonEditConfig.setObjectName("buttonEditConfig")
        self.buttonGroupConfig.addWidget(self.buttonEditConfig)
        self.buttonClearConfig = QtWidgets.QPushButton(self.layoutWidget_4)
        self.buttonClearConfig.setObjectName("buttonClearConfig")
        self.buttonGroupConfig.addWidget(self.buttonClearConfig)
        self.tabWidget.addTab(self.tabConfig, "")

        self.retranslateUi(MainScreen)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

        # my additions (not auto-generated by QtCreator)
        self.tableWearable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWearable.verticalHeader().setVisible(False)

        self.systemState = systemState
        self.manualSetup(MainScreen)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "D.R.E.W. System Tool"))
        item = self.tableStatus.horizontalHeaderItem(0)
        item.setText(_translate("MainScreen", "Zone Name"))
        item = self.tableStatus.horizontalHeaderItem(1)
        item.setText(_translate("MainScreen", "Wearables Present"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStatus), _translate("MainScreen", "Status"))
        item = self.tableWearable.horizontalHeaderItem(0)
        item.setText(_translate("MainScreen", "Name"))
        item = self.tableWearable.horizontalHeaderItem(1)
        item.setText(_translate("MainScreen", "Wearable ID"))
        self.buttonEditWearable.setText(_translate("MainScreen", "Edit"))
        self.buttonDeleteWearable.setText(_translate("MainScreen", "Delete"))
        self.buttonNewWearable.setText(_translate("MainScreen", "New"))
        self.labelWearable.setText(_translate("MainScreen", "Wearables:"))
        self.buttonEditDevice.setText(_translate("MainScreen", "Edit"))
        self.buttonDeleteDevice.setText(_translate("MainScreen", "Delete"))
        self.buttonNewDevice.setText(_translate("MainScreen", "New"))
        self.labelZone.setText(_translate("MainScreen", "Connected Devices:"))
        item = self.tableDevice.horizontalHeaderItem(0)
        item.setText(_translate("MainScreen", "Name"))
        item = self.tableDevice.horizontalHeaderItem(1)
        item.setText(_translate("MainScreen", "Type"))
        item = self.tableDevice.horizontalHeaderItem(2)
        item.setText(_translate("MainScreen", "State"))
        self.buttonEditZone.setText(_translate("MainScreen", "Edit"))
        self.buttonDeleteZone.setText(_translate("MainScreen", "Delete"))
        self.buttonNewZone.setText(_translate("MainScreen", "New"))
        self.labelDevice.setText(_translate("MainScreen", "Zones:"))
        item = self.tableZone.horizontalHeaderItem(0)
        item.setText(_translate("MainScreen", "Name"))
        item = self.tableZone.horizontalHeaderItem(1)
        item.setText(_translate("MainScreen", "Module ID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHardware), _translate("MainScreen", "Hardware Setup"))
        item = self.tableConfig.horizontalHeaderItem(0)
        item.setText(_translate("MainScreen", "Device"))
        item = self.tableConfig.horizontalHeaderItem(1)
        item.setText(_translate("MainScreen", "Containing Zone"))
        item = self.tableConfig.horizontalHeaderItem(2)
        item.setText(_translate("MainScreen", "Entry Action"))
        item = self.tableConfig.horizontalHeaderItem(3)
        item.setText(_translate("MainScreen", "Exit Action"))
        self.buttonEditConfig.setText(_translate("MainScreen", "Edit"))
        self.buttonClearConfig.setText(_translate("MainScreen", "Clear Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConfig), _translate("MainScreen", "System Setup"))


#----------
    

    def manualSetup(self, MainScreen):
        # set up dialogs
        self.wearableDialog = QDialog()
        self.wearableUi = Ui_WearableDialog()
        self.wearableUi.setupUi(self.wearableDialog)
        self.zoneDialog = QDialog()
        self.zoneUi = Ui_ZoneDialog()
        self.zoneUi.setupUi(self.zoneDialog)
        self.deviceDialog = QDialog()
        self.deviceUi = Ui_DeviceDialog()
        self.deviceUi.setupUi(self.deviceDialog)
        self.configDialog = QDialog()
        self.configUi = Ui_ConfigDialog()
        self.configUi.setupUi(self.configDialog)

        # group buttons into lists for convenience
        self.wearableButtons = [self.buttonEditWearable, self.buttonDeleteWearable, self.buttonNewWearable]
        self.zoneButtons = [self.buttonEditZone, self.buttonDeleteZone, self.buttonNewZone]
        self.deviceButtons = [self.buttonEditDevice, self.buttonDeleteDevice, self.buttonNewDevice]
        self.configButtons = [self.buttonEditConfig, self.buttonClearConfig]
        self.buttonGroups = [self.wearableButtons, self.zoneButtons, self.deviceButtons, self.configButtons]
        self.tables = [self.tableWearable, self.tableZone, self.tableDevice, self.tableConfig]

        # "New" buttons
        self.buttonNewWearable.clicked.connect(lambda: self.editWearable(True))
        self.buttonNewZone.clicked.connect(lambda: self.editZone(True))
        self.buttonNewDevice.clicked.connect(lambda: self.editDevice(True))

        # "Edit" buttons
        self.buttonEditWearable.clicked.connect(lambda: self.editWearable(False))
        self.buttonEditZone.clicked.connect(lambda: self.editZone(False))
        self.buttonEditDevice.clicked.connect(lambda: self.editDevice(False))
        self.buttonEditConfig.clicked.connect(lambda: self.editConfig())

        # "Delete" buttons
        self.buttonDeleteWearable.clicked.connect(lambda: self.deleteWearable())
        self.buttonDeleteZone.clicked.connect(lambda: self.deleteZone())
        self.buttonDeleteDevice.clicked.connect(lambda: self.deleteDevice())

        # dialog "Cancel" buttons
        self.wearableUi.buttonCancel.clicked.connect(lambda: self.wearableDialog.hide())
        self.deviceUi.buttonCancel.clicked.connect(lambda: self.deviceDialog.hide())
        self.zoneUi.buttonCancel.clicked.connect(lambda: self.zoneDialog.hide())
        self.configUi.buttonCancel.clicked.connect(lambda: self.configDialog.hide())

        # dialog "Save" buttons
        # self.wearableUi.buttonSave.clicked.connect(lambda: self.wearableDialog.hide())
        # self.deviceUi.buttonSave.clicked.connect(lambda: self.deviceDialog.hide())
        # self.zoneUi.buttonSave.clicked.connect(lambda: self.zoneDialog.hide())
        # self.configUi.buttonSave.clicked.connect(lambda: self.configDialog.hide())

        # populate tables with current system info
        self.populateTables()

        # enable/disable buttons when table selection changes
        self.tables[0].itemSelectionChanged.connect(lambda: self.updateButtonAvailability(0))
        self.tables[1].itemSelectionChanged.connect(lambda: self.updateButtonAvailability(1))
        self.tables[2].itemSelectionChanged.connect(lambda: self.updateButtonAvailability(2))
        self.tables[3].itemSelectionChanged.connect(lambda: self.updateButtonAvailability(3))

        # set initial button enabled/disabled state
        for i in range(4):
            self.updateButtonAvailability(i)

        
        
    def editWearable(self, isNew):
        self.newFlag = isNew
        wearable = None
        if (isNew):
            wearable = self.systemState.newWearable()
        else:
            wearable = self.systemState.getWearableByName(self.tableWearable.selectedItems()[0].text())
        self.wearableUi.inputName.setPlainText(wearable.name)
        self.refreshWearableDropdown()
        self.wearableDialog.show()

    def editZone(self, isNew):
        self.newFlag = isNew
        zone = None
        if (isNew):
            zone = self.systemState.newZone()
        else:
            zone = self.systemState.getZoneByName(self.tableZone.selectedItems()[0].text())
        self.zoneUi.inputName.setPlainText(zone.name)
        self.refreshZoneModuleDropdown()
        self.zoneDialog.show()

    def editDevice(self, isNew):
        self.newFlag = isNew
        device = None
        if (isNew):
            device = self.systemState.newDevice()
        else:
            device = self.systemState.getDeviceByName(self.tableDevice.selectedItems()[0].text())
        self.deviceUi.inputName.setPlainText(device.name)
        self.refreshDeviceDropdown()
        self.deviceDialog.show()

    def editConfig(self):
        self.configDialog.show()

    # def saveWearable(self):

    # def saveZone(self):

    # def saveDevice(self):

    # def saveConfig(self):

    def deleteWearable(self):
        self.systemState.deleteWearableByName(self.tableWearable.selectedItems()[0].text())
        self.tableWearable.removeRow(self.tableWearable.currentRow())

    def deleteZone(self):
        self.systemState.deleteZoneByName(self.tableZone.selectedItems()[0].text())
        self.tableZone.removeRow(self.tableZone.currentRow())

    def deleteDevice(self):
        self.systemState.deleteDeviceByName(self.tableDevice.selectedItems()[0].text())
        self.tableDevice.removeRow(self.tableDevice.currentRow())

    def updateButtonAvailability(self, tableId):
        shouldEnable = ( len(self.tables[tableId].selectedIndexes()) != 0)
        buttons = self.buttonGroups[tableId]
        for i in range(2): # only update edit & delete buttons
            buttons[i].setEnabled(shouldEnable)

    def refreshWearableDropdown(self):
        # TODO
        if (self.wearableUi.dropdownWearable.count() == 0):
            self.wearableUi.dropdownWearable.addItem("< no unassigned wearables detected >", None)

    def refreshZoneModuleDropdown(self):
        # TODO
        if (self.zoneUi.dropdownModule.count() == 0):
            self.zoneUi.dropdownModule.addItem("< no unassigned modules detected >", None)

    def refreshDeviceDropdown(self):
        # TODO
        if (self.deviceUi.dropdownDevice.count() == 0):
            self.deviceUi.dropdownDevice.addItem("< no unassigned devices detected >", None)

    def refreshConfigDropdowns(self):
        # TODO
        if (self.configUi.dropdownZone.count() == 0):
            self.configUi.dropdownZone.addItem("< no zones exist >", None)

    def populateTables(self):
        for wearable in self.systemState.wearables:
            self.tableWearable.insertRow(0)
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(wearable.name)
            self.tableWearable.setItem(0, 0, item)
            item = QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            item.setText(str(wearable.hwId))
            self.tableWearable.setItem(0, 1, item)

