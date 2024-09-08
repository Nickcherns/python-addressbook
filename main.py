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

def main_menu():
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
    select_main_menu()
    
def select_main_menu():
    selection = input("Enter a number to continue... ")

    
    
    
    
    
    
    if selection == "1": # 1. Add an Entry [WORKS]
        print("DEBUG: Selection = 1")
        add_entry_to_book()
    elif selection == "2": # 2. Remove an Entry
        print("DEBUG: Selection = 2")
    elif selection == "3": # 3. Search for an Entry
        print("DEBUG: Selection = 3")
        search_address_book()
    elif selection == "4": # 4. Print the Address Book [WORKS + DEBUG CHECK]
        print("DEBUG: Selection = 4")
        print_address_book()
    elif selection == "5": # 5. Clear Address Book [WORKS - book needs clarification when empty]
        print("DEBUG: Selection = 5")
        clear_address_book()
    elif selection == "6": # 6. Quit [WORKS]
        print("DEBUG: Selection = 6")
        exit(1)
    else:
        print("Selection not found...")
        select_main_menu()

def add_entry_to_book():
    print("\n\nEnter information to add entry to Address Book")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    phone_number = input("Phone Number: ")
    email_address = input("Email Address: ")
    new_entry = {
        "First Name: " : first_name,
        "Last Name: " : last_name,
        "Phone Number: " : phone_number,
        "Email Address: " : email_address
    }
    book.add_entry(new_entry)
    print("Entry Added!")
    return_to_main_menu()

def print_address_book():
    book.print_book(book.book)
    print(book.debug_print_raw_book())
    return_to_main_menu()

def search_address_book():
    print("\nSelect your search type....")
    print("1. Name")
    print("2. Phone Number")
    print("3. Email Address")
    selection = input("Input your selection: ")
    if selection == "1":
        search_type = "name"
        search_value = input("\nEnter first name to search by: ")
        book.search_book(search_type, search_value)
    elif selection == "2":
        search_type = "number"
        search_value = input("\nEnter phone number to search by: ")
        book.search_book(search_type, search_value)
    elif selection == "3":
        search_type = "email"
        search_value = input("\nEnter email address to search by: ")
        book.search_book(search_type, search_value)
    print("Address Book searched...")
    return_to_main_menu()

def clear_address_book():
    book.clear_book()
    print("Address Book is cleared!")
    return_to_main_menu()

def return_to_main_menu():
    enter_input = input("Press enter to continue to the Main Menu...")
    if enter_input == "":
        main_menu()
    else:
        return_to_main_menu()



main_menu()


