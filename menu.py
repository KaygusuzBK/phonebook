import classes
while True:
    print(""" 
    1) Add Contact
    2) List Contact
    3) Delete Person

    """)

    if choose == "1":
        Person = classes.Person()
        Person.addToPerson()
    elif choose == "2" :
        classes.ContactList.listItems()
    elif choose == "3" :
        classes.ContactList.deletePerson()
    else:
        exit
