from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.png"))
        self.setWindowTitle("PyQt6 QSlider")
        self.setStyleSheet("background-color: green")

        h_box = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changed_slider)

        self.label = QLabel("")
        self.setFont(QFont("Times", 15))

        h_box.addWidget(self.slider)
        h_box.addWidget(self.label)

        self.setLayout(h_box)

    def changed_slider(self):
        value = self.slider.value()
        self.label.setText(str(value))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
