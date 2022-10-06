from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# Create an instance of QApplication
app = QApplication(sys.argv)
# Create an instance of your application's window
window = QMainWindow()
window.statusBar().showMessage("Hello World")
window.menuBar().addMenu("File")
# Show your application's GUI
window.show()
# Execute your application
sys.exit(app.exec())
