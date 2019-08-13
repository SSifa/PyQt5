# Creating check boxes

from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel
from PyQt5 import QtGui
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt Check Box"
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

        self.check = QCheckBox("Football")
        self.check.setChecked(True)
        self.check.toggled.connect(self.onCheckbox)
        hboxLayout.addWidget(self.check)

        self.check1 = QCheckBox("Tennis")
        self.check1.toggled.connect(self.onCheckbox)
        hboxLayout.addWidget(self.check1)

        self.check2 = QCheckBox("Basketball")
        self.check2.toggled.connect(self.onCheckbox)
        hboxLayout.addWidget(self.check2)

        self.groupBox.setLayout(hboxLayout)

    def onCheckbox(self):
        checkbox = self.sender()

        if checkbox.isChecked():
            self.label.setText(checkbox.text() + " is selected.")


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())