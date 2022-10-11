from PyQt6.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTime, QTimer
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.label = None
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.png"))
        self.setWindowTitle("PyQt6 QLCDNumber")
        self.setStyleSheet("background-color: green")

        timer = QTimer()
        timer.timeout.connect(self.show_lcd)
        timer.start(1000)

        self.show_lcd()

    def show_lcd(self):
        v_box = QVBoxLayout()

        lcd = QLCDNumber()
        lcd.setStyleSheet("background:red")

        v_box.addWidget(lcd)

        time = QTime.currentTime()
        text = time.toString("hh:mm")

        lcd.display(text)

        self.setLayout(v_box)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
