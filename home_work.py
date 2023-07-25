from PyQt5.QtWidgets import *
from menuRepository import MenuRepository

class Window(QMainWindow):

    menu = MenuRepository().getAllData()


    def __init__(self):
        super().__init__()
        self.setFixedSize(300,600)

        geometry = 30
        for item in self.menu:
            self.newName = QCheckBox(item["foodName"],self)
            self.newName.move(30, geometry)
            geometry += 30

        self.btn = QPushButton("Submit", self)
        self.btn.move(30,300)
        self.btn.clicked.connect( self.checkOrder)

    def checkOrder(self):
        print(self.newName.isChecked())


app = QApplication([])
window = Window()
window.show()
app.exec()