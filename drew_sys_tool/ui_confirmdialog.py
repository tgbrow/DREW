# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmdialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfirmDialog(object):
    def setupUi(self, ConfirmDialog):
        ConfirmDialog.setObjectName("ConfirmDialog")
        ConfirmDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ConfirmDialog.resize(380, 100)
        self.labelAreYouSure = QtWidgets.QLabel(ConfirmDialog)
        self.labelAreYouSure.setGeometry(QtCore.QRect(10, 10, 361, 21))
        self.labelAreYouSure.setObjectName("labelAreYouSure")
        self.labelWarning = QtWidgets.QLabel(ConfirmDialog)
        self.labelWarning.setGeometry(QtCore.QRect(10, 20, 361, 52))
        self.labelWarning.setStyleSheet("color: rgb(255, 0, 0)")
        self.labelWarning.setWordWrap(True)
        self.labelWarning.setObjectName("labelWarning")
        self.buttonNo = QtWidgets.QPushButton(ConfirmDialog)
        self.buttonNo.setGeometry(QtCore.QRect(211, 70, 75, 23))
        self.buttonNo.setObjectName("buttonNo")
        self.buttonYes = QtWidgets.QPushButton(ConfirmDialog)
        self.buttonYes.setGeometry(QtCore.QRect(290, 70, 75, 23))
        self.buttonYes.setObjectName("buttonYes")

        self.retranslateUi(ConfirmDialog)
        QtCore.QMetaObject.connectSlotsByName(ConfirmDialog)

    def retranslateUi(self, ConfirmDialog):
        _translate = QtCore.QCoreApplication.translate
        ConfirmDialog.setWindowTitle(_translate("ConfirmDialog", "Confim Deletion"))
        self.labelAreYouSure.setText(_translate("ConfirmDialog", "Are you sure you want to delete <type> <name>?"))
        self.labelWarning.setText(_translate("ConfirmDialog", "Note: All devices assigned to this zone will become unassigned after zone deletion. Update device-to-zone assignments in the \"System Setup\" tab."))
        self.buttonNo.setText(_translate("ConfirmDialog", "No - Cancel"))
        self.buttonYes.setText(_translate("ConfirmDialog", "Yes - Delete"))

