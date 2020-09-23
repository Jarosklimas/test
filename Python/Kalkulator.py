import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot




class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        self.interfejs()

    def clicked(self) :
        self.label.setText("Dodawanie wynik")

    def interfejs(self):

        self.resize(400, 500)
        self.setWindowTitle("Kalkulator")
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Dodawanie")
        self.label.move(50, 50)

        self.b1 = QPushButton(self)
        
        self.b1.setText("Oblicz")
        self.b1.move(50, 70)
        self.b1.clicked.connect(self.clicked)

        label = QtWidgets.QLabel(self)
        label.setText("Odejmowanie")
        label.move(50, 150)

        label = QtWidgets.QLabel(self)
        label.setText("Mnożenie")
        label.move(50, 250)

        label = QtWidgets.QLabel(self)
        label.setText("Dzielenie")
        label.move(50, 350)

        self.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = QMainWindow()
    okno = Kalkulator()
    sys.exit(app.exec_())
