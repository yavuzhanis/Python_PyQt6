import sys
import typing
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QWidget
from password import Ui_MainWindow
import random
import string
import sqlite3

baglanti = sqlite3.connect('sifrelerim.db')
cursor = baglanti.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS sifreler(hesap TEXT , email TEXT , sifre TEXT)")


class Window (QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_olustur.clicked.connect(self.olustur)
        self.ui.btn_yazdir.clicked.connect(self.yazdir)

    def olustur(self):
        harfler = string.ascii_lowercase+string.digits+string.ascii_uppercase
        sifrem = ''.join(random.choice(harfler) for i in range(10))
        hesabim = self.ui.hesap.text()
        emailim = self.ui.email.text()
        self.ui.sifrem.setText(sifrem)
        cursor.execute("insert into sifreler values(?,?,?)",
                       (hesabim, emailim, sifrem))
        baglanti.commit()

    def yazdir(self):
        cursor.execute('select * from sifreler')
        liste = cursor.fetchall()
        for i in liste:
            self.ui.listem.addItems(["Hesap Bilgileri"])
            self.ui.listem.addItems(i)


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())
