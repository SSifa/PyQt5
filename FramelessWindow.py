# This program creates a Frameless window application

from PyQt5.QtWidgets import QWidget, QApplication, QSizeGrip, QVBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt Frameless Window"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a frameless window
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        # Adding size grip for resizing the window
        vbox = QVBoxLayout()
        sizegrip = QSizeGrip(self)
        vbox.addWidget(sizegrip)

        self.setLayout(vbox)

        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
