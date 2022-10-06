from PyQt6.QtWidgets import QApplication, QDialog
import sys

# Create an instance of QApplication
app = QApplication(sys.argv)
# Create an instance of your application's window
window = QDialog()
# Show your application's GUI
window.show()
# Execute your application
sys.exit(app.exec())
