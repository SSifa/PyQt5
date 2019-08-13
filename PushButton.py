# A simple PyQt5 project to create a functional Push Button

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtGui
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Pusb Button"
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

        self.UiComponents()

        self.show()

    def UiComponents(self):
        button = QPushButton("Close Application", self)
        button.move(50, 50)
        button.setToolTip("Clicking this button will close the Application")
        button.clicked.connect(self.CloseApplication)

    def CloseApplication(self):
        sys.exit()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())