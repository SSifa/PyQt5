# This program creates splitters application

from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QHBoxLayout, QSplitter, QLineEdit
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt Splitters"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.hbox = QHBoxLayout()

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.splitters()
        self.setLayout(self.hbox)

        self.show()

    def splitters(self):
        leftFrame = QFrame()
        leftFrame.setFrameShape(QFrame.StyledPanel)

        bottomFrame = QFrame()
        bottomFrame.setFrameShape(QFrame.StyledPanel)

        lineEdit = QLineEdit()

        # Horizontal splitter
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(leftFrame)
        splitter1.addWidget(lineEdit)
        splitter1.setSizes([200, 200])

        # Vertical splitter
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottomFrame)

        self.hbox.addWidget(splitter2)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())