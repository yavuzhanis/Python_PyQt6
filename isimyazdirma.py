# Form implementation generated from reading ui file 'isimyazdirma.ui'
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
        self.lblName = QtWidgets.QLabel(self.centralwidget)
        self.lblName.setGeometry(QtCore.QRect(60, 130, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lblName.setFont(font)
        self.lblName.setObjectName("lblName")
        self.lblSurName = QtWidgets.QLabel(self.centralwidget)
        self.lblSurName.setGeometry(QtCore.QRect(60, 160, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.lblSurName.setFont(font)
        self.lblSurName.setObjectName("lblSurName")
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(140, 130, 181, 21))
        self.txtName.setObjectName("txtName")
        self.txtSurname = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSurname.setGeometry(QtCore.QRect(140, 160, 181, 21))
        self.txtSurname.setObjectName("txtSurname")
        self.btnYaz = QtWidgets.QPushButton(self.centralwidget)
        self.btnYaz.setGeometry(QtCore.QRect(140, 200, 121, 41))
        self.btnYaz.setObjectName("btnYaz")
        self.lblSonuc = QtWidgets.QLabel(self.centralwidget)
        self.lblSonuc.setGeometry(QtCore.QRect(150, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblSonuc.setFont(font)
        self.lblSonuc.setText("")
        self.lblSonuc.setObjectName("lblSonuc")
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
        self.lblName.setText(_translate("MainWindow", "İsim:"))
        self.lblSurName.setText(_translate("MainWindow", "Soyisim:"))
        self.btnYaz.setText(_translate("MainWindow", "Kaydet"))
