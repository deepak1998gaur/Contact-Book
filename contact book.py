import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = json.load(file)
        return contacts
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts, name, phone, email):
    contact = {"Name": name, "Phone": phone, "Email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['Name']} - {contact['Phone']} - {contact['Email']}")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(contacts, name, phone, email)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
