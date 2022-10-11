from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLineEdit
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("23-QSlider_with_Designer.ui", self)

        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.line = self.findChild(QLineEdit, "lineEdit")

        self.slider.sliderMoved.connect(self.slider_changed)
        self.line.returnPressed.connect(self.line_changed)

    def slider_changed(self, value):
        self.line.setText(str(value))

    def line_changed(self):
        value = int(self.line.text())
        self.slider.setValue(value)


app = QApplication([])
window = UI()
window.show()
app.exec()
