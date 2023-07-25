from PyQt5.QtWidgets import *
from userRepository import UserRepository


class MainWindow(QMainWindow):
    _userRepository = UserRepository()

    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 700)
        self.searchInput = QLineEdit(self)
        self.searchInput.textChanged.connect(self.searchUsers)

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(20, 60, 260, 500)
        self.setListWidgetItems(self._userRepository.getAllData())
        self.listWidget.itemClicked.connect(self.showUserInfo)

    def setListWidgetItems(self, data):
        self.listWidget.clear()

        for item in data:
            newItem = QListWidgetItem(item["first_name"]) 
            newItem.userData = item
            self.listWidget.addItem(newItem)


    def showUserInfo(self):
        userInfo = self.listWidget.currentItem().userData
        self.userInfoFront = UserInfoFront(userInfo["user_id"], self)
        self.userInfoFront.show()


    def searchUsers(self):
        word = self.searchInput.text()
        data = self._userRepository.search(word)
        self.setListWidgetItems(data)



class UserInfoFront(QMainWindow):
    _userData = {}
    _userRepository = UserRepository()
    def __init__(self, userId, mainClass):
        self._userId = userId
        self._mainClass = mainClass

        super().__init__()
        self.setFixedSize(400, 400)
        
        self._userData = self._userRepository.getById(userId)
        
        if( not self._userData ):
            notFound = QLabel("Topilmadi", self)
            notFound.move(150, 150)
            notFound.setStyleSheet("font-size: 20px")
            return
        
        self.firstNameLabel = QLabel("Firstname: " + self._userData["first_name"], self)
        self.firstNameLabel.move(30, 40)
        self.firstNameLabel.setStyleSheet("font-size: 30px")
        self.firstNameLabel.adjustSize()

        self.lastNameLabel = QLabel("Lastname: " + self._userData["last_name"], self)
        self.lastNameLabel.move(30, 90)
        self.lastNameLabel.setStyleSheet("font-size: 30px")
        self.lastNameLabel.adjustSize()
        

        self.idLabel = QLabel("Id: " + str(self._userData["user_id"]), self)
        self.idLabel.move(30, 140)
        self.idLabel.setStyleSheet("font-size: 30px")
        self.idLabel.adjustSize()


        self.ageLabel = QLabel("Age: " + str(self._userData["age"]), self)
        self.ageLabel.move(30, 190)
        self.ageLabel.setStyleSheet("font-size: 30px")
        self.ageLabel.adjustSize()


        self.closeBtn = QPushButton("Close", self)
        self.closeBtn.clicked.connect(lambda: self.close())
        
        self.deleteBtn = QPushButton("Delete", self)
        self.deleteBtn.move(120,0)
        self.deleteBtn.setStyleSheet("background-color:red")
        self.deleteBtn.clicked.connect(self.deleteUser)


    def deleteUser(self):
        self._userRepository.deleteById(self._userId)
        self.messageBox("User deleted")
        self._mainClass.setListWidgetItems([])
        self.close()


    def messageBox(self, word):
        msg = QMessageBox(self)
        msg.setText(word)
        msg.show()
        msg.exec()





app = QApplication([])
obj = MainWindow()
obj.show()
app.exec()