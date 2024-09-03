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
        for i in dict:
            for key, value in dict[i].items():
                print(key, value)
            print("---------------------------")

    def addEntry(self, newEntry):
        bookCount = self.countBook()
        self.book.update({("Entry" + str(bookCount + 1)), newEntry})

    def countBook(self):
        bookList = len(self.book)
        return bookList
    
    def debugPrintRawBook(self):
        print(self.book)


