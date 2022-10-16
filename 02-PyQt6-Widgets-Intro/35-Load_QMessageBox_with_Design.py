from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QDialog, QPushButton


class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("35-QMessageBox_with_Designer.ui", self)
        self.setWindowTitle("PyQt6 QMessageBox")

        self.button_warning = self.findChild(QPushButton, "pushButton_warning")
        self.button_warning.clicked.connect(self.warning_message)
        self.button_info = self.findChild(QPushButton, "pushButton_info")
        self.button_info.clicked.connect(self.info_message)
        self.button_about = self.findChild(QPushButton, "pushButton_about")
        self.button_about.clicked.connect(self.about_message)

    def warning_message(self):
        QMessageBox.warning(self, "Warning", "This is a warning message")

    def info_message(self):
        QMessageBox.information(self, "Information", "This is an information message")

    def about_message(self):
        QMessageBox.about(self, "About", "This is an about message")


app = QApplication([])
window = UI()
window.show()
app.exec()