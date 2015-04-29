# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    clickCount = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(140, 150, 160, 44))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.instrLabel = QtWidgets.QLabel(self.widget)
        self.instrLabel.setObjectName("instrLabel")
        self.verticalLayout.addWidget(self.instrLabel)
        self.pushMeButton = QtWidgets.QPushButton(self.widget)
        self.pushMeButton.setObjectName("pushMeButton")
        self.verticalLayout.addWidget(self.pushMeButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushMeButton.clicked.connect(self.buttonClickResponse)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.instrLabel.setText(_translate("Form", "My boy, please push this button."))
        self.pushMeButton.setText(_translate("Form", "Push Me!"))

    def buttonClickResponse(self):
        if (self.clickCount == 0):
            self.instrLabel.setText("Thank you, my son.")
        elif (self.clickCount == 1):
            self.instrLabel.setText("You can stop now.")
        elif (self.clickCount == 2):
            self.instrLabel.setText("No, seriously. Stop.")
        elif (self.clickCount == 3):
            self.instrLabel.setText("Fuck you...")
        else:
            sys.exit()
        self.clickCount += 1

