# This program creates a QtScrollArea application

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QFormLayout, QScrollArea, QGroupBox, QLabel, QVBoxLayout
from PyQt5 import QtGui
import sys


class Window(QWidget):

    def __init__(self, val):
        super().__init__()

        self.title = "PyQt Scroll Area"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.value = val

        self.labelList = []
        self.buttonList = []
        self.formLayout = QFormLayout()
        self.groupBpx = QGroupBox("Scroll Area")
        self.layout = QVBoxLayout()

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.scrollArea()
        self.setLayout(self.layout)

        self.show()

    def scrollArea(self):
        for i in range(self.value):
            self.labelList.append(QLabel("Label"))
            self.buttonList.append(QPushButton("Click me"))
            self.formLayout.addRow(self.labelList[i], self.buttonList[i])

        self.groupBpx.setLayout(self.formLayout)
        scroll = QScrollArea()
        scroll.setWidget(self.groupBpx)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        self.layout.addWidget(scroll)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window(30)
    sys.exit(App.exec())
