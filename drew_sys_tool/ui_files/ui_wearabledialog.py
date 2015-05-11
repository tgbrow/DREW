# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wearabledialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WearableDialog(object):
    def setupUi(self, WearableDialog):
        WearableDialog.setObjectName("WearableDialog")
        WearableDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        WearableDialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WearableDialog.sizePolicy().hasHeightForWidth())
        WearableDialog.setSizePolicy(sizePolicy)
        WearableDialog.setMinimumSize(QtCore.QSize(400, 300))
        WearableDialog.setMaximumSize(QtCore.QSize(400, 300))
        self.labelName = QtWidgets.QLabel(WearableDialog)
        self.labelName.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.labelName.setObjectName("labelName")
        self.labelSelectWearable = QtWidgets.QLabel(WearableDialog)
        self.labelSelectWearable.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.labelSelectWearable.setObjectName("labelSelectWearable")
        self.dropdownWearable = QtWidgets.QComboBox(WearableDialog)
        self.dropdownWearable.setGeometry(QtCore.QRect(20, 120, 361, 22))
        self.dropdownWearable.setObjectName("dropdownWearable")
        self.buttonRefresh = QtWidgets.QPushButton(WearableDialog)
        self.buttonRefresh.setGeometry(QtCore.QRect(300, 150, 81, 23))
        self.buttonRefresh.setObjectName("buttonRefresh")
        self.layoutWidget = QtWidgets.QWidget(WearableDialog)
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
        self.inputName = QtWidgets.QLineEdit(WearableDialog)
        self.inputName.setGeometry(QtCore.QRect(20, 40, 361, 20))
        self.inputName.setMaxLength(40)
        self.inputName.setObjectName("inputName")

        self.retranslateUi(WearableDialog)
        QtCore.QMetaObject.connectSlotsByName(WearableDialog)

    def retranslateUi(self, WearableDialog):
        _translate = QtCore.QCoreApplication.translate
        WearableDialog.setWindowTitle(_translate("WearableDialog", "Wearable Setup"))
        self.labelName.setText(_translate("WearableDialog", "Wearable Name:"))
        self.labelSelectWearable.setText(_translate("WearableDialog", "Select Wearable Unit:"))
        self.buttonRefresh.setText(_translate("WearableDialog", "Refresh List"))
        self.buttonCancel.setText(_translate("WearableDialog", "Cancel"))
        self.buttonSave.setText(_translate("WearableDialog", "Save"))

