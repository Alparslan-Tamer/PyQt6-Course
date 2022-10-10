from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QSpinBox, QLabel
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("17-QSpinBox_EditingFinished_with_Designer.ui", self)

        self.line_p_price = self.findChild(QLineEdit, "lineEdit_p_price")
        self.line_p_total = self.findChild(QLineEdit, "lineEdit_p_total")
        self.line_s_price = self.findChild(QLineEdit, "lineEdit_s_price")
        self.line_s_total = self.findChild(QLineEdit, "lineEdit_s_total")
        self.spin_p = self.findChild(QSpinBox, "spinBox")
        self.spin_p.editingFinished.connect(self.pen_result)
        self.spin_s = self.findChild(QSpinBox, "spinBox_2")
        self.spin_s.editingFinished.connect(self.sugar_result)
        self.label_result = self.findChild(QLabel, "label_result")

    def pen_result(self):
        pen_price = int(self.line_p_price.text())
        total_pen_price = self.spin_p.value() * pen_price
        self.line_p_total.setText(str(total_pen_price))

    def sugar_result(self):
        sugar_price = int(self.line_s_price.text())
        total_sugar_price = self.spin_s.value() * sugar_price
        self.line_s_total.setText(str(total_sugar_price))

        self.get_total_price()

    def get_total_price(self):
        total_pen_price = int(self.line_p_total.text())
        total_sugar_price = int(self.line_s_total.text())
        total_price = total_pen_price + total_sugar_price

        self.label_result.setText("Total Price Is: {}".format(total_price))

app = QApplication([])
window = UI()
window.show()
app.exec()
