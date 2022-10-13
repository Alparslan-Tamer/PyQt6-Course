from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.png"))
        self.setWindowTitle("PyQt6 QListWidget")
        self.setStyleSheet("background-color: green")

        v_box = QVBoxLayout()

        self.list = QListWidget()
        self.list.insertItem(0, "Python")
        self.list.insertItem(1, "Java")
        self.list.insertItem(2, "JavaScript")
        self.list.insertItem(3, "C++")
        self.list.insertItem(4, "C#")
        self.list.insertItem(1, "Kotlin")
        self.list.setFont(QFont("Times", 15))
        self.list.setStyleSheet("background-color: white")
        self.list.clicked.connect(self.item_clicked)

        self.label = QLabel("")
        self.label.setFont(QFont("Times", 15))

        v_box.addWidget(self.list)
        v_box.addWidget(self.label)

        self.setLayout(v_box)

    def item_clicked(self):
        self.label.setText("You have selected: " + self.list.currentItem().text())


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
