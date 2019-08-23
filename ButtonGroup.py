#This program creates a Button group application

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QButtonGroup, QLabel, QHBoxLayout
from PyQt5 import QtGui
import sys

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt ButtonGroup"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.buttongroup = QButtonGroup()
        self.hbox = QHBoxLayout()
        self.label = QLabel(self)

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.buttongroup.buttonClicked[int].connect(self.onButtonClicked)
        self.buttongroup.buttonPressed[int].connect(self.onButtonPressed)
        self.buttongroup.buttonReleased[int].connect(self.onButtonReleased)
        self.buttonGroup()
        self.hbox.addWidget(self.label)
        self.setLayout(self.hbox)

        self.show()

    def buttonGroup(self):
        button = QPushButton('Python')
        self.buttongroup.addButton(button, 1)
        self.hbox.addWidget(button)

        button2 = QPushButton('Java')
        self.buttongroup.addButton(button2, 2)
        self.hbox.addWidget(button2)

        button3 = QPushButton('C++')
        self.buttongroup.addButton(button3, 3)
        self.hbox.addWidget(button3)

    def onButtonClicked(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.label.setText(button.text() + ' was clicked')

    def onButtonPressed(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.label.setText(button.text() + ' was pressed!')

    def onButtonReleased(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.label.setText(button.text() + ' was released!')


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
