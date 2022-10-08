from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.ico"))
        self.setWindowTitle("PyQt6 - Event Handling")
        self.setStyleSheet("background-color: green")

        self.create_widgets()

    def create_widgets(self):
        h_box = QHBoxLayout()

        btn = QPushButton("Change Text", self)
        btn.clicked.connect(self.clicked_btn)
        self.label = QLabel("Default Text", self)

        h_box.addWidget(btn)
        h_box.addWidget(self.label)

        self.setLayout(h_box)

    def clicked_btn(self):
        self.label.setText("New Text")
        self.label.setFont(QFont("Times", 20))
        self.label.setStyleSheet("color: red")



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())