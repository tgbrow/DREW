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
        PauseChangeDialog.resize(200, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PauseChangeDialog.sizePolicy().hasHeightForWidth())
        PauseChangeDialog.setSizePolicy(sizePolicy)
        PauseChangeDialog.setMinimumSize(QtCore.QSize(200, 200))
        PauseChangeDialog.setMaximumSize(QtCore.QSize(200, 200))
        self.labelGIF = QtWidgets.QLabel(PauseChangeDialog)
        self.labelGIF.setGeometry(QtCore.QRect(30, 30, 140, 140))
        self.labelGIF.setText("")
        self.labelGIF.setObjectName("labelGIF")

        self.retranslateUi(PauseChangeDialog)
        QtCore.QMetaObject.connectSlotsByName(PauseChangeDialog)

    def retranslateUi(self, PauseChangeDialog):
        _translate = QtCore.QCoreApplication.translate
        PauseChangeDialog.setWindowTitle(_translate("PauseChangeDialog", "Dialog"))

