from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.png"))
        self.setWindowTitle("PyQt6 QTableWidget")
        self.setStyleSheet("background-color: green")

        v_box = QVBoxLayout()

        table_widget = QTableWidget()
        table_widget.setRowCount(3)
        table_widget.setColumnCount(3)

        table_widget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        table_widget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        table_widget.setItem(0, 2, QTableWidgetItem("Cell (1,3)"))
        table_widget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        table_widget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        table_widget.setItem(1, 2, QTableWidgetItem("Cell (2,3)"))
        table_widget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        table_widget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        table_widget.setItem(2, 2, QTableWidgetItem("Cell (3,3)"))

        v_box.addWidget(table_widget)

        self.setLayout(v_box)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
