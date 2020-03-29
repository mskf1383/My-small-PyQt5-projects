"""by MSKF"""


from sys import argv
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot


# Main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.UI()

        # Set resize button as centeral widget
        self.setCentralWidget(self.resize_btn)
    

    # User interface
    def UI(self):
        self.setWindowTitle("resize.py")
        self.resize(200, 300)


        # Resize button
        self.resize_btn = QPushButton("resize", self)
        self.resize_btn.clicked.connect(self.RESIZE)


    # When resize button pressed
    @pyqtSlot()
    def RESIZE(self):
        self.resize(randint(200, 500), randint(200, 500))


# Application
app = QApplication(argv)
window = MainWindow()
window.show()
app.exec_()