
from PyQt5 import QtCore, QtGui, QtWidgets
from eposta_dogrula import *
from uye_kaydi import *
from seferara import *
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import psycopg2

nick='postgres'
password = '364218'
host = '127.0.0.1'
database = "SavT"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 344)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_baslik = QtWidgets.QLabel(self.centralwidget)
        self.label_baslik.setGeometry(QtCore.QRect(230, 50, 71, 16))
        self.label_baslik.setObjectName("label_baslik")
        self.label_eposta = QtWidgets.QLabel(self.centralwidget)
        self.label_eposta.setGeometry(QtCore.QRect(130, 90, 51, 20))
        self.label_eposta.setObjectName("label_eposta")
        self.label_parola = QtWidgets.QLabel(self.centralwidget)
        self.label_parola.setGeometry(QtCore.QRect(130, 130, 41, 16))
        self.label_parola.setObjectName("label_parola")
        self.lineEdit_eposta = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_eposta.setGeometry(QtCore.QRect(190, 90, 211, 22))
        self.lineEdit_eposta.setText("")
        self.lineEdit_eposta.setObjectName("lineEdit_eposta")
        self.lineEdit_parola = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_parola.setGeometry(QtCore.QRect(190, 130, 211, 22))
        self.lineEdit_parola.setObjectName("lineEdit_parola")
        self.lineEdit_parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_yeniparola = QtWidgets.QLabel(self.centralwidget)
        self.label_yeniparola.setGeometry(QtCore.QRect(130, 170, 131, 20))
        self.label_yeniparola.setObjectName("label_yeniparola")
        self.label_uyeol = QtWidgets.QLabel(self.centralwidget)
        self.label_uyeol.setGeometry(QtCore.QRect(130, 210, 101, 20))
        self.label_uyeol.setObjectName("label_uyeol")
        self.pushButton_yeniparola = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_yeniparola.setGeometry(QtCore.QRect(270, 170, 131, 28))
        self.pushButton_yeniparola.setObjectName("pushButton_yeniparola")
        self.pushButton_uyeol = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_uyeol.setGeometry(QtCore.QRect(270, 210, 131, 28))
        self.pushButton_uyeol.setObjectName("pushButton_uyeol")
        self.pushButton_girisyap = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_girisyap.setGeometry(QtCore.QRect(130, 260, 93, 28))
        self.pushButton_girisyap.setObjectName("pushButton_girisyap")
        self.label_uyari = QtWidgets.QLabel(self.centralwidget)
        self.label_uyari.setGeometry(QtCore.QRect(240, 250, 290, 41))
        self.label_uyari.setText("")
        self.label_uyari.setObjectName("label_uyari")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.vt_baglan()

        self.pushButton_yeniparola.clicked.connect(self.parola_yenile)
        self.pushButton_uyeol.clicked.connect(self.yeni_uyelik)
        self.pushButton_girisyap.clicked.connect(self.girisyap)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UYE GIRISI"))
        self.label_baslik.setText(_translate("MainWindow", "ÜYE GİRİŞİ"))
        self.label_eposta.setText(_translate("MainWindow", "e - posta"))
        self.label_parola.setText(_translate("MainWindow", "Parola"))
        self.label_yeniparola.setText(_translate("MainWindow", "Parolanı mı unuttun?"))
        self.label_uyeol.setText(_translate("MainWindow", "Üye değil misin?"))
        self.pushButton_yeniparola.setText(_translate("MainWindow", "Yeni Parola"))
        self.pushButton_uyeol.setText(_translate("MainWindow", "Üye Ol"))
        self.pushButton_girisyap.setText(_translate("MainWindow", "Giriş Yap"))

    def vt_baglan(self):
        self.baglanti = psycopg2.connect(dbname=database, host=host, password=password, user=nick)
        self.cursor = self.baglanti.cursor()

    def parola_yenile(self):
        eposta = self.lineEdit_eposta.text() 
        self.cursor.execute("SELECT * FROM Yolcu WHERE email = %s", (eposta,))
        kullanıcı = self.cursor.fetchone()
        if kullanıcı == None:
            self.label_uyari.setText("Parola yenilemek için E-posta adresinizi giriniz!")
        else:
            self.mail_gonder()
            self.eposta_dogrula_window = QtWidgets.QDialog()
            self.eposta_dogrula = Ui_EpostaDogrula(eposta, self.kod)
            self.eposta_dogrula.setupUi(self.eposta_dogrula_window)
            self.eposta_dogrula_window.show()

    def yeni_uyelik(self):
        self.uye_kaydı_window = QtWidgets.QDialog()
        self.uye_kaydı = Ui_UyeKaydi()
        self.uye_kaydı.setupUi(self.uye_kaydı_window)
        self.uye_kaydı_window.show()

    def girisyap(self):
        eposta = self.lineEdit_eposta.text()
        parola = self.lineEdit_parola.text()
        self.cursor.execute("SELECT * FROM Yolcu WHERE email = %s", (eposta,))
        kullanıcı = self.cursor.fetchone()
        if kullanıcı == None:
            self.label_uyari.setText("E-posta adresi yanlış!")
        elif kullanıcı[3] != parola:
            self.label_uyari.setText("Parola yanlış!")
        else:
            all_data = {"eposta": eposta}
            self.seferara_window = QtWidgets.QDialog()
            self.seferara = Ui_Seferara(all_data)
            self.seferara.setupUi(self.seferara_window)
            self.seferara_window.show()

    def mail_gonder(self):
        alıcı = self.lineEdit_eposta.text()
        self.kod = random.randint(100000, 999999)
        yazi = f"Parola yenileme kodunuz: {self.kod}"

        mesaj = MIMEMultipart()
        mesaj["From"] = "savtgrupn@gmail.com"
        mesaj["To"] = alıcı
        mesaj["Subject"] = "Parola Yenileme İsteği"
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())