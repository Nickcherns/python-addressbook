class AddressBook:

    
    def __init__(self):
        self.name = "Address Book"
        self.book = {
            "entry1" : { 
                "First Name:" :"John",
                "Last Name:" : "Smith",
                "Phone Number:" : "1234567890",
                "emailAddress:" : "jSmith@aol.com"
            },
            "entry2" : {
                "First Name:" : "Jane",
                "Last Name:" : "Smith",
                "Phone Number:" : "9870536842",
                "Email Address:" : "JaneSmith@aol.com"
            },
            "entry3" : {
                "First Name:" : "Timothy",
                "Last Name:" : "Nickles",
                "Phone Number:" : "4959483847",
                "Email Address:" : "nickleTim@gmail.com"
            },
            "entry4": {
                "First Name:": "Brad",
                "Last Name:": "Louis",
                "Phone Number:": "8231905583",
                "Email Address:": "blouy@hotmail.com"
            },
            "entry5": {
                "First Name:": "Peter",
                "Last Name:": "Love",
                "Phone Number:": "2978590123",
                "Email Address:": "plove@gmail.com"
            },
            "entry6": {
                "First Name:": "Hubert",
                "Last Name:": "Frank",
                "Phone Number:": "1039458394",
                "Email Address:": "hubertser@aol.com"
            },
            "entry7": {
                "First Name:": "Keith",
                "Last Name:": "Teradello",
                "Phone Number:": "9234859348",
                "Email Address:": "tdello@yahoo.com"
            },
            "entry8": {
                "First Name:": "Geoff",
                "Last Name:": "Clark",
                "Phone Number:": "9380249287",
                "Email Address:": "gclark@gmail.com"
            },
            "entry9": {
                "First Name:": "Test",
                "Last Name:": "Test",
                "Phone Number:": "0000000000",
                "Email Address:": "test@test.com"
            },

        }

    def print_book(self, dict):
        print("\n---------------------------")
        print("------ " + self.name + " -------")
        print("---------------------------")
        if len(self.book) == 0:
            print("  ** NO ENTRIES FOUND **")
        for entry in dict:
            for key, value in dict[entry].items():
                print(key, value)
            print("---------------------------")

    def add_entry(self, new_entry):
        book_count = self.count_book()
        user_entry = {("Entry" + str(book_count + 1)): new_entry}
        self.book.update(user_entry)

    def count_book(self):
        book_list = len(self.book)
        return book_list
    
    def clear_book(self):
        for i in self.book.copy():
            del self.book[i]

    def remove_entry(self, entry_name):
        del self.book[entry_name]
        print("Entry Removed...")

    def return_entry_by_email(self, email_address):
        email_address = email_address.lower()
        found_entry = []
        entry_name = ""
        for entry in self.book:
            for key, value in self.book[entry].items():
                key = key.lower()
                value = value.lower()
                if "email" not in key:
                    continue
                if email_address in value:
                    found_entry.append(self.book[entry])
                    entry_name = entry
        if len(found_entry) > 1:
            return "Too many entries found..."
        else:
            print("---------------------------")
            print("------- Entry Found -------")
            print("---------------------------")
            for key, value in found_entry[0].items():
                print(key, value)
            print("---------------------------")
            return entry_name

    def search_book(self, search_type, search_value):
        print("---------------------------")
        # print("DEBUG: Searching Book...")
        print("---------------------------")
        search_value = str(search_value).lower()
        found_entries = []
        # iterate over each entry in book
        for entry in self.book:
            if self.book[entry] in found_entries:
                break
            # iterate over each entry items in book
            for key, value in self.book[entry].items():
                key = key.lower()
                value = value.lower()
                # if search_type doesn't match key, move to next iteration
                if search_type not in key:
                    continue
                # if search_value matches value, add entry to found_entries
                if search_value in value:
                    found_entries.append(self.book[entry])
                    break
        # if found_entries has at least 1 entry, print entry
        if len(found_entries) >= 1:
            for entry in found_entries:
                for key, value in entry.items():
                    print(key, value)
                print("---------------------------")
                
    def debug_print_raw_book(self):
        print(self.book.keys())
        # for i in self.book:
        #     print(self.book[i])


