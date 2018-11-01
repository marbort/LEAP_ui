# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aa.ui',
# licensing of 'aa.ui' applies.
#
# Created: Thu Nov  1 16:24:45 2018
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication

class Ui_aaWindow(object):
    def setupUi(self, aaWindow):
        aaWindow.setObjectName("aaWindow")
        aaWindow.resize(879, 531)
        self.centralwidget = QtWidgets.QWidget(aaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.textEdit_name = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textEdit_name.sizePolicy().hasHeightForWidth())
        self.textEdit_name.setSizePolicy(sizePolicy)
        self.textEdit_name.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_name.setObjectName("textEdit_name")
        self.horizontalLayout_3.addWidget(self.textEdit_name)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_params = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_params.setObjectName("checkBox_params")
        self.verticalLayout.addWidget(self.checkBox_params)
        self.checkBox_charge = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_charge.setObjectName("checkBox_charge")
        self.verticalLayout.addWidget(self.checkBox_charge)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sequence_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.sequence_text.setAcceptRichText(False)
        self.sequence_text.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.sequence_text.setObjectName("sequence_text")
        self.horizontalLayout_2.addWidget(self.sequence_text)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.listWidget_ff = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_ff.setObjectName("listWidget_ff")
        QtWidgets.QListWidgetItem(self.listWidget_ff)
        QtWidgets.QListWidgetItem(self.listWidget_ff)
        QtWidgets.QListWidgetItem(self.listWidget_ff)
        self.horizontalLayout.addWidget(self.listWidget_ff)
        self.label_solv = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_solv.setFont(font)
        self.label_solv.setTextFormat(QtCore.Qt.RichText)
        self.label_solv.setObjectName("label_solv")
        self.horizontalLayout.addWidget(self.label_solv)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        QtWidgets.QListWidgetItem(self.listWidget)
        QtWidgets.QListWidgetItem(self.listWidget)
        QtWidgets.QListWidgetItem(self.listWidget)
        QtWidgets.QListWidgetItem(self.listWidget)
        self.horizontalLayout.addWidget(self.listWidget)
        self.label_solv_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_solv_2.setFont(font)
        self.label_solv_2.setTextFormat(QtCore.Qt.RichText)
        self.label_solv_2.setObjectName("label_solv_2")
        self.horizontalLayout.addWidget(self.label_solv_2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.push_done = QtWidgets.QPushButton(self.centralwidget)
        self.push_done.setObjectName("push_done")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.push_done)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.GLU = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GLU.sizePolicy().hasHeightForWidth())
        self.GLU.setSizePolicy(sizePolicy)
        self.GLU.setObjectName("GLU")
        self.gridLayout.addWidget(self.GLU, 1, 1, 1, 1)
        self.GLN = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GLN.sizePolicy().hasHeightForWidth())
        self.GLN.setSizePolicy(sizePolicy)
        self.GLN.setObjectName("GLN")
        self.gridLayout.addWidget(self.GLN, 1, 2, 1, 1)
        self.ALA = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ALA.sizePolicy().hasHeightForWidth())
        self.ALA.setSizePolicy(sizePolicy)
        self.ALA.setObjectName("ALA")
        self.gridLayout.addWidget(self.ALA, 0, 0, 1, 1)
        self.ASP = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ASP.sizePolicy().hasHeightForWidth())
        self.ASP.setSizePolicy(sizePolicy)
        self.ASP.setObjectName("ASP")
        self.gridLayout.addWidget(self.ASP, 0, 3, 1, 1)
        self.HIS = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HIS.sizePolicy().hasHeightForWidth())
        self.HIS.setSizePolicy(sizePolicy)
        self.HIS.setObjectName("HIS")
        self.gridLayout.addWidget(self.HIS, 2, 0, 1, 1)
        self.pushButton_17SER = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17SER.sizePolicy().hasHeightForWidth())
        self.pushButton_17SER.setSizePolicy(sizePolicy)
        self.pushButton_17SER.setObjectName("pushButton_17SER")
        self.gridLayout.addWidget(self.pushButton_17SER, 3, 3, 1, 1)
        self.MET = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MET.sizePolicy().hasHeightForWidth())
        self.MET.setSizePolicy(sizePolicy)
        self.MET.setObjectName("MET")
        self.gridLayout.addWidget(self.MET, 3, 0, 1, 1)
        self.LYS = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LYS.sizePolicy().hasHeightForWidth())
        self.LYS.setSizePolicy(sizePolicy)
        self.LYS.setObjectName("LYS")
        self.gridLayout.addWidget(self.LYS, 2, 3, 1, 1)
        self.TRP = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TRP.sizePolicy().hasHeightForWidth())
        self.TRP.setSizePolicy(sizePolicy)
        self.TRP.setObjectName("TRP")
        self.gridLayout.addWidget(self.TRP, 4, 1, 1, 1)
        self.ILE = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ILE.sizePolicy().hasHeightForWidth())
        self.ILE.setSizePolicy(sizePolicy)
        self.ILE.setObjectName("ILE")
        self.gridLayout.addWidget(self.ILE, 2, 1, 1, 1)
        self.LEU = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LEU.sizePolicy().hasHeightForWidth())
        self.LEU.setSizePolicy(sizePolicy)
        self.LEU.setObjectName("LEU")
        self.gridLayout.addWidget(self.LEU, 2, 2, 1, 1)
        self.VAL = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VAL.sizePolicy().hasHeightForWidth())
        self.VAL.setSizePolicy(sizePolicy)
        self.VAL.setObjectName("VAL")
        self.gridLayout.addWidget(self.VAL, 4, 3, 1, 1)
        self.TYR = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TYR.sizePolicy().hasHeightForWidth())
        self.TYR.setSizePolicy(sizePolicy)
        self.TYR.setObjectName("TYR")
        self.gridLayout.addWidget(self.TYR, 4, 2, 1, 1)
        self.PRO = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PRO.sizePolicy().hasHeightForWidth())
        self.PRO.setSizePolicy(sizePolicy)
        self.PRO.setObjectName("PRO")
        self.gridLayout.addWidget(self.PRO, 3, 2, 1, 1)
        self.GLY = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GLY.sizePolicy().hasHeightForWidth())
        self.GLY.setSizePolicy(sizePolicy)
        self.GLY.setObjectName("GLY")
        self.gridLayout.addWidget(self.GLY, 1, 3, 1, 1)
        self.CYS = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CYS.sizePolicy().hasHeightForWidth())
        self.CYS.setSizePolicy(sizePolicy)
        self.CYS.setObjectName("CYS")
        self.gridLayout.addWidget(self.CYS, 1, 0, 1, 1)
        self.ARG = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ARG.sizePolicy().hasHeightForWidth())
        self.ARG.setSizePolicy(sizePolicy)
        self.ARG.setObjectName("ARG")
        self.gridLayout.addWidget(self.ARG, 0, 1, 1, 1)
        self.PHE = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PHE.sizePolicy().hasHeightForWidth())
        self.PHE.setSizePolicy(sizePolicy)
        self.PHE.setObjectName("PHE")
        self.gridLayout.addWidget(self.PHE, 3, 1, 1, 1)
        self.ASN = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ASN.sizePolicy().hasHeightForWidth())
        self.ASN.setSizePolicy(sizePolicy)
        self.ASN.setObjectName("ASN")
        self.gridLayout.addWidget(self.ASN, 0, 2, 1, 1)
        self.THR = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.THR.sizePolicy().hasHeightForWidth())
        self.THR.setSizePolicy(sizePolicy)
        self.THR.setObjectName("THR")
        self.gridLayout.addWidget(self.THR, 4, 0, 1, 1)
        self.ACE = QtWidgets.QPushButton(self.centralwidget)
        self.ACE.setObjectName("ACE")
        self.gridLayout.addWidget(self.ACE, 5, 1, 1, 1)
        self.NME = QtWidgets.QPushButton(self.centralwidget)
        self.NME.setObjectName("NME")
        self.gridLayout.addWidget(self.NME, 5, 2, 1, 1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.gridLayout)
        aaWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(aaWindow)
        self.statusbar.setObjectName("statusbar")
        aaWindow.setStatusBar(self.statusbar)
        self.actionNew_Structure = QtWidgets.QAction(aaWindow)
        self.actionNew_Structure.setObjectName("actionNew_Structure")

        self.retranslateUi(aaWindow)
        QtCore.QMetaObject.connectSlotsByName(aaWindow)

        #############################
        self.sequence =[]

        self.push_done.clicked.connect(self.write_file)

        self.ALA.clicked.connect(self.add_ALA)
        self.ARG.clicked.connect(self.add_ARG)
        self.ASN.clicked.connect(self.add_ASN)
        self.ASP.clicked.connect(self.add_ASP)
        self.CYS.clicked.connect(self.add_CYS)
        self.GLU.clicked.connect(self.add_GLU)
        self.GLN.clicked.connect(self.add_GLN)
        self.GLY.clicked.connect(self.add_GLY)
        self.HIS.clicked.connect(self.add_HIS)
        self.ILE.clicked.connect(self.add_ILE)
        self.LEU.clicked.connect(self.add_LEU)
        self.LYS.clicked.connect(self.add_LYS)
        self.MET.clicked.connect(self.add_MET)
        self.PHE.clicked.connect(self.add_PHE)
        self.PRO.clicked.connect(self.add_PRO)
        self.pushButton_17SER.clicked.connect(self.add_SER)
        self.THR.clicked.connect(self.add_THR)
        self.TRP.clicked.connect(self.add_TRP)
        self.TYR.clicked.connect(self.add_TYR)
        self.VAL.clicked.connect(self.add_VAL)

        self.ACE.clicked.connect(self.add_ACE)
        self.NME.clicked.connect(self.add_NME)

        

    
        
        
    def add_ALA(self):
        self.sequence.append("ALA ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

 
 

    def add_ARG(self):
        self.sequence.append("ARG ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()



    def add_ASN(self):
        self.sequence.append("ASN ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_ASP(self):
        self.sequence.append("ASP ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_CYS(self):
        self.sequence.append("CYS ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_GLU(self):
        self.sequence.append("GLU ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_GLN(self):
        self.sequence.append("GLN ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_GLY(self):
        self.sequence.append("GLY ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_HIS(self):
        self.sequence.append("HIS ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_ILE(self):
        self.sequence.append("ILE ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_LEU(self):
        self.sequence.append("LEU ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_LYS(self):
        self.sequence.append("LYS ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_MET(self):
        self.sequence.append("MET ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_PHE(self):
        self.sequence.append("PHE ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_PRO(self):
        self.sequence.append("PRO ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_SER(self):
        self.sequence.append("SER ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_THR(self):
        self.sequence.append("THR ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_TRP(self):
        self.sequence.append("TRP ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_TYR(self):
        self.sequence.append("TYR ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_VAL(self):
        self.sequence.append("VAL ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_ACE(self):
        self.sequence.append("ACE ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()

    def add_NME(self):
        self.sequence.append("NME ")
        self.sequence_text.setText(''.join(self.sequence))
        self.sequence_text.repaint()
###############################

    def retranslateUi(self, aaWindow):
        aaWindow.setWindowTitle(QtWidgets.QApplication.translate("aaWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("aaWindow", "Structure Name", None, -1))
        self.checkBox_params.setText(QtWidgets.QApplication.translate("aaWindow", "Check for missing params", None, -1))
        self.checkBox_charge.setText(QtWidgets.QApplication.translate("aaWindow", "Print total charge", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("aaWindow", "Sequence", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("aaWindow", "Force Field", None, -1))
        __sortingEnabled = self.listWidget_ff.isSortingEnabled()
        self.listWidget_ff.setSortingEnabled(False)
        self.listWidget_ff.item(0).setText(QtWidgets.QApplication.translate("aaWindow", "ff14SB", None, -1))
        self.listWidget_ff.item(1).setText(QtWidgets.QApplication.translate("aaWindow", "gaff", None, -1))
        self.listWidget_ff.item(2).setText(QtWidgets.QApplication.translate("aaWindow", "gaff2", None, -1))
        self.listWidget_ff.setSortingEnabled(__sortingEnabled)
        self.label_solv.setText(QtWidgets.QApplication.translate("aaWindow", "Solvent", None, -1))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtWidgets.QApplication.translate("aaWindow", "Vacuum", None, -1))
        self.listWidget.item(1).setText(QtWidgets.QApplication.translate("aaWindow", "TIP3P Water", None, -1))
        self.listWidget.item(2).setText(QtWidgets.QApplication.translate("aaWindow", "TIP4P Water", None, -1))
        self.listWidget.item(3).setText(QtWidgets.QApplication.translate("aaWindow", "OPLS  Water", None, -1))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_solv_2.setText(QtWidgets.QApplication.translate("aaWindow", "Buffer", None, -1))
        self.push_done.setText(QtWidgets.QApplication.translate("aaWindow", "Done", None, -1))
        self.GLU.setText(QtWidgets.QApplication.translate("aaWindow", "GLU", None, -1))
        self.GLN.setText(QtWidgets.QApplication.translate("aaWindow", "GLN", None, -1))
        self.ALA.setText(QtWidgets.QApplication.translate("aaWindow", "ALA", None, -1))
        self.ASP.setText(QtWidgets.QApplication.translate("aaWindow", "ASP", None, -1))
        self.HIS.setText(QtWidgets.QApplication.translate("aaWindow", "HIS", None, -1))
        self.pushButton_17SER.setText(QtWidgets.QApplication.translate("aaWindow", "SER", None, -1))
        self.MET.setText(QtWidgets.QApplication.translate("aaWindow", "MET", None, -1))
        self.LYS.setText(QtWidgets.QApplication.translate("aaWindow", "LYS", None, -1))
        self.TRP.setText(QtWidgets.QApplication.translate("aaWindow", "TRP", None, -1))
        self.ILE.setText(QtWidgets.QApplication.translate("aaWindow", "ILE", None, -1))
        self.LEU.setText(QtWidgets.QApplication.translate("aaWindow", "LEU", None, -1))
        self.VAL.setText(QtWidgets.QApplication.translate("aaWindow", "VAL", None, -1))
        self.TYR.setText(QtWidgets.QApplication.translate("aaWindow", "TYR", None, -1))
        self.PRO.setText(QtWidgets.QApplication.translate("aaWindow", "PRO", None, -1))
        self.GLY.setText(QtWidgets.QApplication.translate("aaWindow", "GLY", None, -1))
        self.CYS.setText(QtWidgets.QApplication.translate("aaWindow", "CYS", None, -1))
        self.ARG.setText(QtWidgets.QApplication.translate("aaWindow", "ARG", None, -1))
        self.PHE.setText(QtWidgets.QApplication.translate("aaWindow", "PHE", None, -1))
        self.ASN.setText(QtWidgets.QApplication.translate("aaWindow", "ASN", None, -1))
        self.THR.setText(QtWidgets.QApplication.translate("aaWindow", "THR", None, -1))
        self.ACE.setText(QtWidgets.QApplication.translate("aaWindow", "ACE", None, -1))
        self.NME.setText(QtWidgets.QApplication.translate("aaWindow", "NME", None, -1))
        self.actionNew_Structure.setText(QtWidgets.QApplication.translate("aaWindow", "New Structure", None, -1))

        ########################################   
    def write_file(self):
        self.finalseq = ''.join(self.sequence)
        pippo = open(self.textEdit_name.toPlainText() + ".leap" , "a")
        if self.listWidget_ff.item(0).isSelected():
            pippo.write("source leaprc.protein.ff14SB\n")

        if self.listWidget_ff.item(1).isSelected():
            pippo.write("source leaprc.gaff\n")

        if self.listWidget_ff.item(2).isSelected():
            pippo.write("source leaprc.gaff2\n")

        pippo.write( self.textEdit_name.toPlainText() + " = sequence { " + self.finalseq + "} \n")

        if self.listWidget.item(0).isSelected():
            print("no solvation")
        elif self.listWidget.item(1).isSelected():
            pippo.write("source leaprc.water.tip3p \n")
            pippo.write("solvatebox " + self.textEdit_name.toPlainText() + " " + self.listWidget.currentItem().text() + " " 
             + self.textEdit.toPlainText() + "\n")
        elif self.listWidget.item(2).isSelected():
            pippo.write("source leaprc.water.tip4pew \n")
            pippo.write("solvatebox " + self.textEdit_name.toPlainText() + " " + self.listWidget.currentItem().text() + " " 
             + self.textEdit.toPlainText() + "\n")
        elif self.listWidget.item(3).isSelected():
            pippo.write("source leaprc.water.opc \n")
            pippo.write("solvatebox " + self.textEdit_name.toPlainText() + " " + self.listWidget.currentItem().text() + " " 
             + self.textEdit.toPlainText() + "\n")

        if self.checkBox_charge.isChecked():
            pippo.write("charge " + self.textEdit_name.toPlainText() + "\n")

        if self.checkBox_params.isChecked():
            pippo.write("check " + self.textEdit_name.toPlainText() + "\n")

        pippo.write("saveamberparm " + self.textEdit_name.toPlainText() + " " + self.textEdit_name.toPlainText() + ".parm7 " 
            + self.textEdit_name.toPlainText() + ".inpcrd\n")


        pippo.close()
###########################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aaWindow = QtWidgets.QMainWindow()
    ui = Ui_aaWindow()
    ui.setupUi(aaWindow)
    aaWindow.show()
    sys.exit(app.exec_())

