# Creating radio buttons

from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel
from PyQt5 import QtGui
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt Radio Buttons"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))

        self.radioButton()
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.groupBox)
        vboxLayout.addWidget(self.label)

        self.setLayout(vboxLayout)

        self.show()

    def radioButton(self):
        self.groupBox = QGroupBox("What is your Favorite sport?")
        self.groupBox.setFont(QtGui.QFont("Sanserif", 15))

        hboxLayout = QHBoxLayout()

        self.radiobtn = QRadioButton("Football")
        self.radiobtn.setChecked(True)
        self.radiobtn.toggled.connect(self.onRadioButton)
        hboxLayout.addWidget(self.radiobtn)

        self.radiobtn1 = QRadioButton("Tennis")
        self.radiobtn1.toggled.connect(self.onRadioButton)
        hboxLayout.addWidget(self.radiobtn1)

        self.radiobtn2 = QRadioButton("Basketball")
        self.radiobtn2.toggled.connect(self.onRadioButton)
        hboxLayout.addWidget(self.radiobtn2)

        self.groupBox.setLayout(hboxLayout)

    def onRadioButton(self):
        radioButton = self.sender()

        if radioButton.isChecked():
            self.label.setText(radioButton.text() + " is selected.")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
