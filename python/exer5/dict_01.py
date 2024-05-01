# exercize 4 1st question


phone_book = {}

def add_entry(name, number):
    phone_book[name] = number
    print(f"Added entry: {name} - {number}")

def search_entry(name):
    if name in phone_book: 
        print(f"Number for {name}: {phone_book[name]}")
    else:
        print(f"{name} not found in the phone book")

def sort_phone_book():
    sorted_phone_book = sorted(phone_book.items(), key=lambda x: x[0])
    print("Sorted phone book:")
    for name, number in sorted_phone_book:
        print(f"{name}: {number}")

def delete_entry(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Deleted entry: {name}")
    else:
        print(f"{name} not found in the phone book")

def view_phone_book():
    print("Phone Book Entries:")
    for name, number in phone_book.items():
        print(f"{name}: {number}")

# Main loop to perform operations
while True:
    print("\nPhone Book Operations:")
    print("1. Add entry")
    print("2. Search entry")
    print("3. Sort phone book")
    print("4. Delete entry")
    print("5. View entire phone book")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_entry(name, number)
    elif choice == '2':
        name = input("Enter name to search: ")
        search_entry(name)
    elif choice == '3':
        sort_phone_book()
    elif choice == '4':
        name = input("Enter name to delete: ")
        delete_entry(name)
    elif choice == '5':
        view_phone_book()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
