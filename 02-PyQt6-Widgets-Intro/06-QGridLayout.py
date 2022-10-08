from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.ico"))
        self.setWindowTitle("PyQt6 QGridLayout")
        self.setStyleSheet("background-color: green")

        grid_layout = QGridLayout()

        btn1 = QPushButton("Click 1", self)
        btn2 = QPushButton("Click 2", self)
        btn3 = QPushButton("Click 3", self)
        btn4 = QPushButton("Click 4", self)
        btn5 = QPushButton("Click 5", self)
        btn6 = QPushButton("Click 6", self)
        btn7 = QPushButton("Click 7", self)
        btn8 = QPushButton("Click 8", self)

        grid_layout.addWidget(btn1, 0, 0)
        grid_layout.addWidget(btn2, 0, 1)
        grid_layout.addWidget(btn3, 0, 2)
        grid_layout.addWidget(btn4, 0, 3)
        grid_layout.addWidget(btn5, 1, 0)
        grid_layout.addWidget(btn6, 1, 1)
        grid_layout.addWidget(btn7, 1, 2)
        grid_layout.addWidget(btn8, 1, 3)

        self.setLayout(grid_layout)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
