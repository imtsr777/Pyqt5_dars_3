from json import loads

class MenuRepository:

    _fileConnection = ""

    def getAllData(self):
        self._fileConnection = open("menu.json", "r")
        data = self._fileConnection.read()
        data = loads(data)
        return data
    



    def closeFile(self):
        self._fileConnection.close()



# obj = MenuRepository()
# print(type(obj.getAllData()))