from PyQt6.QtWidgets import QApplication, QLineEdit, QListWidget, QPushButton, QDialog, QInputDialog, QMessageBox
from PyQt6 import uic


class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("27-QListWidget_CRUD_with_Designer.ui", self)
        self.setWindowTitle("PyQt6 QListWidget CRUD")

        self.list_widget = self.findChild(QListWidget, "listWidget")
        self.button_add = self.findChild(QPushButton, "pushButton_add")
        self.button_add.clicked.connect(self.add_item)
        self.button_edit = self.findChild(QPushButton, "pushButton_edit")
        self.button_edit.clicked.connect(self.edit_item)
        self.button_remove = self.findChild(QPushButton, "pushButton_remove")
        self.button_remove.clicked.connect(self.remove_item)
        self.button_sort = self.findChild(QPushButton, "pushButton_sort")
        self.button_sort.clicked.connect(self.sort_items)

    def add_item(self):
        row = self.list_widget.currentRow()
        title = "Add Item"
        data, ret = QInputDialog.getText(self, title, title)
        if ret and data is not None:
            self.list_widget.insertItem(row, data)

    def edit_item(self):
        row = self.list_widget.currentRow()
        item = self.list_widget.item(row)

        if item is not None:
            title = "Edit Item"
            data, ret = QInputDialog.getText(self, title, title, QLineEdit.EchoMode.Normal, item.text())
            if ret and data is not None:
                item.setText(data)

    def remove_item(self):
        row = self.list_widget.currentRow()
        item = self.list_widget.item(row)

        if item is None:
            return

        reply = QMessageBox.question(self, "Remove Item", "Do you want to remove this item?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            self.list_widget.takeItem(row)

    def sort_items(self):
        self.list_widget.sortItems()


app = QApplication([])
window = UI()
window.show()
app.exec()