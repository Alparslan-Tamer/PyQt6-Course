from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.png"))
        self.setWindowTitle("PyQt6 QCheckBox")
        self.setStyleSheet("background-color: green")

        h_box = QHBoxLayout()

        self.check_py = QCheckBox("Python")
        self.check_py.setIcon(QIcon("images/python.png"))
        self.check_py.setIconSize(QSize(40, 40))
        self.check_py.setFont(QFont("Sanserif", 20))
        self.check_py.stateChanged.connect(self.item_selected)

        self.check_java = QCheckBox("Java")
        self.check_java.setIcon(QIcon("images/java.png"))
        self.check_java.setIconSize(QSize(40, 40))
        self.check_java.setFont(QFont("Sanserif", 20))
        self.check_java.stateChanged.connect(self.item_selected)

        self.check_js = QCheckBox("JavaScript")
        self.check_js.setIcon(QIcon("images/js.png"))
        self.check_js.setIconSize(QSize(40, 40))
        self.check_js.setFont(QFont("Sanserif", 20))
        self.check_js.stateChanged.connect(self.item_selected)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("Sanserif", 20))

        v_box = QVBoxLayout()
        v_box.addWidget(self.label)

        h_box.addWidget(self.check_py)
        h_box.addWidget(self.check_java)
        h_box.addWidget(self.check_js)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

    def item_selected(self):
        value = ""

        if self.check_py.isChecked():
            value = self.check_py.text()

        if self.check_java.isChecked():
            value = self.check_java.text()

        if self.check_js.isChecked():
            value = self.check_js.text()

        self.label.setText("You have selected: " + value)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
