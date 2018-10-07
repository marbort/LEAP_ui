from PySide2 import QtCore, QtGui, QtWidgets

def parametri(self):
        mdinput = open("md.in" , "a")
        mdinput.write("dt = " + self.lineEdit_tstep.text() + "\n")
        mdinput.write("nstlim = " + self.lineEdit_dstlim.text() + "\n")
        mdinput.write("ntpr = " + self.lineEdit_ntpr.text() + "\n")
        mdinput.write("ntwr = " + self.lineEdit_ntwr.text() + "\n")
        mdinput.write("ntwx = " + self.lineEdit_ntwx.text() + "\n")
        mdinput.write("cut = " + self.lineEdit_cut.text() + "\n")

        if checkBox_SHAKE.isChecked():
            mdinput.write("ntc = 2\nntf=2\n")
        else:
            mdinput.write("ntc = 1\n")

        if checkBox.isChecked():
            mdinput.write("ntx = 1")
                

        if checkBox_2.isChecked():
            mdinput.write("imin = 0\nntx=5\n")

        if checkBox_3.isChecked():
            mdinput.write("irest = 1\n")
