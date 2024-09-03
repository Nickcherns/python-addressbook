from addressBook import AddressBook

book = AddressBook()

def mainMenu():
    print("----------------------------------------------")
    print("Welcome to the Address Book")
    print("----------------------------------------------")
    print("1. Add an Entry")
    print("2. Remove an Entry")
    print("3. Search for an Entry")
    print("4. Print the Address Book")
    print("5. Clear Address Book")
    print("6. Quit")
    print("----------------------------------------------")
    selectMainMenu()
    
def selectMainMenu():
    selection = input("Enter a number to continue... ")

    if selection == "1":
        print("DEBUG: Selection = 1")
        addEntryToBook()
    elif selection == "2":
        print("DEBUG: Selection = 2")
    elif selection == "3":
        print("DEBUG: Selection = 3")
    elif selection == "4":
        print("DEBUG: Selection = 4")
        printAddressBook()
    elif selection == "5":
        print("DEBUG: Selection = 5")
    elif selection == "6":
        print("DEBUG: Selection = 6")
        exit(1)
    else:
        print("Selection not found...")
        selectMainMenu()

def addEntryToBook():
    print("\n\nEnter information to add entry to Address Book")
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    phoneNumber = input("Phone Number: ")
    emailAddress = input("Email Address: ")
    newEntry = {
        "First Name: " : firstName,
        "Last Name: " : lastName,
        "Phone Number: " : phoneNumber,
        "Email Address: " : emailAddress
    }
    book.addEntry(newEntry)
    print("Entry Added!")
    returnToMainMenu()

def printAddressBook():
    book.printBook(book.book)
    print(book.debugPrintRawBook())
    returnToMainMenu()

def returnToMainMenu():
    enterInput = input("Press enter to continue to the Main Menu...")
    if enterInput == "":
        mainMenu()
    else:
        returnToMainMenu()  



mainMenu()


