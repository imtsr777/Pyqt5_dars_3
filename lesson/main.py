from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300,400)
        self.btn = QPushButton("Click",self)
        self.btn.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.secondWindow = SeconWindow()
        self.secondWindow.show()
        self.close()


class SeconWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300,400)
        self.setWindowTitle("Second window")
        self.btn = QPushButton("First",self)

        self.btn.clicked.connect(self.openFirstWindow)


    def openFirstWindow(self):
        self.firstWindow = MainWindow()
        self.firstWindow.show()
        self.close()



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
