from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTime, QTimer
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setGeometry(200, 200, 500, 200)
        self.setWindowIcon(QIcon("images/python.png"))
        self.setWindowTitle("PyQt6 QLCDNumber")
        self.setStyleSheet("background-color: green")

        self.create_combo()

    def create_combo(self):
        h_box = QHBoxLayout()

        label = QLabel("Select Account Type: ")
        label.setFont(QFont("Times", 15))

        self.combo = QComboBox()
        self.combo.addItem("Current Account")
        self.combo.addItem("Deposit Account")
        self.combo.addItem("Saving Account")
        self.combo.currentTextChanged.connect(self.combo_changed)

        v_box = QVBoxLayout()
        self.label_result = QLabel()
        self.label_result.setFont(QFont("Times", 15))
        v_box.addWidget(self.label_result)
        v_box.addLayout(h_box)

        h_box.addWidget(label)
        h_box.addWidget(self.combo)

        self.setLayout(v_box)

    def combo_changed(self):
        item = self.combo.currentText()
        self.label_result.setText("Your Account Type Is: " + item)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())