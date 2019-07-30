# Layout Management - GridLayout

from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5 import QtGui
import sys

class Window(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 GridLayout"
        self.top = 50
        self.left = 50
        self.width = 400
        self.height = 300
        self.icon = "home.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("What is your favorite Programming Language?")
        gridLayout = QGridLayout()

        button = QPushButton("Python", self)
        button.move(50, 50)
        button.setToolTip("Python")
        gridLayout.addWidget(button, 0, 0)

        button1 = QPushButton("Java", self)
        button1.move(50, 50)
        button1.setToolTip("Java")
        gridLayout.addWidget(button1, 0, 1)

        button2 = QPushButton("C++", self)
        button2.move(50, 50)
        button2.setToolTip("C++")
        gridLayout.addWidget(button2, 1, 0)

        button3 = QPushButton("C#", self)
        button3.move(50, 50)
        button3.setToolTip("C#")
        gridLayout.addWidget(button3, 1, 1)

        self.groupBox.setLayout(gridLayout)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
