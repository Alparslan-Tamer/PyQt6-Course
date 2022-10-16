from PyQt6.QtWidgets import QApplication, QFontComboBox, QDialog, QLabel, QPlainTextEdit
from PyQt6.QtGui import QFont
from PyQt6 import uic


class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("28-QFontComboBox_with_Designer.ui", self)
        self.setWindowTitle("PyQt6 QFontComboBox")

        self.font_combo_box = self.findChild(QFontComboBox, "fontComboBox")
        self.plain_text_edit = self.findChild(QPlainTextEdit, "plainTextEdit")
        self.font_combo_box.currentFontChanged.connect(self.change_type)

    def change_type(self):
        my_font = QFont(self.font_combo_box.itemText(self.font_combo_box.currentIndex()))
        self.plain_text_edit.setFont(my_font)


app = QApplication([])
window = UI()
window.show()
app.exec()
