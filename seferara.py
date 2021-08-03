# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seferara.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from sefer import *
import psycopg2
nick='postgres'
password = '364218'
host = '127.0.0.1'
database = "SavT"

class Ui_Seferara(object):
    def __init__(self, all_data):
        self.all_data = all_data

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(625, 444)
        self.cmb_kalkis = QtWidgets.QComboBox(Dialog)
        self.cmb_kalkis.setGeometry(QtCore.QRect(260, 50, 150, 22))
        self.cmb_kalkis.setCurrentText("")
        self.cmb_kalkis.setObjectName("cmb_kalkis")
        self.cmb_kalkis.addItem("")
        self.cmb_kalkis.addItem("")
        self.cmb_kalkis.addItem("")
        self.cmb_kalkis.addItem("")
        self.cmb_kalkis.addItem("")
        self.cmb_kalkis.addItem("")
        self.cmb_kalkis.setCurrentText("1 Ankara-Izmir")

        self.label_kalkis = QtWidgets.QLabel(Dialog)
        self.label_kalkis.setGeometry(QtCore.QRect(190, 50, 61, 21))
        self.label_kalkis.setObjectName("label_kalkis")
        self.label_tarih = QtWidgets.QLabel(Dialog)
        self.label_tarih.setGeometry(QtCore.QRect(290, 100, 71, 20))
        self.label_tarih.setObjectName("label_tarih")
        self.takvim = QtWidgets.QCalendarWidget(Dialog)
        self.takvim.setGeometry(QtCore.QRect(130, 130, 392, 236))
        self.takvim.setObjectName("takvim")
        self.pushButton_seferara = QtWidgets.QPushButton(Dialog)
        self.pushButton_seferara.setGeometry(QtCore.QRect(140, 390, 121, 28))
        self.pushButton_seferara.setObjectName("pushButton_seferara")
        self.label_uyari = QtWidgets.QLabel(Dialog)
        self.label_uyari.setGeometry(QtCore.QRect(300, 390, 300, 25))
        self.label_uyari.setObjectName("label_uyari")

        self.retranslateUi(Dialog)
        self.cmb_kalkis.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.vt_baglan()

        self.pushButton_seferara.clicked.connect(self.sefer_ara)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SEFER ARA"))
        self.cmb_kalkis.setItemText(0, _translate("Dialog", "1 Ankara-Izmir"))
        self.cmb_kalkis.setItemText(1, _translate("Dialog", "2 Izmir-Ankara"))
        self.cmb_kalkis.setItemText(2, _translate("Dialog", "3 Ankara-Kars"))
        self.cmb_kalkis.setItemText(3, _translate("Dialog", "4 Kars-Ankara"))
        self.cmb_kalkis.setItemText(4, _translate("Dialog", "5 Istanbul-Ankara"))
        self.cmb_kalkis.setItemText(5, _translate("Dialog", "6 Ankara-Istanbul"))
        self.label_kalkis.setText(_translate("Dialog", "Güzergah"))
        self.label_tarih.setText(_translate("Dialog", "Sefer Tarihi"))
        self.pushButton_seferara.setText(_translate("Dialog", "Sefer Ara"))

    def vt_baglan(self):
        self.baglanti = psycopg2.connect(dbname=database, host=host, password=password, user=nick)
        self.cursor = self.baglanti.cursor()
        
    def sefer_ara(self):
        guzergah = int(self.cmb_kalkis.currentText()[0])
        tarih = self.takvim.selectedDate().toString().split()
        tarih = f"{tarih[2]}/{self.ay_cevir(tarih[1])}/{tarih[3]}"


        self.all_data["tarih"] = tarih
        self.all_data["guzergah"] = guzergah
        self.sefersec_window = QtWidgets.QDialog()
        self.sefersec = Ui_Sefersec(self.all_data)
        self.sefersec.setupUi(self.sefersec_window)
        self.sefersec_window.show()

    def ay_cevir(self, ay):
        if ay == "Oca":
            return "01"
        elif ay == "Şub":
            return "02"
        elif ay == "Mar":
            return "03"
        elif ay == "Nis":
            return "04"
        elif ay == "May":
            return "05"
        elif ay == "Haz":
            return "06"
        elif ay == "Tem":
            return "07"
        elif ay == "Ağu":
            return "08"
        elif ay == "Eyl":
            return "09"
        elif ay == "Eki":
            return "10"
        elif ay == "Kas":
            return "11"
        else:
            return "12"                                               

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Seferara()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())