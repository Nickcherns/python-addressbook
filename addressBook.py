class AddressBook:

    
    def __init__(self):
        self.name = "Address Book"
        self.book = {
            "entry1" : { 
                "First Name:" :"John",
                "Last Name:" : "Smith",
                "Phone Number:" : 1234567890,
                "emailAddress:" : "jSmith@aol.com"
            },
            "entry2" : {
                "First Name:" : "Jane",
                "Last Name:" : "Smith",
                "Phone Number:" : 9870546842,
                "Email Address:" : "JaneSmith@aol.com"
            },
        }

    def printBook(self, dict):
        print("\n\n---------------------------")
        print("-------" + self.name + "--------")
        print("---------------------------")
        for entry in dict:
            for key, value in dict[entry].items():
                print(key, value)
            print("---------------------------")

    def addEntry(self, newEntry):
        bookCount = self.countBook()
        userEntry = {("Entry" + str(bookCount + 1)): newEntry}
        self.book.update(userEntry)

    def countBook(self):
        bookList = len(self.book)
        return bookList
    
    def clearBook(self):
        for i in self.book.copy():
            del self.book[i]

    def searchBook(self, searchType, searchValue):
        # open dictionary to nested dictionary
        # match search type with nested dict key
        #   for each key in each nested dict
        #       if searchValue == nested dict value
        #           display found entry
        searchValue = searchValue.lower()
        for entry in self.book:
            for key, value in self.book[entry].items:
                lowerCaseKey = key.lower()
                if searchType in lowerCaseKey:
                    if searchValue in value:
                        return self.book[entry]
                # if searchType == "first name":
                #     pass
                # elif searchType == "last name":
                #     pass
                # elif searchType == "phone number":
                #     pass
                # elif searchType == "email address":
                #     pass
    
    def debugPrintRawBook(self):
        print(self.book.keys())
        for i in self.book:
            print(self.book[i])


