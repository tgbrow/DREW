# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.tableStatus.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableStatus.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.tableWearable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWearable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWearable.setObjectName("tableWearable")
        self.tableWearable.setColumnCount(2)
        self.tableWearable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWearable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWearable.setHorizontalHeaderItem(1, item)
        self.tableWearable.horizontalHeader().setDefaultSectionSize(224)
        self.tableWearable.horizontalHeader().setStretchLastSection(True)
        self.tableWearable.verticalHeader().setVisible(False)
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
        self.tableDevice.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableDevice.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.tableDevice.verticalHeader().setVisible(False)
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
        self.tableZone.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableZone.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableZone.setObjectName("tableZone")
        self.tableZone.setColumnCount(3)
        self.tableZone.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableZone.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableZone.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableZone.setHorizontalHeaderItem(2, item)
        self.tableZone.horizontalHeader().setDefaultSectionSize(149)
        self.tableZone.horizontalHeader().setStretchLastSection(True)
        self.tableZone.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tabHardware, "")
        self.tabConfig = QtWidgets.QWidget()
        self.tabConfig.setObjectName("tabConfig")
        self.tableConfig = QtWidgets.QTableWidget(self.tabConfig)
        self.tableConfig.setGeometry(QtCore.QRect(10, 10, 450, 551))
        self.tableConfig.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableConfig.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.tableConfig.verticalHeader().setVisible(False)
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
        item = self.tableZone.horizontalHeaderItem(2)
        item.setText(_translate("MainScreen", "Threshold"))
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

