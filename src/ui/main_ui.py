# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 209)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.baseLabel = QtWidgets.QLabel(self.centralwidget)
        self.baseLabel.setObjectName("baseLabel")
        self.horizontalLayout.addWidget(self.baseLabel)
        self.baseLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.baseLineEdit.setObjectName("baseLineEdit")
        self.horizontalLayout.addWidget(self.baseLineEdit)
        self.baseToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.baseToolButton.setObjectName("baseToolButton")
        self.horizontalLayout.addWidget(self.baseToolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mapLabel = QtWidgets.QLabel(self.centralwidget)
        self.mapLabel.setObjectName("mapLabel")
        self.horizontalLayout_2.addWidget(self.mapLabel)
        self.mapLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.mapLineEdit.setObjectName("mapLineEdit")
        self.horizontalLayout_2.addWidget(self.mapLineEdit)
        self.mapToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.mapToolButton.setObjectName("mapToolButton")
        self.horizontalLayout_2.addWidget(self.mapToolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cfgLabel = QtWidgets.QLabel(self.centralwidget)
        self.cfgLabel.setObjectName("cfgLabel")
        self.horizontalLayout_3.addWidget(self.cfgLabel)
        self.cfgLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cfgLineEdit.setObjectName("cfgLineEdit")
        self.horizontalLayout_3.addWidget(self.cfgLineEdit)
        self.cfgToolButton = QtWidgets.QToolButton(self.centralwidget)
        self.cfgToolButton.setObjectName("cfgToolButton")
        self.horizontalLayout_3.addWidget(self.cfgToolButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.genButton = QtWidgets.QPushButton(self.centralwidget)
        self.genButton.setObjectName("genButton")
        self.verticalLayout_3.addWidget(self.genButton)
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setObjectName("updateButton")
        self.verticalLayout_3.addWidget(self.updateButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.baseLabel.setText(_translate("MainWindow", "Base src path"))
        self.baseToolButton.setText(_translate("MainWindow", "..."))
        self.mapLabel.setText(_translate("MainWindow", "map file"))
        self.mapToolButton.setText(_translate("MainWindow", "..."))
        self.cfgLabel.setText(_translate("MainWindow", "cfg file"))
        self.cfgToolButton.setText(_translate("MainWindow", "..."))
        self.genButton.setText(_translate("MainWindow", "Generate"))
        self.updateButton.setText(_translate("MainWindow", "Update Adr"))
