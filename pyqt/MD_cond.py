# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MD_cond.ui',
# licensing of 'MD_cond.ui' applies.
#
# Created: Thu Nov  1 15:58:42 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MD_cond(object):
    def setupUi(self, MD_cond):
        MD_cond.setObjectName("MD_cond")
        MD_cond.resize(995, 425)
        self.centralwidget = QtWidgets.QWidget(MD_cond)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_cT = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_cT.setFont(font)
        self.checkBox_cT.setObjectName("checkBox_cT")
        self.gridLayout.addWidget(self.checkBox_cT, 2, 4, 1, 1)
        self.label_solv_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_solv_6.sizePolicy().hasHeightForWidth())
        self.label_solv_6.setSizePolicy(sizePolicy)
        self.label_solv_6.setMinimumSize(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_solv_6.setFont(font)
        self.label_solv_6.setTextFormat(QtCore.Qt.RichText)
        self.label_solv_6.setObjectName("label_solv_6")
        self.gridLayout.addWidget(self.label_solv_6, 3, 2, 1, 1)
        self.textEdit_t0 = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_t0.sizePolicy().hasHeightForWidth())
        self.textEdit_t0.setSizePolicy(sizePolicy)
        self.textEdit_t0.setMinimumSize(QtCore.QSize(10, 2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_t0.setFont(font)
        self.textEdit_t0.setObjectName("textEdit_t0")
        self.gridLayout.addWidget(self.textEdit_t0, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 2, 1, 1)
        self.checkBox_cP = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_cP.setFont(font)
        self.checkBox_cP.setObjectName("checkBox_cP")
        self.gridLayout.addWidget(self.checkBox_cP, 3, 4, 1, 1)
        self.textEdit_p0 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_p0.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_p0.sizePolicy().hasHeightForWidth())
        self.textEdit_p0.setSizePolicy(sizePolicy)
        self.textEdit_p0.setMinimumSize(QtCore.QSize(5, 2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_p0.setFont(font)
        self.textEdit_p0.setObjectName("textEdit_p0")
        self.gridLayout.addWidget(self.textEdit_p0, 3, 1, 1, 1)
        self.checkBox_IGB = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_IGB.setFont(font)
        self.checkBox_IGB.setObjectName("checkBox_IGB")
        self.gridLayout.addWidget(self.checkBox_IGB, 1, 3, 1, 1)
        self.label_solv_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_solv_3.setFont(font)
        self.label_solv_3.setTextFormat(QtCore.Qt.RichText)
        self.label_solv_3.setObjectName("label_solv_3")
        self.gridLayout.addWidget(self.label_solv_3, 2, 0, 1, 1)
        self.textEdit_ti = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_ti.sizePolicy().hasHeightForWidth())
        self.textEdit_ti.setSizePolicy(sizePolicy)
        self.textEdit_ti.setMinimumSize(QtCore.QSize(0, 2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_ti.setFont(font)
        self.textEdit_ti.setObjectName("textEdit_ti")
        self.gridLayout.addWidget(self.textEdit_ti, 2, 3, 1, 1)
        self.checkBox_cV = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_cV.setFont(font)
        self.checkBox_cV.setObjectName("checkBox_cV")
        self.gridLayout.addWidget(self.checkBox_cV, 4, 0, 1, 1)
        self.textEdit_pi = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_pi.sizePolicy().hasHeightForWidth())
        self.textEdit_pi.setSizePolicy(sizePolicy)
        self.textEdit_pi.setMinimumSize(QtCore.QSize(5, 2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_pi.setFont(font)
        self.textEdit_pi.setObjectName("textEdit_pi")
        self.gridLayout.addWidget(self.textEdit_pi, 3, 3, 1, 1)
        self.lineEdit_title = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_title.setFont(font)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.gridLayout.addWidget(self.lineEdit_title, 1, 1, 1, 1)
        self.checkBox_vacuum = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.checkBox_vacuum.setFont(font)
        self.checkBox_vacuum.setObjectName("checkBox_vacuum")
        self.gridLayout.addWidget(self.checkBox_vacuum, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_solv_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_solv_5.sizePolicy().hasHeightForWidth())
        self.label_solv_5.setSizePolicy(sizePolicy)
        self.label_solv_5.setMinimumSize(QtCore.QSize(0, 5))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_solv_5.setFont(font)
        self.label_solv_5.setTextFormat(QtCore.Qt.RichText)
        self.label_solv_5.setObjectName("label_solv_5")
        self.gridLayout.addWidget(self.label_solv_5, 3, 0, 1, 1)
        self.label_solv_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_solv_4.setFont(font)
        self.label_solv_4.setTextFormat(QtCore.Qt.RichText)
        self.label_solv_4.setObjectName("label_solv_4")
        self.gridLayout.addWidget(self.label_solv_4, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MD_cond.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MD_cond)
        self.statusbar.setObjectName("statusbar")
        MD_cond.setStatusBar(self.statusbar)

        self.retranslateUi(MD_cond)
        QtCore.QMetaObject.connectSlotsByName(MD_cond)

###############
        self.pushButton_2.clicked.connect(self.write_env)

################

    def retranslateUi(self, MD_cond):
        MD_cond.setWindowTitle(QtWidgets.QApplication.translate("MD_cond", "MainWindow", None, -1))
        self.checkBox_cT.setText(QtWidgets.QApplication.translate("MD_cond", "Constant Temperature", None, -1))
        self.label_solv_6.setText(QtWidgets.QApplication.translate("MD_cond", "<html><head/><body><p align=\"center\">Final</p><p align=\"center\">Pressure</p></body></html>", None, -1))
        self.textEdit_t0.setHtml(QtWidgets.QApplication.translate("MD_cond", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MD_cond", "Done", None, -1))
        self.checkBox_cP.setText(QtWidgets.QApplication.translate("MD_cond", "Constant Pressure", None, -1))
        self.checkBox_IGB.setText(QtWidgets.QApplication.translate("MD_cond", "IGB", None, -1))
        self.label_solv_3.setText(QtWidgets.QApplication.translate("MD_cond", "<html><head/><body><p align=\"center\">Initial </p><p align=\"center\">Temperature</p></body></html>", None, -1))
        self.checkBox_cV.setText(QtWidgets.QApplication.translate("MD_cond", "Constant Volume", None, -1))
        self.checkBox_vacuum.setText(QtWidgets.QApplication.translate("MD_cond", "Vacuum", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MD_cond", "Title", None, -1))
        self.label_solv_5.setText(QtWidgets.QApplication.translate("MD_cond", "<html><head/><body><p align=\"center\">Initial </p><p align=\"center\">Pressure</p></body></html>", None, -1))
        self.label_solv_4.setText(QtWidgets.QApplication.translate("MD_cond", "<html><head/><body><p align=\"center\">Final</p><p align=\"center\">Temperature</p></body></html>", None, -1))
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
    ############################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MD_cond = QtWidgets.QMainWindow()
    ui = Ui_MD_cond()
    ui.setupUi(MD_cond)
    MD_cond.show()
    sys.exit(app.exec_())

