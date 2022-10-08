from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.ico"))
        self.setWindowTitle("PyQt6 QPushButton")
        self.setStyleSheet("background-color: green")

        self.create_button()

    def create_button(self):
        btn = QPushButton("Click Me", self)
        btn.setGeometry(100, 100, 200, 50)
        btn.setFont(QFont("Times", 20, QFont.Weight.Bold))
        btn.setIcon(QIcon("images/python.ico"))
        btn.setIconSize(QSize(36, 36))

        # popup menu
        menu = QMenu()
        menu.setFont(QFont("Times", 20, QFont.Weight.Bold))
        menu.setStyleSheet("background-color: green")
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
