from PyQt6.QtWidgets import QApplication, QCalendarWidget, QWidget, QLabel, QPushButton, QSpinBox
from PyQt6.QtGui import QFont
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("31-Calender_Demo_with_Designer.ui", self)
        self.setWindowTitle("PyQt6 QCalendarWidget")

        self.calendarWidget = self.findChild(QCalendarWidget, "calendarWidget")
        self.spin_box = self.findChild(QSpinBox, "spinBox")
        self.push_button = self.findChild(QPushButton, "pushButton")
        self.push_button.clicked.connect(self.calculate)
        self.label_reservation = self.findChild(QLabel, "label_reservation")
        self.label_result = self.findChild(QLabel, "label_result")

    def calculate(self):
        rom_rent = 40
        date_selected = self.calendarWidget.selectedDate()
        date_in_string = str(date_selected.toPyDate())
        num_of_days = self.spin_box.value()

        self.label_reservation.setText(f"Reservation for {date_in_string} for {num_of_days} days")
        self.label_result.setText(f"Total cost: {rom_rent * num_of_days} $")


app = QApplication([])
window = UI()
window.show()
app.exec()
