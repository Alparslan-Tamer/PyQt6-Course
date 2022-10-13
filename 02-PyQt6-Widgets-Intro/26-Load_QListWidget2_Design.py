from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QPushButton, QLineEdit
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("26-QListWidget2_with_Designer.ui", self)

        self.list_widget = self.findChild(QListWidget, "listWidget")
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.add_item)
        self.line_edit = self.findChild(QLineEdit, "lineEdit")

    def add_item(self):
        self.list_widget.addItem(self.line_edit.text())
        self.line_edit.setText("")


app = QApplication([])
window = UI()
window.show()
app.exec()