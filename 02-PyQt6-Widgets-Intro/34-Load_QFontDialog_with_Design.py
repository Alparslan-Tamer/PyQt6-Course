from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QFontDialog, QDialog, QPushButton, QTextEdit


class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("34-QFontDialog_with_Designer.ui", self)
        self.setWindowTitle("PyQt6 QFontDialog")

        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.change_font)
        self.text_edit = self.findChild(QTextEdit, "textEdit")

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)


app = QApplication([])
window = UI()
window.show()
app.exec()