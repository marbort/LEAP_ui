# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MD_cond.ui',
# licensing of 'MD_cond.ui' applies.
#
# Created: Sat Oct  6 18:32:06 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MD_cond(object):
    def setupUi(self, MD_cond):
        MD_cond.setObjectName("MD_cond")
        MD_cond.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MD_cond)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox_vacuum = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_vacuum.setGeometry(QtCore.QRect(70, 90, 162, 20))
        self.checkBox_vacuum.setObjectName("checkBox_vacuum")
        self.checkBox_IGB = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_IGB.setGeometry(QtCore.QRect(70, 110, 162, 20))
        self.checkBox_IGB.setObjectName("checkBox_IGB")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 150, 722, 182))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_solv_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_solv_3.setFont(font)
        self.label_solv_3.setTextFormat(QtCore.Qt.RichText)
        self.label_solv_3.setObjectName("label_solv_3")
        self.gridLayout.addWidget(self.label_solv_3, 0, 0, 1, 1)
        self.checkBox_cP = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_cP.setObjectName("checkBox_cP")
        self.gridLayout.addWidget(self.checkBox_cP, 1, 4, 1, 1)
        self.textEdit_pi = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_pi.setObjectName("textEdit_pi")
        self.gridLayout.addWidget(self.textEdit_pi, 1, 3, 1, 1)
        self.textEdit_ti = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_ti.setObjectName("textEdit_ti")
        self.gridLayout.addWidget(self.textEdit_ti, 0, 3, 1, 1)
        self.textEdit_p0 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_p0.setObjectName("textEdit_p0")
        self.gridLayout.addWidget(self.textEdit_p0, 1, 1, 1, 1)
        self.textEdit_t0 = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_t0.sizePolicy().hasHeightForWidth())
        self.textEdit_t0.setSizePolicy(sizePolicy)
        self.textEdit_t0.setMinimumSize(QtCore.QSize(10, 1))
        self.textEdit_t0.setObjectName("textEdit_t0")
        self.gridLayout.addWidget(self.textEdit_t0, 0, 1, 1, 1)
        self.label_solv_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_solv_5.setFont(font)
        self.label_solv_5.setTextFormat(QtCore.Qt.RichText)
        self.label_solv_5.setObjectName("label_solv_5")
        self.gridLayout.addWidget(self.label_solv_5, 1, 0, 1, 1)
        self.checkBox_cT = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_cT.setObjectName("checkBox_cT")
        self.gridLayout.addWidget(self.checkBox_cT, 0, 4, 1, 1)
        self.label_solv_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_solv_6.setFont(font)
        self.label_solv_6.setTextFormat(QtCore.Qt.RichText)
        self.label_solv_6.setObjectName("label_solv_6")
        self.gridLayout.addWidget(self.label_solv_6, 1, 2, 1, 1)
        self.label_solv_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_solv_4.setFont(font)
        self.label_solv_4.setTextFormat(QtCore.Qt.RichText)
        self.label_solv_4.setObjectName("label_solv_4")
        self.gridLayout.addWidget(self.label_solv_4, 0, 2, 1, 1)
        self.checkBox_cV = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_cV.setObjectName("checkBox_cV")
        self.gridLayout.addWidget(self.checkBox_cV, 2, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 480, 114, 32))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(210, 50, 321, 23))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_title = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.horizontalLayout.addWidget(self.lineEdit_title)
        MD_cond.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MD_cond)
        self.statusbar.setObjectName("statusbar")
        MD_cond.setStatusBar(self.statusbar)

        self.retranslateUi(MD_cond)
        QtCore.QMetaObject.connectSlotsByName(MD_cond)

###############
        self.pushButton.clicked.connect(self.write_env)

################

    def retranslateUi(self, MD_cond):
        MD_cond.setWindowTitle(QtWidgets.QApplication.translate("MD_cond", "MainWindow", None, -1))
        self.checkBox_vacuum.setText(QtWidgets.QApplication.translate("MD_cond", "Vacuum", None, -1))
        self.checkBox_IGB.setText(QtWidgets.QApplication.translate("MD_cond", "IGB", None, -1))
        self.label_solv_3.setText(QtWidgets.QApplication.translate("MD_cond", "<html><head/><body><p align=\"center\">Initial </p><p align=\"center\">Temperature</p></body></html>", None, -1))
        self.checkBox_cP.setText(QtWidgets.QApplication.translate("MD_cond", "Constant Pressure", None, -1))
        self.label_solv_5.setText(QtWidgets.QApplication.translate("MD_cond", "<html><head/><body><p align=\"center\">Initial </p><p align=\"center\">Pressure</p></body></html>", None, -1))
        self.checkBox_cT.setText(QtWidgets.QApplication.translate("MD_cond", "Constant Temperature", None, -1))
        self.label_solv_6.setText(QtWidgets.QApplication.translate("MD_cond", "<html><head/><body><p align=\"center\">Final</p><p align=\"center\">Pressure</p></body></html>", None, -1))
        self.label_solv_4.setText(QtWidgets.QApplication.translate("MD_cond", "<html><head/><body><p align=\"center\">Final</p><p align=\"center\">Temperature</p></body></html>", None, -1))
        self.checkBox_cV.setText(QtWidgets.QApplication.translate("MD_cond", "Constant Volume", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MD_cond", "Done", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MD_cond", "Title", None, -1))

########################## 
    def write_env(self):
        mdinput = open("md.in","a")
        mdinput.write(self.lineEdit_title.text() + "\n&cntrl\n")
        mdinput.write("presi = " + self.textEdit_pi.toPlainText() + "\n")
        mdinput.write("pres0 = " + self.textEdit_p0.toPlainText() + "\n")
        mdinput.write("tempi = " + self.textEdit_ti.toPlainText() + "\n")
        mdinput.write("temp0 = " + self.textEdit_t0.toPlainText() + "\n")

        if self.checkBox_IGB.isChecked():
            mdinput.write("igb=1\n")

        if self.checkBox_cV.isChecked():
            mdinput.write("ntb = 1 \n")

        if self.checkBox_cT.isChecked():
            mdinput.write("ntt = 1 \n")

        if self.checkBox_cP.isChecked():
            mdinput.write("ntp = 1 \n barostat = 2 \n")
        
        mdinput.close()
        #self.MD_cond.close()
    ############################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MD_cond = QtWidgets.QMainWindow()
    ui = Ui_MD_cond()
    ui.setupUi(MD_cond)
    MD_cond.show()
    sys.exit(app.exec_())

