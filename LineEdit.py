# Creating line edit

from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLineEdit, QLabel
from PyQt5 import QtGui
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt LineEdit"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.hbox = QHBoxLayout()
        self.label = QLabel(self)
        self.lineedit = QLineEdit(self)

        self.initWindow()

    def initWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label.setFont(QtGui.QFont("Sanserif", 15))

        self.lineEdits()

        self.setLayout(self.hbox)
        self.show()

    def lineEdits(self):
        self.lineedit.setFont(QtGui.QFont("sanserif", 15))
        self.lineedit.returnPressed.connect(self.onPressed)
        self.hbox.addWidget(self.lineedit)
        self.hbox.addWidget(self.label)

    def onPressed(self):
        self.label.setText(self.lineedit.text())


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
