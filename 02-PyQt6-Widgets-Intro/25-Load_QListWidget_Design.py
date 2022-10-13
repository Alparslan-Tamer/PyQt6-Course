from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QLabel
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("25-QListWidget_with_Designer.ui", self)

        self.list_widget = self.findChild(QListWidget, "listWidget")
        self.list_widget.itemSelectionChanged.connect(self.list_changed)
        self.label_result = self.findChild(QLabel, "label_result")

    def list_changed(self):
        self.label_result.setText("You have selected: " + self.list_widget.currentItem().text())


app = QApplication([])
window = UI()
window.show()
app.exec()
