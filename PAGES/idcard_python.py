# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Birol/Desktop/Gym_Management_System_mxsoftware-master/assets/GUI/idcard.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 350)
        Form.setMinimumSize(QtCore.QSize(450, 350))
        Form.setMaximumSize(QtCore.QSize(450, 394))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.idphotolabel = QtWidgets.QLabel(Form)
        self.idphotolabel.setMinimumSize(QtCore.QSize(300, 300))
        self.idphotolabel.setText("")
        self.idphotolabel.setObjectName("idphotolabel")
        self.verticalLayout.addWidget(self.idphotolabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(-1, 50, -1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.kaydetybutton = QtWidgets.QPushButton(Form)
        self.kaydetybutton.setObjectName("kaydetybutton")
        self.horizontalLayout.addWidget(self.kaydetybutton)
        self.exitbutton = QtWidgets.QPushButton(Form)
        self.exitbutton.setObjectName("exitbutton")
        self.horizontalLayout.addWidget(self.exitbutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.kaydetybutton.setText(_translate("Form", "KAYDET"))
        self.exitbutton.setText(_translate("Form", "ÇIK"))

