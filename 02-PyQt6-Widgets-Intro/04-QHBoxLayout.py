from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.ico"))
        self.setWindowTitle("PyQt6 QHBoxLayout")
        self.setStyleSheet("background-color: green")

        h_box = QHBoxLayout()

        btn1 = QPushButton("Click 1", self)
        btn2 = QPushButton("Click 2", self)
        btn3 = QPushButton("Click 3", self)
        btn4 = QPushButton("Click 4", self)

        h_box.addWidget(btn1)
        h_box.addWidget(btn2)
        h_box.addWidget(btn3)
        h_box.addWidget(btn4)
        h_box.addSpacing(50)
        h_box.addStretch(5)

        self.setLayout(h_box)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
