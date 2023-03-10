# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mkt_choice.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MKTChoice(object):
    def setupUi(self, MKTChoice):
        MKTChoice.setObjectName("MKTChoice")
        MKTChoice.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MKTChoice.sizePolicy().hasHeightForWidth())
        MKTChoice.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MKTChoice)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(0, 10, 71, 31))
        self.back.setObjectName("back")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(320, 490, 191, 61))
        self.submit.setObjectName("submit")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 851, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.molec_sens_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.molec_sens_layout.setContentsMargins(300, 0, 0, 0)
        self.molec_sens_layout.setObjectName("molec_sens_layout")
        self.pv = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.pv.setObjectName("pv")
        self.molec_sens_layout.addWidget(self.pv, 1, 0, 1, 1)
        self.vt = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.vt.setObjectName("vt")
        self.molec_sens_layout.addWidget(self.vt, 2, 0, 1, 1)
        self.pt = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.pt.setObjectName("pt")
        self.molec_sens_layout.addWidget(self.pt, 0, 0, 1, 1)
        self.submit.raise_()
        self.gridLayoutWidget.raise_()
        self.back.raise_()
        MKTChoice.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MKTChoice)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MKTChoice.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MKTChoice)
        self.statusbar.setObjectName("statusbar")
        MKTChoice.setStatusBar(self.statusbar)

        self.retranslateUi(MKTChoice)
        QtCore.QMetaObject.connectSlotsByName(MKTChoice)

    def retranslateUi(self, MKTChoice):
        _translate = QtCore.QCoreApplication.translate
        MKTChoice.setWindowTitle(_translate("MKTChoice", "MKTChoice"))
        self.back.setText(_translate("MKTChoice", "??????????"))
        self.submit.setText(_translate("MKTChoice", "??????????????"))
        self.pv.setText(_translate("MKTChoice", "???????????? ???????????????? + ???????????? ???????????? (P + V)"))
        self.vt.setText(_translate("MKTChoice", "???????????? ???????????? + ???????????? ?????????????????????? (V + T)"))
        self.pt.setText(_translate("MKTChoice", "???????????? ?????????????????????? + ???????????? ???????????????? (P + T)"))
