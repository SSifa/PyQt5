# This program creates a Spin box application

from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox, QLabel, QVBoxLayout
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt Spin Box"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.lable = QLabel(self)
        self.vbox = QVBoxLayout()
        self.spinbox = QSpinBox()

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.lable.setAlignment(Qt.AlignCenter)

        self.spinBox()
        self.vbox.addWidget(self.lable)
        self.setLayout(self.vbox)
        self.show()

    def spinBox(self):
        self.spinbox.valueChanged.connect(self.spin_value)
        self.vbox.addWidget(self.spinbox)

    def spin_value(self):
        val = self.spinbox.value()
        self.lable.setText("Spinbox value is: " + str(val))


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
