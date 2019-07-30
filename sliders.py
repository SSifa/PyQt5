import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QHBoxLayout, QLabel, QGroupBox, QVBoxLayout, QGridLayout, \
    QDesktopWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Slider"
        self.windowWidth = 650
        self.windowHeight = 650
        self.left = 200
        self.top = 100
        self.iconName = "breast.jpg"

        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))

        sizeObject = QDesktopWidget().screenGeometry(-1)
        screenWidth = sizeObject.width()
        screenHeight = sizeObject.height()

        self.x_coordinate = (screenWidth / 2 - self.windowWidth / 2)
        self.y_coordinate = (screenHeight / 2 - self.windowHeight / 2)

        self.setGeometry(self.x_coordinate, self.y_coordinate, self.windowWidth, self.windowHeight)
        self.setStyleSheet("background-color:green")

        label = QLabel("Breast Cancer Predictor")
        label.setFont(QtGui.QFont("Sanserif", 15))

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(self.groupbox)

        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupbox = QGroupBox("Set the feature size")
        self.groupbox.setFont(QtGui.QFont("Sanserif", 15))
        self.groupbox.setStyleSheet("background-color:cyan")
        self.groupbox.setMinimumSize(650, 600)
        gridLayout = QGridLayout()

        ################### First Slider ###################################
        self.label = QLabel("Clump Thickness:")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label, 0, 0)

        self.slider1 = QSlider()
        self.slider1.setOrientation(Qt.Horizontal)
        self.slider1.setTickPosition(QSlider.TicksBelow)
        self.slider1.setTickInterval(1)
        self.slider1.setMinimum(0)
        self.slider1.setMaximum(10)
        self.slider1.valueChanged.connect(self.changedValue)
        gridLayout.addWidget(self.slider1, 0, 1)

        self.label1 = QLabel("0")
        self.label1.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label1, 0, 2)

        ################### Second Slider ###################################
        self.label = QLabel("Uniformity of Cell Size:")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label, 1, 0)

        self.slider2 = QSlider()
        self.slider2.setOrientation(Qt.Horizontal)
        self.slider2.setTickPosition(QSlider.TicksBelow)
        self.slider2.setTickInterval(1)
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(10)
        self.slider2.valueChanged.connect(self.changedValue)
        gridLayout.addWidget(self.slider2, 1, 1)

        self.label2 = QLabel("0")
        self.label2.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label2, 1, 2)

        ################### Third Slider ###################################
        self.label = QLabel("Uniformity of Cell Shape:")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label, 2, 0)

        self.slider3 = QSlider()
        self.slider3.setOrientation(Qt.Horizontal)
        self.slider3.setTickPosition(QSlider.TicksBelow)
        self.slider3.setTickInterval(1)
        self.slider3.setMinimum(0)
        self.slider3.setMaximum(10)
        self.slider3.valueChanged.connect(self.changedValue)
        gridLayout.addWidget(self.slider3, 2, 1)

        self.label3 = QLabel("0")
        self.label3.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label3, 2, 2)

        ################### Fourth Slider ###################################
        self.label = QLabel("Marginal Adhesion:")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label, 3, 0)

        self.slider4 = QSlider()
        self.slider4.setOrientation(Qt.Horizontal)
        self.slider4.setTickPosition(QSlider.TicksBelow)
        self.slider4.setTickInterval(1)
        self.slider4.setMinimum(0)
        self.slider4.setMaximum(10)
        self.slider4.valueChanged.connect(self.changedValue)
        gridLayout.addWidget(self.slider4, 3, 1)

        self.label4 = QLabel("0")
        self.label4.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label4, 3, 2)

        ################### Fifth Slider ###################################
        self.label = QLabel("Single Epithelial Cell Size:")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label, 4, 0)

        self.slider5 = QSlider()
        self.slider5.setOrientation(Qt.Horizontal)
        self.slider5.setTickPosition(QSlider.TicksBelow)
        self.slider5.setTickInterval(1)
        self.slider5.setMinimum(0)
        self.slider5.setMaximum(10)
        self.slider5.valueChanged.connect(self.changedValue)
        gridLayout.addWidget(self.slider5, 4, 1)

        self.label5 = QLabel("0")
        self.label5.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label5, 4, 2)

        ################### Sixth Slider ###################################
        self.label = QLabel("Bare Nuclei:")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label, 5, 0)

        self.slider6 = QSlider()
        self.slider6.setOrientation(Qt.Horizontal)
        self.slider6.setTickPosition(QSlider.TicksBelow)
        self.slider6.setTickInterval(1)
        self.slider6.setMinimum(0)
        self.slider6.setMaximum(10)
        self.slider6.valueChanged.connect(self.changedValue)
        gridLayout.addWidget(self.slider6, 5, 1)

        self.label6 = QLabel("0")
        self.label6.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label6, 5, 2)

        ################### Seventh Slider ###################################
        self.label = QLabel("Bland Chromatin:")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label, 6, 0)

        self.slider7 = QSlider()
        self.slider7.setOrientation(Qt.Horizontal)
        self.slider7.setTickPosition(QSlider.TicksBelow)
        self.slider7.setTickInterval(1)
        self.slider7.setMinimum(0)
        self.slider7.setMaximum(10)
        self.slider7.valueChanged.connect(self.changedValue)
        gridLayout.addWidget(self.slider7, 6, 1)

        self.label7 = QLabel("0")
        self.label7.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label7, 6, 2)

        ################### Eighth Slider ###################################
        self.label = QLabel("Normal Nucleoli:")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(self.label, 7, 0)

        slider8 = QSlider()
        slider8.setOrientation(Qt.Horizontal)
        slider8.setTickPosition(QSlider.TicksBelow)
        slider8.setTickInterval(1)
        slider8.setMinimum(0)
        slider8.setMaximum(10)
        slider8.valueChanged.connect(self.changedValue)
        gridLayout.addWidget(slider8, 7, 1)

        label8 = QLabel("0")
        label8.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(label8, 7, 2)

        ################### Ninth Slider ###################################
        label = QLabel("Mitoses:")
        label.setAlignment(Qt.AlignRight)
        label.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(label, 8, 0)

        slider9 = QSlider()
        slider9.setOrientation(Qt.Horizontal)
        slider9.setTickPosition(QSlider.TicksBelow)
        slider9.setTickInterval(1)
        slider9.setMinimum(0)
        slider9.setMaximum(10)
        slider9.valueChanged.connect(self.changedValue)
        gridLayout.addWidget(slider9, 8, 1)

        label9 = QLabel("0")
        label9.setFont(QtGui.QFont("Sanserif", 15))
        gridLayout.addWidget(label9, 8, 2)

        self.groupbox.setLayout(gridLayout)


    def changedValue(self):
        size = self.slider1.value()
        self.label1.setText(str(size))


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())