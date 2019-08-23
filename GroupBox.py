# This program creates a GroupBox application

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QHBoxLayout, QGroupBox, QVBoxLayout
from PyQt5 import QtGui
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt ButtonGroup"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.groupbox = QGroupBox('Select your favourite programming language')
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.groupBox()
        self.hbox.addWidget(self.groupbox)
        self.setLayout(self.hbox)

        self.show()

    def groupBox(self):
        rad1 = QRadioButton('Python')
        self.vbox.addWidget(rad1)

        rad2 = QRadioButton('Java')
        self.vbox.addWidget(rad2)

        rad3 = QRadioButton('C++')
        self.vbox.addWidget(rad3)

        self.groupbox.setLayout(self.vbox)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
