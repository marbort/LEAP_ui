# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Thu Nov  1 15:33:38 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from aa import Ui_aaWindow
from MD_cond import Ui_MD_cond
from MD_param import Ui_MD_param

#pippo = open("pippo.txt", "a")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_cond = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cond.sizePolicy().hasHeightForWidth())
        self.pushButton_cond.setSizePolicy(sizePolicy)
        self.pushButton_cond.setObjectName("pushButton_cond")
        self.gridLayout.addWidget(self.pushButton_cond, 0, 1, 1, 1)
        self.pushButton_param = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_param.sizePolicy().hasHeightForWidth())
        self.pushButton_param.setSizePolicy(sizePolicy)
        self.pushButton_param.setObjectName("pushButton_param")
        self.gridLayout.addWidget(self.pushButton_param, 5, 1, 1, 1)
        self.pushButton_aa = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_aa.sizePolicy().hasHeightForWidth())
        self.pushButton_aa.setSizePolicy(sizePolicy)
        self.pushButton_aa.setObjectName("pushButton_aa")
        self.gridLayout.addWidget(self.pushButton_aa, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
##################
        self.pushButton_aa.clicked.connect(self.window_aa)
        self.pushButton_cond.clicked.connect(self.window_cond)
        self.pushButton_param.clicked.connect(self.window_param)
###################
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton_cond.setText(QtWidgets.QApplication.translate("MainWindow", "MD Conditions", None, -1))
        self.pushButton_param.setText(QtWidgets.QApplication.translate("MainWindow", "MD Parameters", None, -1))
        self.pushButton_aa.setText(QtWidgets.QApplication.translate("MainWindow", "Sequence", None, -1))

##################
        self.pushButton_aa.clicked.connect(self.window_aa)
        self.pushButton_cond.clicked.connect(self.window_cond)
        self.pushButton_param.clicked.connect(self.window_param)

    def window_aa(self):
        self.wid = QtWidgets.QMainWindow()
        self.ui = Ui_aaWindow()
        self.ui.setupUi(self.wid)
        self.wid.show()

    def window_cond(self):
        self.wid2 = QtWidgets.QMainWindow()
        self.ui = Ui_MD_cond()
        self.ui.setupUi(self.wid2)
        self.wid2.show()

    def window_param(self):
        self.wid3 = QtWidgets.QMainWindow()
        self.ui = Ui_MD_param()
        self.ui.setupUi(self.wid3)
        self.wid3.show()

###################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

