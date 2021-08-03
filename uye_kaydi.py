# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uye_kaydi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
nick='postgres'
password = '364218'
host = '127.0.0.1'
database = "SavT"

class Ui_UyeKaydi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 388)
        self.label_bilgi = QtWidgets.QLabel(Dialog)
        self.label_bilgi.setGeometry(QtCore.QRect(220, 40, 101, 16))
        self.label_bilgi.setObjectName("label_bilgi")
        self.label_ad = QtWidgets.QLabel(Dialog)
        self.label_ad.setGeometry(QtCore.QRect(30, 110, 31, 21))
        self.label_ad.setObjectName("label_ad")
        self.label_soyad = QtWidgets.QLabel(Dialog)
        self.label_soyad.setGeometry(QtCore.QRect(280, 110, 51, 21))
        self.label_soyad.setObjectName("label_soyad")
        self.label_eposta = QtWidgets.QLabel(Dialog)
        self.label_eposta.setGeometry(QtCore.QRect(10, 160, 55, 21))
        self.label_eposta.setObjectName("label_eposta")
        self.label_parola = QtWidgets.QLabel(Dialog)
        self.label_parola.setGeometry(QtCore.QRect(280, 160, 55, 21))
        self.label_parola.setObjectName("label_parola")
        self.label_sex = QtWidgets.QLabel(Dialog)
        self.label_sex.setGeometry(QtCore.QRect(280, 210, 61, 21))
        self.label_sex.setObjectName("label_sex")
        self.label_hes = QtWidgets.QLabel(Dialog)
        self.label_hes.setGeometry(QtCore.QRect(280, 260, 71, 21))
        self.label_hes.setObjectName("label_hes")
        self.label_tc = QtWidgets.QLabel(Dialog)
        self.label_tc.setGeometry(QtCore.QRect(20, 260, 41, 21))
        self.label_tc.setObjectName("label_tc")
        self.label_tel = QtWidgets.QLabel(Dialog)
        self.label_tel.setGeometry(QtCore.QRect(10, 210, 61, 21))
        self.label_tel.setObjectName("label_tel")
        self.label_uyari = QtWidgets.QLabel(Dialog)
        self.label_uyari.setGeometry(QtCore.QRect(150, 330, 351, 21))
        self.label_uyari.setText("")
        self.label_uyari.setObjectName("label_uyari")
        self.lineEdit_ad = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ad.setGeometry(QtCore.QRect(70, 110, 181, 22))
        self.lineEdit_ad.setText("")
        self.lineEdit_ad.setObjectName("lineEdit_ad")
        self.lineEdit_soyad = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_soyad.setGeometry(QtCore.QRect(340, 110, 161, 22))
        self.lineEdit_soyad.setText("")
        self.lineEdit_soyad.setObjectName("lineEdit_soyad")
        self.lineEdit_eposta = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_eposta.setGeometry(QtCore.QRect(70, 160, 181, 22))
        self.lineEdit_eposta.setText("")
        self.lineEdit_eposta.setObjectName("lineEdit_eposta")
        self.lineEdit_parola = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_parola.setGeometry(QtCore.QRect(342, 160, 161, 22))
        self.lineEdit_parola.setObjectName("lineEdit_parola")
        self.lineEdit_tel = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_tel.setGeometry(QtCore.QRect(70, 210, 181, 22))
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.lineEdit_tc = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_tc.setGeometry(QtCore.QRect(70, 260, 181, 22))
        self.lineEdit_tc.setObjectName("lineEdit_tc")
        self.lineEdit_hes = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_hes.setGeometry(QtCore.QRect(350, 260, 151, 22))
        self.lineEdit_hes.setObjectName("lineEdit_hes")
        self.pushButton_kayit = QtWidgets.QPushButton(Dialog)
        self.pushButton_kayit.setGeometry(QtCore.QRect(30, 330, 93, 28))
        self.pushButton_kayit.setObjectName("pushButton_kayt")
        self.combo_sex = QtWidgets.QComboBox(Dialog)
        self.combo_sex.setGeometry(QtCore.QRect(350, 210, 151, 22))
        self.combo_sex.setObjectName("combo_sex")
        self.combo_sex.addItem("KADIN")
        self.combo_sex.addItem("ERKEK")
        self.combo_sex.setCurrentText("KADIN")

        self.retranslateUi(Dialog)
        self.combo_sex.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.vt_baglan()

        self.pushButton_kayit.clicked.connect(self.kayit_ol)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "UYE KAYDI"))
        self.label_bilgi.setText(_translate("Dialog", "YENİ ÜYE KAYDI"))
        self.label_ad.setText(_translate("Dialog", "AD"))
        self.label_soyad.setText(_translate("Dialog", "SOYAD"))
        self.label_eposta.setText(_translate("Dialog", "E-POSTA"))
        self.label_parola.setText(_translate("Dialog", "PAROLA"))
        self.label_sex.setText(_translate("Dialog", "CİNSİYET"))
        self.label_hes.setText(_translate("Dialog", "HES KODU"))
        self.label_tc.setText(_translate("Dialog", "TCKN"))
        self.label_tel.setText(_translate("Dialog", "TELEFON"))
        self.pushButton_kayit.setText(_translate("Dialog", "KAYIT OL"))
        self.combo_sex.setItemText(0, _translate("Dialog", "Kadin"))
        self.combo_sex.setItemText(1, _translate("Dialog", "Erkek"))

    def vt_baglan(self):
        self.baglanti = psycopg2.connect(dbname=database, host=host, password=password, user=nick)
        self.cursor = self.baglanti.cursor()

    def kayit_ol(self):
        ad = self.lineEdit_ad.text()
        soyad = self.lineEdit_soyad.text()
        eposta = self.lineEdit_eposta.text()
        parola = self.lineEdit_parola.text()
        tel = self.lineEdit_tel.text()
        sex = self.combo_sex.currentText()
        tc = self.lineEdit_tc.text()
        hes = self.lineEdit_hes.text()

        if len(ad) == 0 or len(soyad) == 0 or len(eposta) == 0 or len(parola) == 0 or len(tel) == 0 or len(tc) == 0 or len(hes) == 0:
            self.label_uyari.setText("Tüm alanları doldurunuz!")

        elif not eposta.endswith(".com") or eposta.find("@") == -1 or eposta.count("@") != 1:
            self.label_uyari.setText("E-posta adresi kullanılamaz")

        elif len(parola) < 4 or len(parola) > 16:
            self.label_uyari.setText("Parola 4-16 uzunluğunda olmalı")

        elif len(tel) != 10 or not tel.isdigit():
            self.label_uyari.setText("Tel 10 rakamdan oluşmalı")

        elif len(tc) != 11 or not tc.isdigit():
            self.label_uyari.setText("TCKN 11 rakamdan oluşmalı")

        elif len(hes) != 4 or not hes.isdigit():
            self.label_uyari.setText("Hes kodu 4 rakamdan oluşmalı")
        
        else:
            self.cursor.execute("SELECT * FROM Yolcu WHERE email = %s", (eposta,))
            yolcu = self.cursor.fetchone()
            if yolcu != None:
                self.label_uyari.setText("E-posta adresi kullanılıyor!")
            else:
                self.cursor.execute("SELECT * FROM Yolcu WHERE tckn = %s", (tc,))
                yolcu = self.cursor.fetchone()
                if yolcu != None:
                    self.label_uyari.setText("TCKN kullanılıyor!")
                else:
                    self.cursor.execute("SELECT * FROM Yolcu WHERE heskodu = %s", (int(hes),))
                    yolcu = self.cursor.fetchone()
                    if yolcu != None:
                        self.label_uyari.setText("HES Kodu kullanılıyor!")
                    else:
                        self.cursor.execute("SELECT * FROM Yolcu WHERE telefon = %s", (tel,))
                        yolcu = self.cursor.fetchone()
                        if yolcu != None:
                            self.label_uyari.setText("Telefon numarası kullanılıyor!")
                        else:
                            self.cursor.execute("INSERT INTO Yolcu VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (ad, soyad, eposta, parola, tel, sex, tc, int(hes)))
                            self.baglanti.commit()
                            self.label_uyari.setText("Kayıt Başarılı!")
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_UyeKaydi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())