from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QDoubleSpinBox
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("16-QDoubleSpinBox_with_Designer.ui", self)

        self.line_price = self.findChild(QLineEdit, "lineEdit_price")
        self.double_spin = self.findChild(QDoubleSpinBox, "doubleSpinBox")
        self.line_result = self.findChild(QLineEdit, "lineEdit_total")

        self.double_spin.valueChanged.connect(self.spin_selected)

    def spin_selected(self):
        print(len(self.line_price.text()))
        if self.line_price.text() != 0 and self.line_price.text() != "":
            price = int(self.line_price.text())
            total_price = self.double_spin.value() * price

            self.line_result.setText(str(total_price))


app = QApplication([])
window = UI()
window.show()
app.exec()
