# This program creates a QtMainWindow application

from PyQt5.QtWidgets import QWidget, QApplication, QDial, QLabel, QVBoxLayout
from PyQt5 import QtGui
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt QDial"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.vbox = QVBoxLayout()
        self.dial = QDial()
        self.label = QLabel(self)

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.Dial()
        self.setLayout(self.vbox)

        self.show()

    def Dial(self):
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.dial.valueChanged.connect(self.dial_changed)
        self.vbox.addWidget(self.dial)
        self.vbox.addWidget(self.label)

    def dial_changed(self):
        val = self.dial.value()
        self.label.setText("Dial value is: " + str(val))


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
