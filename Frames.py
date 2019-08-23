# This program creates a Frame application

from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QHBoxLayout, QPushButton
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt Frame Window"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.hbox = QHBoxLayout()

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Click Me')
        button.setStyleSheet('color:white')
        button.setStyleSheet('background-color:green')

        self.frame()
        self.hbox.addWidget(button)
        self.setStyleSheet('background-color:yellow')
        self.setLayout(self.hbox)

        self.show()

    def frame(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(0.6)
        frame.setStyleSheet('background-color:blue')
        self.hbox.addWidget(frame)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
