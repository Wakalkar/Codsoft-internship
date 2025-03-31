# Contact Book Application

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        """Add a new contact to the contact book."""
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()

        if name in self.contacts:
            print("Contact with this name already exists!")
        else:
            self.contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            print(f"Contact '{name}' added successfully!")

    def view_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\n--- Contact List ---")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}")
            print("--------------------\n")

    def search_contact(self):
        """Search for a contact by name or phone number."""
        search_query = input("Enter name or phone number to search: ").strip()
        found = False

        for name, details in self.contacts.items():
            if search_query.lower() in name.lower() or search_query == details['phone']:
                print("\n--- Contact Found ---")
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                print("--------------------\n")
                found = True
                break

        if not found:
            print("No contact found with the given name or phone number.")

    def update_contact(self):
        """Update details of an existing contact."""
        name = input("Enter the name of the contact to update: ").strip()
        if name in self.contacts:
            print("\nCurrent Details:")
            print(f"Phone: {self.contacts[name]['phone']}")
            print(f"Email: {self.contacts[name]['email']}")
            print(f"Address: {self.contacts[name]['address']}")
            print("\nEnter new details (leave blank to keep unchanged):")

            phone = input("New phone number: ").strip()
            email = input("New email: ").strip()
            address = input("New address: ").strip()

            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address

            print(f"Contact '{name}' updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self):
        """Delete a contact from the contact book."""
        name = input("Enter the name of the contact to delete: ").strip()
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Contact not found!")

    def main_menu(self):
        """Display the main menu for user interaction."""
        while True:
            print("\n--- Contact Book ---")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.main_menu()
