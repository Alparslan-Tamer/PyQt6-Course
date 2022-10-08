from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.ico"))
        self.setWindowTitle("PyQt6 QVBoxLayout")
        self.setStyleSheet("background-color: green")

        v_box = QVBoxLayout()

        btn1 = QPushButton("Click 1", self)
        btn2 = QPushButton("Click 2", self)
        btn3 = QPushButton("Click 3", self)
        btn4 = QPushButton("Click 4", self)

        v_box.addWidget(btn1)
        v_box.addWidget(btn2)
        v_box.addWidget(btn3)
        v_box.addWidget(btn4)
        v_box.addSpacing(50)
        v_box.addStretch(5)

        self.setLayout(v_box)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
