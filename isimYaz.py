import sys
from PyQt6 import QtCore, QtWidgets
from isimyazdirma import Ui_MainWindow


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnYaz.clicked.connect(self.yazdir)

    def yazdir(self):
        self.ui.lblSonuc.setText(
            self.ui.txtName.text() + " " + self.ui.txtSurname.text())


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())
