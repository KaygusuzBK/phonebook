class Person():
    def __init__(self):
        self.name = input("Enter a name: ")
        self.surname = input("Enter a surname: ")
        self.phoneNumber = input("Enter a phonenumber: ")
    
    def fullName(self):
        fullName = self.name + ' ' + self.surname
        return fullName

class PersonList():
    def __init__(self):
        self.personList = []

    def addToList(self, Person):
        self.personList.append(Person)

    def listItems(self):
        for item in self.personList:
            print(item.name, item.surname, item.phoneNumber)
        with open("phonebook.txt","a",encoding="utf-8") as file:
            file.write(" ")
            file.write(item.name) 
            file.write(" ")
            file.write(item.surname)
            file.write(" ")
            file.write(item.phoneNumber)
            file.write("\n")

    def deletePerson(self, message = "delete person:"):
        deletePersonName = input(message)
        for item in ContactList.personList:
            if  deletePersonName == item.name or deletePersonName == item.surname or deletePersonName == item.phoneNumber :
                ContactList.personList.remove(item)
                return
            else:
                print("No person found.")
                return

    def searchPerson(self, message = "Enter a edit name: "):
        ContactList.deletePerson(message)
        person = Person()
        ContactList.addToList(person)

ContactList = PersonList()

