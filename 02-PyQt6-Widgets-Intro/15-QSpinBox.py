from PyQt6.QtWidgets import QApplication, QWidget, QSpinBox, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.png"))
        self.setWindowTitle("PyQt6 QSpinBox")
        self.setStyleSheet("background-color: green")

        h_box = QHBoxLayout()

        label = QLabel("Laptop price: ")
        label.setFont(QFont("Times", 20))

        self.line_edit = QLineEdit()
        self.spin_box = QSpinBox()
        self.spin_box.valueChanged.connect(self.spin_selected)
        self.total_res = QLineEdit()

        h_box.addWidget(label)
        h_box.addWidget(self.line_edit)
        h_box.addWidget(self.spin_box)
        h_box.addWidget(self.total_res)

        self.setLayout(h_box)

    def spin_selected(self):
        if self.line_edit.text() != 0:
            price = int(self.line_edit.text())
            total_price = self.spin_box.value() * price

            self.total_res.setText(str(total_price))
        else:
            print("Wrong value")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())