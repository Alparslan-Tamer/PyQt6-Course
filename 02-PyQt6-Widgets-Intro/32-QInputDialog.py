from PyQt6.QtWidgets import QApplication, QDialog, QInputDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.png"))
        self.setWindowTitle("PyQt6 QInputDialog")

        self.create_dialog()

    def create_dialog(self):
        h_box = QHBoxLayout()

        label = QLabel("Choose Country: ")
        label.setFont(QFont("Times", 15))

        self.line_edit = QLineEdit()
        self.line_edit.setFont(QFont("Times", 15))

        btn = QPushButton("Choose Country")
        btn.setFont(QFont("Times", 15))
        btn.clicked.connect(self.get_int)

        h_box.addWidget(label)
        h_box.addWidget(self.line_edit)
        h_box.addWidget(btn)

        self.setLayout(h_box)

    def show_dialog(self):
        countries = ["Afghanistan", "Albania", "India", "Pakistan", "United States", "United Kingdom", "Turkey"]

        country, ok = QInputDialog.getItem(self, "Input Dialog", "List of Countries", countries, 0, False)

        if ok and country:
            self.line_edit.setText(country)

    def get_text(self):
        text, ok = QInputDialog.getText(self, "Get Username", "Enter Your Name: ")

        if ok and text:
            self.line_edit.setText(text)

    def get_int(self):
        num, ok = QInputDialog.getInt(self, "Get Number", "Enter a number: ", 0, 0, 100, 1)

        if ok and num:
            self.line_edit.setText(str(num))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())