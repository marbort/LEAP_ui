# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Fri Sep 28 16:07:36 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets 
from aa import Ui_aaWindow
from MD_cond_mod import Ui_MD_cond
from MD_param import Ui_MD_param
#import widget

pippo = open("pippo.txt", "a")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 80, 531, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_aa = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_aa.setObjectName("pushButton_aa")
        self.horizontalLayout.addWidget(self.pushButton_aa)
        self.pushButton_cond = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_cond.setObjectName("pushButton_cond")
        self.horizontalLayout.addWidget(self.pushButton_cond)
        self.pushButton_param = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_param.setObjectName("pushButton_param")
        self.horizontalLayout.addWidget(self.pushButton_param)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton_aa.setText(QtWidgets.QApplication.translate("MainWindow", "Sequence", None, -1))
        self.pushButton_cond.setText(QtWidgets.QApplication.translate("MainWindow", "MD Conditions", None, -1))
        self.pushButton_param.setText(QtWidgets.QApplication.translate("MainWindow", "MD Parameters", None, -1))
	
        self.pushButton_aa.clicked.connect(self.window_aa)
        self.pushButton_cond.clicked.connect(self.window_cond)
        self.pushButton_param.clicked.connect(self.window_param)
    #    self.pushButton.clicked.connect(self.start_sequence)
     #   self.pushButton_2.clicked.connect(self.end_sequence)
    

    #def start_sequence(self):
    #    pippo.write("seq = {")
    #
    #def end_sequence(self):
     #   pippo.write("}")
      #  pippo.close()
      
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
        
        
	
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

