# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connecteddevicedialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConnectedDeviceDialog(object):
    def setupUi(self, ConnectedDeviceDialog):
        ConnectedDeviceDialog.setObjectName("ConnectedDeviceDialog")
        ConnectedDeviceDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ConnectedDeviceDialog.resize(400, 300)
        self.labelName = QtWidgets.QLabel(ConnectedDeviceDialog)
        self.labelName.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.labelName.setObjectName("labelName")
        self.labelSelectDevice = QtWidgets.QLabel(ConnectedDeviceDialog)
        self.labelSelectDevice.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.labelSelectDevice.setObjectName("labelSelectDevice")
        self.inputName = QtWidgets.QPlainTextEdit(ConnectedDeviceDialog)
        self.inputName.setGeometry(QtCore.QRect(20, 40, 361, 21))
        self.inputName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.inputName.setObjectName("inputName")
        self.dropdownDevice = QtWidgets.QComboBox(ConnectedDeviceDialog)
        self.dropdownDevice.setGeometry(QtCore.QRect(20, 110, 361, 22))
        self.dropdownDevice.setObjectName("dropdownDevice")
        self.buttonRefresh = QtWidgets.QPushButton(ConnectedDeviceDialog)
        self.buttonRefresh.setGeometry(QtCore.QRect(310, 140, 71, 23))
        self.buttonRefresh.setObjectName("buttonRefresh")
        self.layoutWidget = QtWidgets.QWidget(ConnectedDeviceDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 260, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.buttonPanel = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.buttonPanel.setContentsMargins(0, 0, 0, 0)
        self.buttonPanel.setObjectName("buttonPanel")
        self.buttonCancel = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonCancel.setObjectName("buttonCancel")
        self.buttonPanel.addWidget(self.buttonCancel)
        self.buttonSave = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonSave.setObjectName("buttonSave")
        self.buttonPanel.addWidget(self.buttonSave)
        self.labelType = QtWidgets.QLabel(ConnectedDeviceDialog)
        self.labelType.setGeometry(QtCore.QRect(20, 170, 131, 16))
        self.labelType.setObjectName("labelType")
        self.dropdownType = QtWidgets.QComboBox(ConnectedDeviceDialog)
        self.dropdownType.setGeometry(QtCore.QRect(20, 190, 361, 22))
        self.dropdownType.setObjectName("dropdownType")

        self.retranslateUi(ConnectedDeviceDialog)
        QtCore.QMetaObject.connectSlotsByName(ConnectedDeviceDialog)

    def retranslateUi(self, ConnectedDeviceDialog):
        _translate = QtCore.QCoreApplication.translate
        ConnectedDeviceDialog.setWindowTitle(_translate("ConnectedDeviceDialog", "Wearable Setup"))
        self.labelName.setText(_translate("ConnectedDeviceDialog", "Name:"))
        self.labelSelectDevice.setText(_translate("ConnectedDeviceDialog", "Select Device:"))
        self.buttonRefresh.setText(_translate("ConnectedDeviceDialog", "Refresh List"))
        self.buttonCancel.setText(_translate("ConnectedDeviceDialog", "Cancel"))
        self.buttonSave.setText(_translate("ConnectedDeviceDialog", "Save"))
        self.labelType.setText(_translate("ConnectedDeviceDialog", "Device Type:"))

