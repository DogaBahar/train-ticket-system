import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from odeme import *
from warning import *

nick='postgres'
password = '364218'
host = '127.0.0.1'
database = "SavT"
class Ui_Dialog_bus(object):

    def __init__(self, all_data):
        self.all_data = all_data

    def vt_baglan(self):
        self.baglanti = psycopg2.connect(dbname=database, host=host, password=password, user=nick)
        self.cursor = self.baglanti.cursor()

    def payment(self,koltuk_no):
        self.cursor.execute('select heskodlar.risk from heskodlar, yolcu where heskodlar.hes_kod=yolcu.heskodu and'
                            " yolcu.email=%s", (self.all_data['eposta'],))
        risk = self.cursor.fetchone()
        if risk[0] == 0:

            self.all_data['koltuk'] = koltuk_no
            self.cursor.execute(f'select business.bk{koltuk_no} from seferler,sefer,business,guzergahlar where seferler.gun =%s and '
                                'sefer.sefer_id=%s and sefer.bus_vagon_id = business.bvagon_id and guzergahlar.guzergah_num=%s and '
                                'seferler.guzergah_no=guzergahlar.guzergah_num ',( self.all_data['tarih'] , self.all_data['sefer'],self.all_data['guzergah']))
            odeme=self.cursor.fetchone()

            if odeme[0]==1:
                self.window = QtWidgets.QDialog()
                self.ui = Ui_Dialog_w(1)
                self.ui.setupUi_w(self.window)
                self.window.show()

            else:
                self.window=QtWidgets.QDialog()
                self.ui=Ui_Dialog_odeme(self.all_data)
                self.ui.setupUi_odeme(self.window)
                self.window.show()

        else:
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Dialog_w(2)
            self.ui.setupUi_w(self.window)
            self.window.show()

    def warning(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Dialog_w()
        self.ui.setupUi_w(self.window)
        self.window.show()


    def setup_bus(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1126, 873)
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(80, 260, 81, 71))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(lambda: self.payment('1'))
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 260, 81, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.payment('2'))
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 260, 81, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.payment('3'))
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 260, 81, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.payment('4'))
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(560, 260, 81, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.payment('5'))
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(660, 260, 81, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.payment('6'))
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(760, 260, 81, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda: self.payment('7'))
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(860, 260, 81, 71))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda: self.payment('8'))
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(950, 260, 81, 71))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(lambda: self.payment('9'))
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(80, 460, 81, 71))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(lambda: self.payment('10'))
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(180, 460, 81, 71))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(lambda: self.payment('11'))
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(280, 460, 81, 71))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(lambda: self.payment('12'))
        self.pushButton_13 = QtWidgets.QPushButton(Dialog)
        self.pushButton_13.setGeometry(QtCore.QRect(430, 460, 81, 71))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.clicked.connect(lambda: self.payment('13'))
        self.pushButton_14 = QtWidgets.QPushButton(Dialog)
        self.pushButton_14.setGeometry(QtCore.QRect(760, 460, 81, 71))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.clicked.connect(lambda: self.payment('14'))
        self.pushButton_15 = QtWidgets.QPushButton(Dialog)
        self.pushButton_15.setGeometry(QtCore.QRect(860, 460, 81, 71))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.clicked.connect(lambda: self.payment('15'))
        self.pushButton_16 = QtWidgets.QPushButton(Dialog)
        self.pushButton_16.setGeometry(QtCore.QRect(950, 460, 81, 71))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.clicked.connect(lambda: self.payment('16'))
        self.pushButton_1a = QtWidgets.QPushButton(Dialog)
        self.pushButton_1a.setGeometry(QtCore.QRect(560, 420, 121, 111))
        self.pushButton_1a.setObjectName("pushButton_1a")
        self.pushButton_1a.clicked.connect(lambda: self.payment('1a'))
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(700, 460, 51, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(370, 460, 51, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(370, 260, 51, 71))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(80, 340, 431, 51))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(560, 340, 471, 51))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(500, 90, 201, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(90, 190, 251, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(550, 540, 141, 16))
        self.label_3.setObjectName("label_3")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(80, 550, 431, 71))
        self.textBrowser_6.setObjectName("textBrowser_6")

        self.vt_baglan()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BUSINESS VAGON"))
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
        self.pushButton_1a.setText(_translate("Dialog", "1-A"))
        self.textBrowser_4.setHtml(_translate("Dialog",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">BAGAJ</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Dialog",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">BAGAJ</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Koltuk Seçimi"))
        self.label_2.setText(_translate("Dialog", "VAGON 1 BUSINESS"))
        self.label_3.setText(_translate("Dialog", "Yalnızca Engelli Yolcular"))
        self.textBrowser_6.setHtml(_translate("Dialog",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">COVID-19 TEDBIRLERİ NEDENİ İLE TRENLERİMİZDE YEMEK, İKRAM, BÜFE VE KAFETERYA HİZMETLERİ VERİLMEMEKTEDİR</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_bus()
    ui.setup_bus(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

