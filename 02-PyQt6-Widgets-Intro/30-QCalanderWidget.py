from PyQt6.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.png"))
        self.setWindowTitle("PyQt6 QCalendarWidget")

        v_box = QVBoxLayout()

        self.calender = QCalendarWidget()
        self.calender.setGridVisible(True)
        self.calender.selectionChanged.connect(self.calender_date)

        self.label = QLabel("")
        self.label.setFont(QFont("Times", 15))
        self.label.setStyleSheet("color: green")

        v_box.addWidget(self.calender)
        v_box.addWidget(self.label)

        self.setLayout(v_box)

    def calender_date(self):
        date = self.calender.selectedDate()
        self.label.setText("Selected Date: " + date.toString())


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
