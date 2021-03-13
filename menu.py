import classes

print(""" 
1) Add Contact
2) List Contact

Plase enter any key to exit...
""")

choose = input("Please Choose Your Option: ")
if choose == "1":
    Person = classes.Person()
    Person.addToPerson()
elif choose == "2" :
    classes.ContanctList.listItem()
else:
    exit