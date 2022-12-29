#Employee Dictionary
#By Yavuz Us

def main():
    employees = { 101 : "John" , 102 : "Doe" , 103 : "Yavuz" }
    runagain = True
    print("Welcome to the Employee Dictionary Function!")

    while runagain == True:    
        functionpick = input("Please pick a function to carry out Add(1), Remove by ID(2), Remove by Name(3), Update(4), View(5) or Exit(0): ")
        validation = functionpick.isdigit()
        while validation == False:
            print("Not a valid entry, please try again!")
            functionpick = input("Please pick a function to carry out Add(1), Remove by ID(2), Remove by Name(3), Update(4), View(5) or Exit(0): ")
            validation = functionpick.isdigit()
        functionpick = int(functionpick)
        if functionpick == 0 :
            print("Thank you for using our program!")
            runagain = False
        elif functionpick == 1 :
            addemp(employees)
        elif functionpick == 2 :
            removeid(employees)
        elif functionpick == 3 :
            removename(employees)
        elif functionpick == 4 :
            updateemp(employees)
        elif functionpick == 5 :
            viewemps(employees)
        else:
            print("Not a valid entry, please try again!")
            functionpick = input("Please pick a function to carry out Add(1), Remove by ID(2), Remove by Name(3), Update(4), View(5) or Exit(0): ")




def addemp(employees):
    print("To add a new employee please fill in the following fields ID Number (had to be a new unused integer) and Last Name (Make sure to spell correctly or you will need to update!)")
    newid = input("Please enter the new ID number: ")
    idvalid = newid.isdigit()
    while idvalid == False:
            print("That was not a valid entry, make sure to enter an integer!")
            newid = input("Please enter new Emplotee name associated with the new ID: ")
            idvalid = newid.isdigit()
    newid = int(newid)
    while newid in employees :
        print("That was not a valid entry, make sure to enter an ID which dosen't exist!")
        newid = input("Please enter a new ID number: ")
        idvalid = newid.isdigit()
        while idvalid == False:
            print("That was not a valid entry, make sure to enter an integer!")
            newid = input("Please enter new ID number to be associated new employee: ")
            idvalid = newid.isdigit()
    newid = int(newid)
    newname = input("Please enter new Employee name to be associated with the new ID: ")
    namevalid = newname.isdigit()
    while namevalid == True:
        print("That was not a valid entry, make sure to enter a name!")
        newname = input("Please enter new Employee name associated with the new ID: ")
        namevalid = newname.isdigit()
    for x in employees:
        if employees[x] == newname:
            namevalid = True
            while namevalid == True:
                print("That employee already exists, please enter a new name!")
                newname = input("Please enter new Employee name associated with the new ID: ")
                if employees[x] == newname:
                    namevalid = True
                else:
                    namevalid = False
    employees[newid] = newname
    return employees

def removeid(employees):
    idrem = input("To remove an employee by ID number enter desired ID number: ")
    if idrem.isdigit():
        idrem = int(idrem)
    while idrem not in employees :
        print("That was not a valid entry, lets try again!")
        idrem = input("To remove an employee by ID number enter desired ID number: ")
        idvalid = idrem.isdigit()
        while idvalid == False :
            print("That was not a valid entry, lets try again!")
            idrem = input("To remove an employee by ID number enter desired ID number: ")
            idvalid = idrem.isdigit()
        idrem = int(idrem)  
    print(f"Employee with ID number {idrem}, named {employees[idrem]} is being removed!")
    employees.pop(idrem)
    return employees


def removename(employees):
    namerem = input("To remove an employee, enter their name (if a name which does not exist is entered, the program revert to main menu): ")
    for x in employees :
        if employees[x] == namerem:
            print(f"Employee with the name {namerem} and ID number {x} is being removed")
            employees.pop(x)
            break
    return employees

def updateemp(employees):
    idup = input("To update an employee enter their ID number: ")
    if idup.isdigit():
        idup = int(idup)
    while idup not in employees :
        print("That was not a valid entry, lets try again!")
        idup = input("To update an employee enter their ID number: ")
        idvalid = idup.isdigit()
        while idvalid == False :
            print("That was not a valid entry, lets try again!")
            idup = input("To update an employee enter their ID number: ")
            idvalid = idup.isdigit()
        idup = int(idup)  
    print(f"Employee with ID number {idup}, named {employees[idup]} is being updated. ")
    newname = input("Enter the new name to be associated with ID number: ")
    employees[idup] = newname
    return employees

def viewemps(employees):
    for x in employees:
        print(f"Employee with the ID number {x}, is named {employees[x]}")
    return employees


main()
