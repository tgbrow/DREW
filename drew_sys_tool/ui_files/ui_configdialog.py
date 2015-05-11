# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configdialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        ConfigDialog.setObjectName("ConfigDialog")
        ConfigDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ConfigDialog.resize(400, 300)
        ConfigDialog.setMinimumSize(QtCore.QSize(400, 300))
        ConfigDialog.setMaximumSize(QtCore.QSize(400, 300))
        self.labelZone = QtWidgets.QLabel(ConfigDialog)
        self.labelZone.setGeometry(QtCore.QRect(30, 50, 181, 16))
        self.labelZone.setObjectName("labelZone")
        self.labelEntryAction = QtWidgets.QLabel(ConfigDialog)
        self.labelEntryAction.setGeometry(QtCore.QRect(30, 120, 211, 16))
        self.labelEntryAction.setObjectName("labelEntryAction")
        self.dropdownEntryAction = QtWidgets.QComboBox(ConfigDialog)
        self.dropdownEntryAction.setGeometry(QtCore.QRect(30, 140, 351, 22))
        self.dropdownEntryAction.setObjectName("dropdownEntryAction")
        self.layoutWidget = QtWidgets.QWidget(ConfigDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 260, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.buttonGroup = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.buttonGroup.setContentsMargins(0, 0, 0, 0)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonCancel = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonCancel.setObjectName("buttonCancel")
        self.buttonGroup.addWidget(self.buttonCancel)
        self.buttonSave = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonSave.setObjectName("buttonSave")
        self.buttonGroup.addWidget(self.buttonSave)
        self.labelExitAction = QtWidgets.QLabel(ConfigDialog)
        self.labelExitAction.setGeometry(QtCore.QRect(30, 190, 211, 16))
        self.labelExitAction.setObjectName("labelExitAction")
        self.dropdownZone = QtWidgets.QComboBox(ConfigDialog)
        self.dropdownZone.setGeometry(QtCore.QRect(30, 70, 351, 22))
        self.dropdownZone.setObjectName("dropdownZone")
        self.dropdownExitAction = QtWidgets.QComboBox(ConfigDialog)
        self.dropdownExitAction.setGeometry(QtCore.QRect(30, 210, 351, 22))
        self.dropdownExitAction.setObjectName("dropdownExitAction")
        self.labelConfig = QtWidgets.QLabel(ConfigDialog)
        self.labelConfig.setGeometry(QtCore.QRect(20, 20, 361, 16))
        self.labelConfig.setObjectName("labelConfig")

        self.retranslateUi(ConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)

    def retranslateUi(self, ConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfigDialog.setWindowTitle(_translate("ConfigDialog", "Device Configuration"))
        self.labelZone.setText(_translate("ConfigDialog", "Zone Containing Device:"))
        self.labelEntryAction.setText(_translate("ConfigDialog", "Device Action on Zone Entry:"))
        self.buttonCancel.setText(_translate("ConfigDialog", "Cancel"))
        self.buttonSave.setText(_translate("ConfigDialog", "Save"))
        self.labelExitAction.setText(_translate("ConfigDialog", "Device Action on Zone Exit:"))
        self.labelConfig.setText(_translate("ConfigDialog", "Configuration for < DEVICE NAME >"))

