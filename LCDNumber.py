# This program creates an LCDNumber application

from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber, QVBoxLayout, QPushButton
from random import randint
from PyQt5 import QtGui
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt LCDNumber"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.vbox = QVBoxLayout()
        self.lcd = QLCDNumber()
        self.button = QPushButton("Random Number Generator")

        self.InitUI()

    def InitUI(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button.clicked.connect(self.LCDHandler)
        self.lcd.setStyleSheet("background-color: green")
        self.button.setStyleSheet("background-color: cyan")

        self.vbox.addWidget(self.lcd)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)

        self.show()

    def LCDHandler(self):
        random = randint(0, 500)
        self.lcd.display(random)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
