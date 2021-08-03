# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eposta_dogrula.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from yeni_parola import *

class Ui_EpostaDogrula(object):
    def __init__(self, eposta, kod):
        self.eposta = eposta
        self.kod = kod

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(414, 240)
        self.label_bilgi = QtWidgets.QLabel(Dialog)
        self.label_bilgi.setGeometry(QtCore.QRect(90, 40, 221, 16))
        self.label_bilgi.setObjectName("label_bilgi")
        self.lineEdit_kod = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_kod.setGeometry(QtCore.QRect(90, 90, 211, 22))
        self.lineEdit_kod.setObjectName("lineEdit_kod")
        self.pushButton_onayla = QtWidgets.QPushButton(Dialog)
        self.pushButton_onayla.setGeometry(QtCore.QRect(90, 140, 111, 28))
        self.pushButton_onayla.setObjectName("pushButton_onayla")
        self.label_uyari = QtWidgets.QLabel(Dialog)
        self.label_uyari.setGeometry(QtCore.QRect(230, 140, 170, 31))
        self.label_uyari.setText("")
        self.label_uyari.setObjectName("label_uyari")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_onayla.clicked.connect(self.kod_onayla)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EPOSTA DOGRULA"))
        self.label_bilgi.setText(_translate("Dialog", "E-posta adresinize gelen kodu giriniz"))
        self.pushButton_onayla.setText(_translate("Dialog", "Onayla"))

    def kod_onayla(self):
        kod = self.lineEdit_kod.text()
        if kod.isdigit():
            if int(kod) != self.kod:
                self.label_uyari.setText("Kod Yanlış!")
            else:
                self.parola_yenile_window = QtWidgets.QDialog()
                self.parola_yenile = Ui_YeniParola(self.eposta)
                self.parola_yenile.setupUi(self.parola_yenile_window)
                self.parola_yenile_window.show()
        else:
            self.label_uyari.setText("Kod rakamlardan oluşmalı")      

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_EpostaDogrula()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())