# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from ui_wearabledialog import Ui_WearableDialog
from ui_zonedialog import Ui_ZoneDialog
from ui_devicedialog import Ui_DeviceDialog
from enum import Enum

BUT_EDIT    = 0
BUT_DELETE  = 1
BUT_NEW     = 2

TABLE_WEARABLE  = 0
TABLE_ZONE      = 1
TABLE_DEVICE    = 2
TABLE_CONFIG    = 3

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
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
        self.buttonPanelWearable = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.buttonPanelWearable.setContentsMargins(0, 0, 0, 0)
        self.buttonPanelWearable.setObjectName("buttonPanelWearable")
        self.buttonEditWearable = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonEditWearable.setObjectName("buttonEditWearable")
        self.buttonPanelWearable.addWidget(self.buttonEditWearable)
        self.buttonDeleteWearable = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonDeleteWearable.setObjectName("buttonDeleteWearable")
        self.buttonPanelWearable.addWidget(self.buttonDeleteWearable)
        self.buttonNewWearable = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonNewWearable.setObjectName("buttonNewWearable")
        self.buttonPanelWearable.addWidget(self.buttonNewWearable)
        self.labelWearable = QtWidgets.QLabel(self.tabHardware)
        self.labelWearable.setGeometry(QtCore.QRect(10, 10, 90, 15))
        self.labelWearable.setObjectName("labelWearable")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tabHardware)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 570, 451, 25))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.buttonPanelDevice = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.buttonPanelDevice.setContentsMargins(0, 0, 0, 0)
        self.buttonPanelDevice.setObjectName("buttonPanelDevice")
        self.buttonEditDevice = QtWidgets.QPushButton(self.layoutWidget_2)
        self.buttonEditDevice.setObjectName("buttonEditDevice")
        self.buttonPanelDevice.addWidget(self.buttonEditDevice)
        self.buttonDeleteDevice = QtWidgets.QPushButton(self.layoutWidget_2)
        self.buttonDeleteDevice.setObjectName("buttonDeleteDevice")
        self.buttonPanelDevice.addWidget(self.buttonDeleteDevice)
        self.buttonNewDevice = QtWidgets.QPushButton(self.layoutWidget_2)
        self.buttonNewDevice.setObjectName("buttonNewDevice")
        self.buttonPanelDevice.addWidget(self.buttonNewDevice)
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
        self.buttonPanelZone = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.buttonPanelZone.setContentsMargins(0, 0, 0, 0)
        self.buttonPanelZone.setObjectName("buttonPanelZone")
        self.buttonEditZone = QtWidgets.QPushButton(self.layoutWidget_3)
        self.buttonEditZone.setObjectName("buttonEditZone")
        self.buttonPanelZone.addWidget(self.buttonEditZone)
        self.buttonDeleteZone = QtWidgets.QPushButton(self.layoutWidget_3)
        self.buttonDeleteZone.setObjectName("buttonDeleteZone")
        self.buttonPanelZone.addWidget(self.buttonDeleteZone)
        self.buttonNewZone = QtWidgets.QPushButton(self.layoutWidget_3)
        self.buttonNewZone.setObjectName("buttonNewZone")
        self.buttonPanelZone.addWidget(self.buttonNewZone)
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
        self.tabSystem = QtWidgets.QWidget()
        self.tabSystem.setObjectName("tabSystem")
        self.tableSystem = QtWidgets.QTableWidget(self.tabSystem)
        self.tableSystem.setGeometry(QtCore.QRect(10, 10, 450, 551))
        self.tableSystem.setObjectName("tableSystem")
        self.tableSystem.setColumnCount(4)
        self.tableSystem.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSystem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSystem.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSystem.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSystem.setHorizontalHeaderItem(3, item)
        self.tableSystem.horizontalHeader().setDefaultSectionSize(112)
        self.tableSystem.horizontalHeader().setStretchLastSection(True)
        self.layoutWidget_4 = QtWidgets.QWidget(self.tabSystem)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 570, 451, 25))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.buttonPanelSystem = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.buttonPanelSystem.setContentsMargins(0, 0, 0, 0)
        self.buttonPanelSystem.setObjectName("buttonPanelSystem")
        self.buttonEditSystem = QtWidgets.QPushButton(self.layoutWidget_4)
        self.buttonEditSystem.setObjectName("buttonEditSystem")
        self.buttonPanelSystem.addWidget(self.buttonEditSystem)
        self.buttonClearSystem = QtWidgets.QPushButton(self.layoutWidget_4)
        self.buttonClearSystem.setObjectName("buttonClearSystem")
        self.buttonPanelSystem.addWidget(self.buttonClearSystem)
        self.tabWidget.addTab(self.tabSystem, "")

        self.retranslateUi(MainScreen)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

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
        item = self.tableSystem.horizontalHeaderItem(0)
        item.setText(_translate("MainScreen", "Device"))
        item = self.tableSystem.horizontalHeaderItem(1)
        item.setText(_translate("MainScreen", "Containing Zone"))
        item = self.tableSystem.horizontalHeaderItem(2)
        item.setText(_translate("MainScreen", "Entry Action"))
        item = self.tableSystem.horizontalHeaderItem(3)
        item.setText(_translate("MainScreen", "Exit Action"))
        self.buttonEditSystem.setText(_translate("MainScreen", "Edit"))
        self.buttonClearSystem.setText(_translate("MainScreen", "Clear Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSystem), _translate("MainScreen", "System Setup"))


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

        self.wearableButtons = [self.buttonEditWearable, self.buttonDeleteWearable, self.buttonNewWearable]
        self.zoneButtons = [self.buttonEditZone, self.buttonDeleteZone, self.buttonNewZone]
        self.deviceButtons = [self.buttonEditDevice, self.buttonDeleteDevice, self.buttonNewDevice]
        self.buttonGroups = [self.wearableButtons, self.zoneButtons, self.deviceButtons]
        self.tables = [self.tableWearable, self.tableZone, self.tableDevice, self.tableSystem]

        # dialog cancel buttons
        self.wearableUi.buttonCancel.clicked.connect(lambda: self.wearableDialog.hide())
        self.deviceUi.buttonCancel.clicked.connect(lambda: self.deviceDialog.hide())
        self.zoneUi.buttonCancel.clicked.connect(lambda: self.zoneDialog.hide())

        # "New" buttons
        self.buttonNewWearable.clicked.connect(lambda: self.editWearable(True))
        self.buttonNewZone.clicked.connect(lambda: self.editZone(True))
        self.buttonNewDevice.clicked.connect(lambda: self.editDevice(True))

        # "Edit" buttons
        self.buttonEditWearable.clicked.connect(lambda: self.editWearable(False))
        self.buttonEditZone.clicked.connect(lambda: self.editZone(False))
        self.buttonEditDevice.clicked.connect(lambda: self.editDevice(False))

        # "Delete" buttons
        # self.buttonDeleteWearable.clicked.connect()
        # self.buttonDeleteZone.clicked.connect()
        # self.buttonDeleteDevice.clicked.connect()

        # enable/disable buttons based on selection
        for i in range(3):
            self.tables[i].itemSelectionChanged.connect(lambda: self.updateButtonAvailability(i))

        # set initial state of UI elements
        for i in range(3):
            self.updateButtonAvailability(i)
        
    def editWearable(self, isNew):
        if (isNew):
            self.wearableUi.inputName.setPlainText("")
        else:
            self.wearableUi.inputName.setPlainText("NAME_GOES_HERE")
        self.refreshWearableDropdown()
        self.wearableDialog.show()

    def editZone(self, isNew):
        if (isNew):
            self.zoneUi.inputName.setPlainText("")
        else:
            self.zoneUi.inputName.setPlainText("NAME_GOES_HERE")
        self.refreshZoneModuleDropdown()
        self.zoneDialog.show()

    def editDevice(self, isNew):
        if (isNew):
            self.deviceUi.inputName.setPlainText("")
        else:
            self.deviceUi.inputName.setPlainText("NAME_GOES_HERE")
        self.refreshDeviceDropdown()
        self.deviceDialog.show()

    def updateButtonAvailability(self, tableId):
        shouldEnable = ( len(self.tables[tableId].selectedIndexes()) != 0)
        buttons = self.buttonGroups[tableId]
        for i in range(2): # only update edit & delete buttons
            buttons[i].setEnabled(shouldEnable)

    def refreshWearableDropdown(self):
        # TODO
        self.wearableUi.dropdownWearable.addItem("< no unassigned wearables detected >", None)

    def refreshZoneModuleDropdown(self):
        # TODO
        self.zoneUi.dropdownModule.addItem("< no unassigned modules detected >", None)

    def refreshDeviceDropdown(self):
        # TODO
        self.deviceUi.dropdownDevice.addItem("< no unassigned devices detected >", None)