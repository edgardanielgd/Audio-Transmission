import sys
from PySide6 import QtCore, QtGui, QtWidgets, QtMultimedia 
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt
from PIL import Image, ImageQt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        
        self.setCentralWidget(self.label)
        painter = QtGui.QPainter(canvas)
        painter.drawLine(10, 10, 300, 200)
        painter.end()

        self.label.setPixmap(canvas)
        
        pil_img = Image.open("./Interface/Test.png")
        qimage = ImageQt.ImageQt(pil_img)
        qPixMap = QPixmap.fromImage( qimage )
        canvas2 = QtGui.QPixmap(qPixMap)
        self.label.setPixmap(canvas2)
        

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()