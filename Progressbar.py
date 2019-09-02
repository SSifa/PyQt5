# This program creates a Progressbar application

from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5 import QtGui
import time
import sys


class MyThread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        count = 0
        while count < 100:
            count += 1

            time.sleep(0.5)
            self.change_value.emit(count)


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.title = "PyQt Progressbar"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.thread = MyThread()

        self.progressbar = QProgressBar()
        self.button = QPushButton("Run Progressbar")

        self.InitUI()

    def InitUI(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey; border-radius: 5px; padding: 1px}"
                                       "QProgressBar::chunk {background:red}")
        self.button.clicked.connect(self.startProgressbar)

        vbox = QVBoxLayout()
        vbox.addWidget(self.progressbar)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

        self.show()

    def startProgressbar(self):
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()

    def setProgressVal(self, val):
        self.progressbar.setValue(val)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
