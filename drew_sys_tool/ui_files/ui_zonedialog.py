# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zonedialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ZoneDialog(object):
    def setupUi(self, ZoneDialog):
        ZoneDialog.setObjectName("ZoneDialog")
        ZoneDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ZoneDialog.resize(400, 300)
        ZoneDialog.setMinimumSize(QtCore.QSize(400, 300))
        ZoneDialog.setMaximumSize(QtCore.QSize(400, 300))
        self.labelName = QtWidgets.QLabel(ZoneDialog)
        self.labelName.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.labelName.setObjectName("labelName")
        self.labelSelectModule = QtWidgets.QLabel(ZoneDialog)
        self.labelSelectModule.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.labelSelectModule.setObjectName("labelSelectModule")
        self.dropdownModule = QtWidgets.QComboBox(ZoneDialog)
        self.dropdownModule.setGeometry(QtCore.QRect(20, 120, 361, 22))
        self.dropdownModule.setObjectName("dropdownModule")
        self.buttonRefresh = QtWidgets.QPushButton(ZoneDialog)
        self.buttonRefresh.setGeometry(QtCore.QRect(300, 150, 81, 23))
        self.buttonRefresh.setObjectName("buttonRefresh")
        self.layoutWidget = QtWidgets.QWidget(ZoneDialog)
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
        self.labelThreshold = QtWidgets.QLabel(ZoneDialog)
        self.labelThreshold.setGeometry(QtCore.QRect(20, 190, 191, 16))
        self.labelThreshold.setObjectName("labelThreshold")
        self.sliderThreshold = QtWidgets.QSlider(ZoneDialog)
        self.sliderThreshold.setGeometry(QtCore.QRect(20, 210, 311, 22))
        self.sliderThreshold.setOrientation(QtCore.Qt.Horizontal)
        self.sliderThreshold.setObjectName("sliderThreshold")
        self.spinnerThreshold = QtWidgets.QSpinBox(ZoneDialog)
        self.spinnerThreshold.setGeometry(QtCore.QRect(340, 210, 42, 22))
        self.spinnerThreshold.setObjectName("spinnerThreshold")
        self.inputName = QtWidgets.QLineEdit(ZoneDialog)
        self.inputName.setGeometry(QtCore.QRect(20, 40, 361, 20))
        self.inputName.setObjectName("inputName")

        self.retranslateUi(ZoneDialog)
        QtCore.QMetaObject.connectSlotsByName(ZoneDialog)

    def retranslateUi(self, ZoneDialog):
        _translate = QtCore.QCoreApplication.translate
        ZoneDialog.setWindowTitle(_translate("ZoneDialog", "Zone Setup"))
        self.labelName.setText(_translate("ZoneDialog", "Zone Name:"))
        self.labelSelectModule.setText(_translate("ZoneDialog", "Select Zone Module:"))
        self.buttonRefresh.setText(_translate("ZoneDialog", "Refresh List"))
        self.buttonCancel.setText(_translate("ZoneDialog", "Cancel"))
        self.buttonSave.setText(_translate("ZoneDialog", "Save"))
        self.labelThreshold.setText(_translate("ZoneDialog", "Zone Threshold (module to wearable):"))
