#
#
# TO DO:
# 1. add input validation
#   a. email address
#   b. phone number
#   c. names (numbers not allowed)
# 2. prettify
# 3. when address book is empty, have it display an empty message
#
#

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

    
    
    
    
    
    
    if selection == "1": # 1. Add an Entry [WORKS]
        print("DEBUG: Selection = 1")
        addEntryToBook() 
    elif selection == "2": # 2. Remove an Entry
        print("DEBUG: Selection = 2")
    elif selection == "3": # 3. Search for an Entry
        print("DEBUG: Selection = 3")
        searchAddressBook()
    elif selection == "4": # 4. Print the Address Book [WORKS + DEBUG CHECK]
        print("DEBUG: Selection = 4")
        printAddressBook() 
    elif selection == "5": # 5. Clear Address Book [WORKS - book needs clarification when empty]
        print("DEBUG: Selection = 5")
        clearAddressBook()
    elif selection == "6": # 6. Quit [WORKS]
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

def searchAddressBook():
    print("\nSelect your search type....")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. Email Address")
    selection = input("Input your selection: ")
    if selection == 1:
        searchType = "first name"
        searchValue = input("\nEnter first name to search by: ")
        print(book.searchBook(searchType, searchValue))
    elif selection == 2:
        searchType = "last name"
        searchValue = input("\nEnter last name to search by: ")
        print(book.searchBook(searchType, searchValue))
    elif selection == 3:
        searchType = "phone number"
        searchValue = input("\nEnter phone number to search by: ")
        print(book.searchBook(searchType, searchValue))
    elif selection == 4:
        searchType = "email address"
        searchValue = input("\nEnter email address to search by: ")
        print(book.searchBook(searchType, searchValue))

def clearAddressBook():
    book.clearBook()
    print("Address Book is cleared!")
    returnToMainMenu()

def returnToMainMenu():
    enterInput = input("Press enter to continue to the Main Menu...")
    if enterInput == "":
        mainMenu()
    else:
        returnToMainMenu()  



mainMenu()


