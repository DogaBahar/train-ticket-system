import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from odeme import *
from warning import *

nick='postgres'
password = '364218'
host = '127.0.0.1'
database = "SavT"

class Ui_ekonomi(object):
    def __init__(self, all_data):
        self.all_data = all_data

    def vt_baglan(self):
        self.baglanti = psycopg2.connect(dbname=database, host=host, password=password, user=nick)
        self.cursor = self.baglanti.cursor()

    def payment(self, koltuk_no):
        self.cursor.execute('select heskodlar.risk from heskodlar, yolcu where heskodlar.hes_kod=yolcu.heskodu and'
                            " yolcu.email=%s",(self.all_data['eposta'],))
        risk = self.cursor.fetchone()
        if risk[0]==0:

            self.all_data['koltuk']=koltuk_no
            self.cursor.execute(
                f'select ekonomik.ek{koltuk_no} from seferler,sefer,ekonomik,guzergahlar where seferler.gun =%s and '
                'sefer.sefer_id=%s and sefer.ek_vagon_id = ekonomik.evagon_id and guzergahlar.guzergah_num=%s and '
                'seferler.guzergah_no=guzergahlar.guzergah_num ',
                (self.all_data['tarih'], self.all_data['sefer'], self.all_data['guzergah']))
            odeme  = self.cursor.fetchone()
            if odeme[0] == 1:
                self.window = QtWidgets.QDialog()
                self.ui = Ui_Dialog_w(1)
                self.ui.setupUi_w(self.window)
                self.window.show()

            else:
                self.window = QtWidgets.QDialog()
                self.ui = Ui_Dialog_odeme(self.all_data)
                self.ui.setupUi_odeme(self.window)
                self.window.show()
        else:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Dialog_w(2)
            self.ui.setupUi_w(self.window)
            self.window.show()

    def warning(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Dialog_w(0)
        self.ui.setupUi_w(self.window)
        self.window.show()

    def setup_ek(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1126, 871)
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(120, 220, 71, 61))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(lambda : self.payment('1'))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 310, 71, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.warning)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 220, 71, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.warning)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 310, 71, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda : self.payment('4'))
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 220, 71, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda : self.payment('5'))
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 310, 71, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.warning)
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 220, 71, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.warning)
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(390, 310, 71, 61))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda : self.payment('8'))
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(480, 220, 71, 61))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda : self.payment('9'))
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(480, 310, 71, 61))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.warning)
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(640, 220, 71, 61))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda : self.payment('11'))
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(640, 310, 71, 61))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.warning)
        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(730, 220, 71, 61))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(self.warning)
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(730, 310, 71, 61))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(lambda : self.payment('14'))
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(820, 220, 71, 61))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(lambda : self.payment('15'))
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(820, 310, 71, 61))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(self.warning)
        self.pushButton_17 = QtWidgets.QPushButton(Dialog)
        self.pushButton_17.setGeometry(QtCore.QRect(910, 220, 71, 61))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.warning)
        self.pushButton_18 = QtWidgets.QPushButton(Dialog)
        self.pushButton_18.setGeometry(QtCore.QRect(910, 310, 71, 61))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(lambda : self.payment('18'))
        self.pushButton_19 = QtWidgets.QPushButton(Dialog)
        self.pushButton_19.setGeometry(QtCore.QRect(1000, 220, 71, 61))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(lambda : self.payment('19'))
        self.pushButton_20 = QtWidgets.QPushButton(Dialog)
        self.pushButton_20.setGeometry(QtCore.QRect(1000, 310, 71, 61))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.clicked.connect(self.warning)
        self.p28 = QtWidgets.QPushButton(Dialog)
        self.p28.setGeometry(QtCore.QRect(390, 520, 71, 61))
        self.p28.setObjectName("p28")
        self.p28.clicked.connect(lambda : self.payment('28'))
        self.p1B = QtWidgets.QPushButton(Dialog)
        self.p1B.setGeometry(QtCore.QRect(640, 520, 161, 61))
        self.p1B.setObjectName("p1B")
        self.p1B.clicked.connect(self.warning)
        self.p31 = QtWidgets.QPushButton(Dialog)
        self.p31.setGeometry(QtCore.QRect(820, 430, 71, 61))
        self.p31.setObjectName("p31")
        self.p31.clicked.connect(lambda : self.payment('31'))
        self.p34 = QtWidgets.QPushButton(Dialog)
        self.p34.setGeometry(QtCore.QRect(910, 520, 71, 61))
        self.p34.setObjectName("p34")
        self.p34.clicked.connect(lambda : self.payment('34'))
        self.p33 = QtWidgets.QPushButton(Dialog)
        self.p33.setGeometry(QtCore.QRect(910, 430, 71, 61))
        self.p33.setObjectName("p33")
        self.p33.clicked.connect(self.warning)
        self.p24 = QtWidgets.QPushButton(Dialog)
        self.p24.setGeometry(QtCore.QRect(210, 520, 71, 61))
        self.p24.setObjectName("p24")
        self.p24.clicked.connect(lambda : self.payment('24'))
        self.p32 = QtWidgets.QPushButton(Dialog)
        self.p32.setGeometry(QtCore.QRect(820, 520, 71, 61))
        self.p32.setObjectName("p32")
        self.p32.clicked.connect(self.warning)
        self.p25 = QtWidgets.QPushButton(Dialog)
        self.p25.setGeometry(QtCore.QRect(300, 430, 71, 61))
        self.p25.setObjectName("p25")
        self.p25.clicked.connect(lambda : self.payment('25'))
        self.p27 = QtWidgets.QPushButton(Dialog)
        self.p27.setGeometry(QtCore.QRect(390, 430, 71, 61))
        self.p27.setObjectName("p27")
        self.p27.clicked.connect(self.warning)
        self.p36 = QtWidgets.QPushButton(Dialog)
        self.p36.setGeometry(QtCore.QRect(1000, 520, 71, 61))
        self.p36.setObjectName("p36")
        self.p36.clicked.connect(self.warning)
        self.p23 = QtWidgets.QPushButton(Dialog)
        self.p23.setGeometry(QtCore.QRect(210, 430, 71, 61))
        self.p23.setObjectName("p23")
        self.p23.clicked.connect(self.warning)
        self.p22 = QtWidgets.QPushButton(Dialog)
        self.p22.setGeometry(QtCore.QRect(120, 520, 71, 61))
        self.p22.setObjectName("p22")
        self.p22.clicked.connect(self.warning)
        self.p26 = QtWidgets.QPushButton(Dialog)
        self.p26.setGeometry(QtCore.QRect(300, 520, 71, 61))
        self.p26.setObjectName("p26")
        self.p26.clicked.connect(self.warning)
        self.p1A = QtWidgets.QPushButton(Dialog)
        self.p1A.setGeometry(QtCore.QRect(640, 430, 161, 61))
        self.p1A.setObjectName("p1A")
        self.p1A.clicked.connect(lambda : self.payment('1a'))
        self.p21 = QtWidgets.QPushButton(Dialog)
        self.p21.setGeometry(QtCore.QRect(120, 430, 71, 61))
        self.p21.setObjectName("p21")
        self.p21.clicked.connect(lambda : self.payment('21'))
        self.p29 = QtWidgets.QPushButton(Dialog)
        self.p29.setGeometry(QtCore.QRect(480, 430, 71, 61))
        self.p29.setObjectName("p29")
        self.p29.clicked.connect(lambda : self.payment('29'))
        self.p30 = QtWidgets.QPushButton(Dialog)
        self.p30.setGeometry(QtCore.QRect(480, 520, 71, 61))
        self.p30.setObjectName("p30")
        self.p30.clicked.connect(self.warning)
        self.p35 = QtWidgets.QPushButton(Dialog)
        self.p35.setGeometry(QtCore.QRect(1000, 430, 71, 61))
        self.p35.setObjectName("p35")
        self.p35.clicked.connect(lambda : self.payment('35'))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(560, 120, 161, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 180, 141, 16))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(120, 600, 431, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(640, 600, 171, 16))
        self.label_3.setObjectName("label_3")
        self.vt_baglan()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EKONOMI VAGON"))
        self.pushButton_1.setText(_translate("Dialog", "1"))
        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.pushButton_6.setText(_translate("Dialog", "6"))
        self.pushButton_7.setText(_translate("Dialog", "7"))
        self.pushButton_8.setText(_translate("Dialog", "8"))
        self.pushButton_9.setText(_translate("Dialog", "9"))
        self.pushButton_10.setText(_translate("Dialog", "10"))
        self.pushButton_11.setText(_translate("Dialog", "11"))
        self.pushButton_12.setText(_translate("Dialog", "12"))
        self.pushButton_13.setText(_translate("Dialog", "13"))
        self.pushButton_14.setText(_translate("Dialog", "14"))
        self.pushButton_15.setText(_translate("Dialog", "15"))
        self.pushButton_16.setText(_translate("Dialog", "16"))
        self.pushButton_17.setText(_translate("Dialog", "17"))
        self.pushButton_18.setText(_translate("Dialog", "19"))
        self.pushButton_19.setText(_translate("Dialog", "19"))
        self.pushButton_20.setText(_translate("Dialog", "20"))
        self.p28.setText(_translate("Dialog", "28"))
        self.p1B.setText(_translate("Dialog", "1-B"))
        self.p31.setText(_translate("Dialog", "31"))
        self.p34.setText(_translate("Dialog", "34"))
        self.p33.setText(_translate("Dialog", "33"))
        self.p24.setText(_translate("Dialog", "24"))
        self.p32.setText(_translate("Dialog", "32"))
        self.p25.setText(_translate("Dialog", "25"))
        self.p27.setText(_translate("Dialog", "27"))
        self.p36.setText(_translate("Dialog", "36"))
        self.p23.setText(_translate("Dialog", "23"))
        self.p22.setText(_translate("Dialog", "22"))
        self.p26.setText(_translate("Dialog", "26"))
        self.p1A.setText(_translate("Dialog", "1-A"))
        self.p21.setText(_translate("Dialog", "21"))
        self.p29.setText(_translate("Dialog", "29"))
        self.p30.setText(_translate("Dialog", "30"))
        self.p35.setText(_translate("Dialog", "35"))
        self.label.setText(_translate("Dialog", "Koltuk Se??imi"))
        self.label_2.setText(_translate("Dialog", "VAGON 2 ECONOMY"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">COVID-19 TEDB??RLER?? NEDEN?? ??LE TRENLER??M??ZDE YEMEK, ??KRAM, B??FE VE KAFETARYA H??ZMETLER?? VER??LMEMEKTED??R</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "YALNIZCA ENGELL?? YOLCULAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ekonomi()
    ui.setup_ek(Dialog)
    Dialog.show()
    sys.exit(app.exec_())