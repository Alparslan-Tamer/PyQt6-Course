from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowIcon(QIcon("images/python.ico"))
        self.setWindowTitle("PyQt6 QLabel")
        self.setStyleSheet("background-color: green")

        # General Label Configuration
        label = QLabel("Hello World", self)
        label.setText("New Hello World" + " " + str(12))
        label.move(100, 100)
        label.setFont(QFont("Times", 20))
        label.setStyleSheet("color: red")
        label.setNum(12)
        # label.clear()

        """ # Image Label #
        label = QLabel(self)
        pixmap = QPixmap("images/python.ico")
        label.setPixmap(pixmap)
        """

        """ # Animated Image Label #
        label = QLabel(self)
        movie = QMovie("images/v.gif")
        label.setMovie(movie)
        movie.start()
        """


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
