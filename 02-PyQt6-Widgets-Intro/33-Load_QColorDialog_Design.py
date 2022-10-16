from PyQt6.QtWidgets import QApplication, QColorDialog, QDialog, QPushButton, QTextEdit, QLabel
from PyQt6 import uic


class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("33-QColorDialog_with_Designer.ui", self)
        self.setWindowTitle("PyQt6 QColorDialog")

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.choose_color)
        self.text_edit = self.findChild(QTextEdit, "textEdit")
        self.label_result = self.findChild(QLabel, "label_result")

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextColor(color)
            self.label_result.setText(f"You have selected color with code: {color.name()}")


app = QApplication([])
window = UI()
window.show()
app.exec()