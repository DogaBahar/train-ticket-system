import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QRadioButton,QLabel,QPushButton
from koltuk_sec import *
from ekonomi_koltuk import *
from business_koltuk import *
from odeme import *
from warning import *

nick='postgres'
password = '364218'
host = '127.0.0.1'
database = "SavT"

class Ui_Sefersec(object):
    def __init__(self, all_data):
        self.all_data = all_data

    def ok(self,saat10,saat12,saat14,saat16):
        self.cursor.execute('select * from seferler where gun = %s and guzergah_no = %s',(self.all_data['tarih'],self.all_data['guzergah']))
        seferler=self.cursor.fetchone()
        if saat10:
            sefer=seferler[2]
        elif saat12:
            sefer = seferler[3]
        elif saat14:
            sefer = seferler[4]
        else:
            sefer = seferler[5]

        print(sefer)
        self.all_data['sefer']=sefer
        self.window=QtWidgets.QDialog()
        self.ui=Ui_Dialog_koltuk_sec(self.all_data)
        self.ui.setup(self.window)
        self.window.show()

    def vt_baglan(self):
        self.baglanti = psycopg2.connect(dbname=database, host=host, password=password, user=nick)
        self.cursor = self.baglanti.cursor()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1324, 867)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(550, 160, 121, 41))
        self.label.setMouseTracking(False)
        self.label.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(640, 240, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(640, 390, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(470, 240, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 290, 101, 16))
        self.label_3.setObjectName("label_3")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(640, 340, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(640, 290, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(470, 340, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(470, 390, 101, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(550, 450, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.ok(self.radioButton.isChecked(), self.radioButton_2.isChecked(), self.radioButton_3.isChecked(), self.radioButton_4.isChecked()))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.vt_baglan()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sefer Seçimi"))
        self.radioButton.setText(_translate("Dialog", "10.00"))
        self.radioButton_2.setText(_translate("Dialog", "16.00"))
        self.label_2.setText(_translate("Dialog", "Sefer No-1"))
        self.label_3.setText(_translate("Dialog", "Sefer No-2"))
        self.radioButton_3.setText(_translate("Dialog", "14.00"))
        self.radioButton_4.setText(_translate("Dialog", "12.00"))
        self.label_4.setText(_translate("Dialog", "Sefer No-3"))
        self.label_5.setText(_translate("Dialog", "Sefer No-4"))
        self.pushButton.setText(_translate("Dialog", "Devam"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Sefersec()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())