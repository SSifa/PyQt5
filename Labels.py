# PyQt5 Labels

from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
import sys

class Window(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Label"
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

        vbox = QVBoxLayout()
        label = QLabel("This is a label")
        vbox.addWidget(label)

        label2 = QLabel("Different Font type and Size")
        label2.setFont(QtGui.QFont("sanserif", 20))

        #Changing label2 text color
        label2.setStyleSheet("color:red")
        vbox.addWidget(label2)

        #Adding an image to a label
        label3 = QLabel(self)
        pixmap = QPixmap("home.png")
        label3.setPixmap(pixmap)
        vbox.addWidget(label3)

        self.setLayout(vbox)

        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
