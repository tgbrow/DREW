# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pausechangedialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PauseChangeDialog(object):
    def setupUi(self, PauseChangeDialog):
        PauseChangeDialog.setObjectName("PauseChangeDialog")
        PauseChangeDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        PauseChangeDialog.resize(170, 170)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PauseChangeDialog.sizePolicy().hasHeightForWidth())
        PauseChangeDialog.setSizePolicy(sizePolicy)
        PauseChangeDialog.setMinimumSize(QtCore.QSize(170, 170))
        PauseChangeDialog.setMaximumSize(QtCore.QSize(170, 170))
        self.labelGIF = QtWidgets.QLabel(PauseChangeDialog)
        self.labelGIF.setGeometry(QtCore.QRect(20, 20, 130, 130))
        self.labelGIF.setText("")
        self.labelGIF.setObjectName("labelGIF")

        self.retranslateUi(PauseChangeDialog)
        QtCore.QMetaObject.connectSlotsByName(PauseChangeDialog)

    def retranslateUi(self, PauseChangeDialog):
        _translate = QtCore.QCoreApplication.translate
        PauseChangeDialog.setWindowTitle(_translate("PauseChangeDialog", "Dialog"))

