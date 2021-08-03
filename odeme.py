import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
nick='postgres'
password = '364218'
host = '127.0.0.1'
database = "SavT"

class Ui_Dialog_odeme(object):

    def __init__(self, all_data):
        self.all_data = all_data

    def vt_baglan(self):
        self.baglanti = psycopg2.connect(dbname=database, host=host, password=password, user=nick)
        self.cursor = self.baglanti.cursor()

    def pay(self):
        self.cursor.execute('select ucret from guzergahlar where guzergah_num= %s'  ,(self.all_data['guzergah'],))
        tutar  = self.cursor.fetchone()
        self.ucret=tutar[0]

        if self.all_data['koltuk_tipi']=='business':
            self.ucret+=30

    def odeme_yap(self):
        kart_no=self.lineEdit.text()
        if len(kart_no)!=16:
            self.label_13.setText("Kart numarası 16 haneli olmalıdır!")
        else:
            if self.all_data['koltuk_tipi']=='ekonomi':
                tip='ek'
                uzun_tip='ekonomik'
                vagon='ek_vagon_id'
                vagon2='evagon_id'
            else:
                tip="bk"
                uzun_tip = 'business'
                vagon = 'bus_vagon_id'
                vagon2 = 'bvagon_id'

            self.label_13.setText("Ödemeniz Başarıyla Alınmıstır!")
            self.mail_gonder()
            self.cursor.execute(f"update {uzun_tip} set {tip}{self.all_data['koltuk']}=1 FROM sefer,seferler,guzergahlar where seferler.gun =%s and  sefer.sefer_id=%s "
                                f'and sefer.{vagon} = {uzun_tip}.{vagon2} and guzergahlar.guzergah_num=%s '
                                'and seferler.guzergah_no=guzergahlar.guzergah_num',(self.all_data['tarih'],self.all_data['sefer'],self.all_data['guzergah'],))

            self.baglanti.commit()

    def mail_gonder(self):
        alıcı = self.all_data['eposta']

        self.cursor.execute('select kalkis_yeri, varis_yeri from guzergahlar where guzergah_num = %s', (self.all_data['guzergah'],))
        city = self.cursor.fetchone()
        kalkis=city[0]
        varis=city[1]

        yazi = f"{self.all_data['tarih']}Tarihli {kalkis}-{varis} Güzergahında {self.all_data['koltuk_tipi']} Vagonunda {self.all_data['koltuk']} Numaralı koltuğunuz başarıyla satın alınmıştır!"

        mesaj = MIMEMultipart()
        mesaj["From"] = "savtgrupn@gmail.com"
        mesaj["To"] = alıcı
        mesaj["Subject"] = "Bilet Bilgisi"
        mesaj_govdesi = MIMEText(yazi, "plain")
        mesaj.attach(mesaj_govdesi)

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("savtgrupn@gmail.com", "savtgrupn123")
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            print("Mail Başarıyla Gönderildi....")
            mail.close()
        except:
            sys.stderr.write("Bir sorun oluştu!")
            sys.stderr.flush()

    def setupUi_odeme(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1304, 868)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(590, 210, 141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(330, 270, 181, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(330, 360, 311, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(330, 320, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(330, 400, 231, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(330, 440, 81, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(430, 440, 71, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(520, 400, 55, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 440, 121, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(690, 270, 141, 16))
        self.label_6.setObjectName("label_6")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(710, 360, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(710, 390, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(710, 420, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(710, 450, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(710, 320, 111, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 490, 170, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(860, 320, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(870, 360, 55, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(870, 390, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(870, 420, 55, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(870, 450, 55, 16))
        self.label_12.setObjectName("label_12")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(680, 300, 291, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(680, 540, 291, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.odeme_yap)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(680, 580, 200, 16))
        self.label_13.setObjectName("label_13")
        self.textBrowser.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.spinBox.raise_()
        self.spinBox_2.raise_()
        self.label_5.raise_()
        self.lineEdit_2.raise_()
        self.label_6.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton_3.raise_()
        self.radioButton_4.raise_()
        self.label_7.raise_()
        self.lineEdit_3.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.pushButton.raise_()
        self.vt_baglan()
        self.pay()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ODEME"))
        self.label.setText(_translate("Dialog", "Ödeme Yap"))
        self.label_2.setText(_translate("Dialog", "Kart Bilgileri"))
        self.label_3.setText(_translate("Dialog", "Kart Numarası"))
        self.label_4.setText(_translate("Dialog", "Son Kullanma Tarihi"))
        self.label_5.setText(_translate("Dialog", "CVV"))
        self.label_6.setText(_translate("Dialog", "Taksit Seçenekleri"))
        self.radioButton.setText(_translate("Dialog", "Tek Çekim"))
        self.radioButton_2.setText(_translate("Dialog", "2 Taksit"))
        self.radioButton_3.setText(_translate("Dialog", "3 Taksit"))
        self.radioButton_4.setText(_translate("Dialog", "4 Taksit"))
        self.label_7.setText(_translate("Dialog", "Taksit Sayısı"))
        self.lineEdit_3.setText(_translate("Dialog", "TUTAR :" + str(self.ucret) +" TL"))
        self.label_8.setText(_translate("Dialog", "Aylık Ödeme"))
        self.label_9.setText(_translate("Dialog", str(self.ucret)))
        self.label_10.setText(_translate("Dialog", str(self.ucret/2)))
        self.label_11.setText(_translate("Dialog", str(self.ucret/3)))
        self.label_12.setText(_translate("Dialog", str(self.ucret/4)))
        self.label_13.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "Ödeme Yap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_odeme()
    ui.setupUi_odeme(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

