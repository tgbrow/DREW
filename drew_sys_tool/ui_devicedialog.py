# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devicedialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeviceDialog(object):
    def setupUi(self, DeviceDialog):
        DeviceDialog.setObjectName("DeviceDialog")
        DeviceDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        DeviceDialog.resize(400, 300)
        DeviceDialog.setMinimumSize(QtCore.QSize(400, 300))
        DeviceDialog.setMaximumSize(QtCore.QSize(400, 300))
        self.labelName = QtWidgets.QLabel(DeviceDialog)
        self.labelName.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.labelName.setObjectName("labelName")
        self.labelSelectDevice = QtWidgets.QLabel(DeviceDialog)
        self.labelSelectDevice.setGeometry(QtCore.QRect(20, 100, 131, 16))
        self.labelSelectDevice.setObjectName("labelSelectDevice")
        self.dropdownDevice = QtWidgets.QComboBox(DeviceDialog)
        self.dropdownDevice.setGeometry(QtCore.QRect(20, 120, 361, 22))
        self.dropdownDevice.setObjectName("dropdownDevice")
        self.buttonRefresh = QtWidgets.QPushButton(DeviceDialog)
        self.buttonRefresh.setGeometry(QtCore.QRect(310, 150, 71, 23))
        self.buttonRefresh.setObjectName("buttonRefresh")
        self.layoutWidget = QtWidgets.QWidget(DeviceDialog)
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
        self.labelType = QtWidgets.QLabel(DeviceDialog)
        self.labelType.setGeometry(QtCore.QRect(20, 190, 131, 16))
        self.labelType.setObjectName("labelType")
        self.dropdownType = QtWidgets.QComboBox(DeviceDialog)
        self.dropdownType.setGeometry(QtCore.QRect(20, 210, 361, 22))
        self.dropdownType.setObjectName("dropdownType")
        self.inputName = QtWidgets.QLineEdit(DeviceDialog)
        self.inputName.setGeometry(QtCore.QRect(20, 40, 361, 20))
        self.inputName.setObjectName("inputName")
        self.labelInvalidName = QtWidgets.QLabel(DeviceDialog)
        self.labelInvalidName.setGeometry(QtCore.QRect(20, 60, 271, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelInvalidName.setFont(font)
        self.labelInvalidName.setStyleSheet("color: rgb(255, 0, 0);")
        self.labelInvalidName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelInvalidName.setObjectName("labelInvalidName")
        self.labelInvalidDevice = QtWidgets.QLabel(DeviceDialog)
        self.labelInvalidDevice.setGeometry(QtCore.QRect(20, 150, 271, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.labelInvalidDevice.setFont(font)
        self.labelInvalidDevice.setStyleSheet("color: rgb(255, 0, 0);")
        self.labelInvalidDevice.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelInvalidDevice.setObjectName("labelInvalidDevice")

        self.retranslateUi(DeviceDialog)
        QtCore.QMetaObject.connectSlotsByName(DeviceDialog)

    def retranslateUi(self, DeviceDialog):
        _translate = QtCore.QCoreApplication.translate
        DeviceDialog.setWindowTitle(_translate("DeviceDialog", "Connected Device Setup"))
        self.labelName.setText(_translate("DeviceDialog", "Device Name:"))
        self.labelSelectDevice.setText(_translate("DeviceDialog", "Select Device:"))
        self.buttonRefresh.setText(_translate("DeviceDialog", "Refresh List"))
        self.buttonCancel.setText(_translate("DeviceDialog", "Cancel"))
        self.buttonSave.setText(_translate("DeviceDialog", "Save"))
        self.labelType.setText(_translate("DeviceDialog", "Device Type:"))
        self.labelInvalidName.setText(_translate("DeviceDialog", "Name already in use -- cannot save."))
        self.labelInvalidDevice.setText(_translate("DeviceDialog", "Invalid device -- cannot save."))

