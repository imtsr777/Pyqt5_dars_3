import sys
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *

from menuRepository import MenuRepository

class Window(QWidget):

    menu = MenuRepository().getAllData()

    def __init__(self, many):
        super().__init__()

        self.layoutH = QHBoxLayout()

        for item in self.menu:
            self.checkbox = QCheckBox(item["foodName"])
            self.checkbox.setCheckState(Qt.Unchecked)

            self.layoutH.addWidget(self.checkbox)
            self.layoutH.setAlignment(Qt.AlignCenter)

        self.label  = QLabel("selected QCheckBox: ")
        self.button = QPushButton("Query whether or not a checkbox is checked")
        self.button.clicked.connect(self.ButtonClicked)

        layoutV     = QVBoxLayout(self)
        layoutV.addLayout(self.layoutH)
        layoutV.addWidget(self.label)
        layoutV.addWidget(self.button)

    def ButtonClicked(self):
        summa = 0

        for i in range(self.layoutH.count()):
            chBox = self.layoutH.itemAt(i).widget()
            if chBox.isChecked():
                for item in self.menu:
                    if( chBox.text() == item["foodName"] ):
                        summa += item["price"]
                        break

        self.label.setText("selected QCheckBox: " + str(summa))  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window(7)
    window.resize(350, 300)
    window.show()
    sys.exit(app.exec_())