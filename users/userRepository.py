from uuid import uuid4
from json import dumps, loads
from random import randint

class UserRepository:
    
    _fileName = "users.json"

    def __init__(self):
        self.fileConnection = open(self._fileName, "r")

    def getAllData(self):
        self.openFileForRead()
        users = self.fileConnection.read()
        users = loads(users)
        return users
    
    def getById(self, id):
        users = self.getAllData()
        for item in users:
            if( item["user_id"] == id ):
                return item
            

    def create(self, first_name, last_name, age):
        data = {
            "user_id": self.generateId(),
            "first_name":first_name,
            "last_name":last_name,
            "age":age
        }

        users = self.getAllData()
        users.append(data)
        users = dumps(users, indent=4)
        self.openFileForWrite()
        self.fileConnection.write(users)

    def search(self, word):
        data = self.getAllData()
        returningData = []
        for item in data:
            if( word.lower() in item["first_name"].lower() ):
                returningData.append(item)
        
        return returningData

        

    def deleteById(self, id):
        self.openFileForRead()
        users = self.fileConnection.read()
        users = loads(users)
        deleteId = None
        for index in range(len(users)):
            if( users[index]["user_id"] == id):
                deleteId = index
                break

        if( deleteId != None ):
            users.pop(deleteId)

        users = dumps(users, indent=4)
        self.openFileForWrite()
        self.fileConnection.write(users)

    def openFileForWrite(self):
        self.fileConnection.close()
        self.fileConnection = open(self._fileName, "w")

    def openFileForRead(self):
        self.fileConnection.close()
        self.fileConnection = open(self._fileName, "r")


    def generateId(self):
        randomId = randint(10000, 99999)
        return randomId




# user1 = UserRepository()
# print(user1.getById(11))
# user1.deleteById(11)
# user1.create("Avaz", "Saidov", 45)
