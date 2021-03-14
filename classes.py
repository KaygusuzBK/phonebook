class Person():
    def __init__(self):
        self.name = input("Enter a name: ")
        self.surname = input("Enter a surname: ")
        self.phoneNumber = input("Enter a phonenumber: ")

    def fullName(self):
        fullName = self.name + ' ' + self.surname
        return fullName

    def addToPerson(self):
        ContactList.addToList(self)
        ContactList.listItems()

class PersonList():
    def __init__(self):
        self.personList = []

    def addToList(self, Person):
        self.personList.append(Person)

    def listItems(self):
        for item in self.personList:
            print(item.name, item.surname, item.phoneNumber )

    def deletePerson(self):        
        deletePersonName = input("Enter the name to be deleted: ")
        for item in ContactList.personList:
            if  deletePersonName == item.name or deletePersonName == item.surname or deletePersonName == item.phoneNumber :
                ContactList.personList.remove(item)
                return
            else:
                print("No person found.")
                return
