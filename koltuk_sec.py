import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from ekonomi_koltuk import *
from business_koltuk import *
from odeme import *

class Ui_Dialog_koltuk_sec(object):

    def __init__(self, all_data):
        self.all_data = all_data

    def ok(self,business,ekonomi):
        if business:
            self.all_data['koltuk_tipi']='business'
            self.window1 = QtWidgets.QDialog()
            self.ui = Ui_Dialog_bus(self.all_data)
            self.ui.setup_bus(self.window1)
            self.window1.show()
        else:
            self.all_data['koltuk_tipi'] = 'ekonomi'
            self.window=QtWidgets.QDialog()
            self.ui=Ui_ekonomi(self.all_data)
            self.ui.setup_ek(self.window)
            self.window.show()



    def setup(self, Dialog):
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(470, 240, 101, 16))
        self.label_2.setObjectName("label_2")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(640, 290, 95, 20))
        self.radioButton_2.setObjectName("radioButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(470, 290, 101, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(530, 360, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.ok(self.radioButton.isChecked(), self.radioButton_2.isChecked()))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "VAGON SECIMI"))
        self.label.setText(_translate("Dialog", "Koltuk Tipi Seçimi"))
        self.radioButton.setText(_translate("Dialog", ""))
        self.radioButton_2.setText(_translate("Dialog", ""))
        self.label_2.setText(_translate("Dialog", "Business Vagon"))
        self.label_3.setText(_translate("Dialog", "Ekonomi Vagon"))
        self.pushButton.setText(_translate("Dialog", "Devam"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_koltuk_sec()
    ui.setup(Dialog)
    Dialog.show()
    sys.exit(app.exec_())