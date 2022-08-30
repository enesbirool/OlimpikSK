# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/Birol/Desktop/Gym_Management_System_mxsoftware-master/assets/GUI/derece_ekle_page.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 376)
        Form.setMinimumSize(QtCore.QSize(411, 376))
        Form.setMaximumSize(QtCore.QSize(411, 376))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/olimpik.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.brans_combobox = QtWidgets.QComboBox(Form)
        self.brans_combobox.setDuplicatesEnabled(False)
        self.brans_combobox.setObjectName("brans_combobox")
        self.brans_combobox.addItem("")
        self.brans_combobox.addItem("")
        self.brans_combobox.addItem("")
        self.brans_combobox.addItem("")
        self.brans_combobox.addItem("")
        self.brans_combobox.addItem("")
        self.brans_combobox.addItem("")
        self.brans_combobox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.brans_combobox)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.turnuva_adi_edit = QtWidgets.QLineEdit(Form)
        self.turnuva_adi_edit.setObjectName("turnuva_adi_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.turnuva_adi_edit)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.turnuvail_edit = QtWidgets.QLineEdit(Form)
        self.turnuvail_edit.setObjectName("turnuvail_edit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.turnuvail_edit)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.derece_edit = QtWidgets.QLineEdit(Form)
        self.derece_edit.setObjectName("derece_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.derece_edit)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ekle_button = QtWidgets.QPushButton(Form)
        self.ekle_button.setObjectName("ekle_button")
        self.horizontalLayout.addWidget(self.ekle_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Derece Ekle"))
        self.label.setText(_translate("Form", "Branş             :"))
        self.brans_combobox.setItemText(0, _translate("Form", "Taekwondo"))
        self.brans_combobox.setItemText(1, _translate("Form", "Cimnastik"))
        self.brans_combobox.setItemText(2, _translate("Form", "KickBoks"))
        self.brans_combobox.setItemText(3, _translate("Form", "Okçuluk"))
        self.brans_combobox.setItemText(4, _translate("Form", "Judo"))
        self.brans_combobox.setItemText(5, _translate("Form", "Pilates"))
        self.brans_combobox.setItemText(6, _translate("Form", "Karate"))
        self.brans_combobox.setItemText(7, _translate("Form", "Fitness"))
        self.label_2.setText(_translate("Form", "Turnuva Adı   :"))
        self.label_3.setText(_translate("Form", "Turnuva ili      :"))
        self.label_4.setText(_translate("Form", "Derecesi         :"))
        self.ekle_button.setText(_translate("Form", "EKLE"))

import assets.py_rc.icons_rc as icons_rc
