# Form implementation generated from reading ui file 'password.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hesap = QtWidgets.QLineEdit(self.centralwidget)
        self.hesap.setGeometry(QtCore.QRect(170, 20, 113, 21))
        self.hesap.setObjectName("hesap")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(170, 60, 113, 21))
        self.email.setObjectName("email")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 60, 16))
        self.label_2.setObjectName("label_2")
        self.sifrem = QtWidgets.QLineEdit(self.centralwidget)
        self.sifrem.setGeometry(QtCore.QRect(170, 100, 113, 21))
        self.sifrem.setObjectName("sifrem")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 100, 60, 16))
        self.label_3.setObjectName("label_3")
        self.btn_olustur = QtWidgets.QPushButton(self.centralwidget)
        self.btn_olustur.setGeometry(QtCore.QRect(190, 160, 113, 32))
        self.btn_olustur.setObjectName("btn_olustur")
        self.btn_yazdir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yazdir.setGeometry(QtCore.QRect(360, 160, 113, 32))
        self.btn_yazdir.setObjectName("btn_yazdir")
        self.listem = QtWidgets.QListWidget(self.centralwidget)
        self.listem.setGeometry(QtCore.QRect(490, 10, 256, 161))
        self.listem.setObjectName("listem")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 36))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Hesap"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Şifre"))
        self.btn_olustur.setText(_translate("MainWindow", "Oluştur"))
        self.btn_yazdir.setText(_translate("MainWindow", "Yazdır"))
