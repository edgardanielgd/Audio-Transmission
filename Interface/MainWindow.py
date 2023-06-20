from Main import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QPushButton
from PySide6 import QtCore, QtGui, QtWidgets

import sys

class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

    
        self.setupUi(self)
        self.frame.setLayout(QtWidgets.QVBoxLayout())

        for i in range(1000):
            button = QPushButton("Button " + str(i))
            self.frame.layout().addWidget(button)
        
        print("Done")


# Construct a QApplication
app = QApplication([])
# Create a window and show it
test = Test()
test.show()
# Run the event loop
sys.exit(app.exec())
