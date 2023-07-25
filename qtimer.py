import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime

class WinForm(QWidget):
    _counter = 1
    def __init__(self,parent=None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('QTimer example')
        self.label = QLabel("0", self)
        self.label.setStyleSheet("""font-size: 40px""")
        self.label.adjustSize()
        self.btn = QPushButton("Start",self)
        self.btn.move(50, 50)

        self.btnStop = QPushButton("Stop",self)
        self.btnStop.move(50, 100)
        
        self.btn.clicked.connect(lambda: self.timer.start(10))
        self.btnStop.clicked.connect(lambda: self.timer.stop())


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.setNewNumber)
    

    def setNewNumber(self):
        self.label.setText(str(self._counter))
        self.label.adjustSize()
        
        self._counter += 1

    

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())