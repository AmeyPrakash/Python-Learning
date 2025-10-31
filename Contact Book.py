contacts = []
def add_contact():
    name = input ("Enter name: ").strip()
    number = input("Enter number: ").strip()

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact already exists.")
            return
    new_contact = {"name":name, "number":number}
    contacts.append(new_contact)
    print(f"Contact {'name'} added successfully")

def search_contact():
    query = input("Enter name or number to search: ").strip()
    found = []
    
    for contact in contacts:
        if query.lower() in contact["name"].lower() or query in contact["number"]:
            found.append(contact)

    if not found:
        print("No matching contact found.")
    else:
        print("\nSearch results: ")
        for c in found:
            print(f"Name:{c['name']} | Number: {c['number']}")

def update_contact():
    name = input("Enter the name to update: ").strip()
    for contact in contacts:
        new_number = input("Enter new number: ").strip()
        contact["number"] = new_number
        print("Contact updated successfully")
        return
    print("contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully")
            return
        else:
            print("Contact not found.")

def show_all():
    if not contacts:
        print("No contacts to show.")
    else:
        print("\nAll contacts: ")
        for contact in contacts:
            print(f"Name:{contact['name']} | Number:{contact['number']}")

while True:
    print("----CONTACT BOOK----")
    print("1. Add contact.")
    print("2. Search Contact.")
    print("3. Update Contact.")   
    print("4. Delete Contact.")
    print("5. Show All Contacts.")
    print("6. Exit")

    choice = input("Enter your choice between 1-6: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        show_all()
    elif choice == "6":
        print("Exiting.....GOODBYE")
        break
    else:
        print("Invalid choice.Please enter a number between 1 and 6.")
