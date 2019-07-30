# Layout Management

from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui
import sys

class Window(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Layout Management"
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
        self.groupBox = QGroupBox("What is your favorite Sport?")
        hboxLayout = QHBoxLayout()

        button = QPushButton("Football", self)
        button.move(50, 50)
        button.setToolTip("Football")
        hboxLayout.addWidget(button)

        button1 = QPushButton("Hockey", self)
        button1.move(50, 50)
        button1.setToolTip("Hockey")
        hboxLayout.addWidget(button1)

        button2 = QPushButton("Volleyball", self)
        button2.move(50, 50)
        button2.setToolTip("Volleyball")
        hboxLayout.addWidget(button2)

        self.groupBox.setLayout(hboxLayout)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
