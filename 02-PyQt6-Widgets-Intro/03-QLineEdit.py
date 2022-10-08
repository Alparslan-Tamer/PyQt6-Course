from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.ico"))
        self.setWindowTitle("PyQt6 QLineEdit")
        self.setStyleSheet("background-color: green")

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Times", 20))
        # line_edit.setText("Default Text")
        # line_edit.setPlaceholderText("Enter Text")
        # line_edit.setEnabled(False)
        # line_edit.setEchoMode(QLineEdit.EchoMode.Password)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
