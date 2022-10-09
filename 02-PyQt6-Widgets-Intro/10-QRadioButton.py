from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setGeometry(200, 200, 500, 100)
        self.setWindowIcon(QIcon("images/python.ico"))
        self.setWindowTitle("PyQt6 QRadioButton")
        self.setStyleSheet("background-color: green")

        self.create_radio()

    def create_radio(self):
        h_box = QHBoxLayout()

        radio_button_py = QRadioButton("Python")
        radio_button_py.setIcon(QIcon("images/python.png"))
        radio_button_py.setIconSize(QSize(40, 40))
        radio_button_py.setFont(QFont("Times", 16))
        radio_button_py.setChecked(True)
        radio_button_py.toggled.connect(self.radio_selected)

        radio_button_java = QRadioButton("Java")
        radio_button_java.setIcon(QIcon("images/java.png"))
        radio_button_java.setIconSize(QSize(40, 40))
        radio_button_java.setFont(QFont("Times", 16))
        radio_button_java.toggled.connect(self.radio_selected)

        radio_button_js = QRadioButton("Javascript")
        radio_button_js.setIcon(QIcon("images/js.png"))
        radio_button_js.setIconSize(QSize(40, 40))
        radio_button_js.setFont(QFont("Times", 16))
        radio_button_js.toggled.connect(self.radio_selected)

        self.label = QLabel("")
        self.label.setFont(QFont("Times", 16))

        v_box = QVBoxLayout()
        v_box.addWidget(self.label)
        v_box.addLayout(h_box)

        h_box.addWidget(radio_button_py)
        h_box.addWidget(radio_button_java)
        h_box.addWidget(radio_button_js)
        self.setLayout(v_box)

    def radio_selected(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            self.label.setText(f"You have selected: {radio_button.text()}")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())