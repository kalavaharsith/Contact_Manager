# ==========================================
# My Contact Book Manager
# Using Classes and File Operations in Python
# ==========================================

import os
import re


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print("\nName  :", self.name)
        print("Phone :", self.phone)
        print("Email :", self.email)

    def save_format(self):
        return f"{self.name},{self.phone},{self.email}\n"


class ContactBook:
    def __init__(self, filename="contacts.txt"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    # Load contacts from file
    def load_contacts(self):
        if os.path.exists(self.filename):

            file = open(self.filename, "r")

            for line in file:
                data = line.strip().split(",")

                if len(data) == 3:
                    name, phone, email = data
                    contact = Contact(name, phone, email)
                    self.contacts.append(contact)

            file.close()

    # Save contacts to file
    def save_contacts(self):

        file = open(self.filename, "w")

        for contact in self.contacts:
            file.write(contact.save_format())

        file.close()

    # Validate phone number
    def valid_phone(self, phone):

        if phone.isdigit() and len(phone) == 10:
            return True

        return False

    # Validate email
    def valid_email(self, email):

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            return True

        return False

    # Add contact
    def add_contact(self):

        print("\n--- Add New Contact ---")

        name = input("Enter Name : ")

        # Phone validation
        while True:

            phone = input("Enter Phone Number : ")

            if self.valid_phone(phone):
                break

            else:
                print("Phone number must contain exactly 10 digits.")

        # Email validation
        while True:

            email = input("Enter Email : ")

            if self.valid_email(email):
                break

            else:
                print("Enter a valid email address.")

        new_contact = Contact(name, phone, email)

        self.contacts.append(new_contact)

        self.save_contacts()

        print("Contact added successfully!")

    # View contacts
    def view_contacts(self):

        print("\n--- Contact List ---")

        if len(self.contacts) == 0:
            print("No contacts found.")
            return

        count = 1

        for contact in self.contacts:

            print(f"\nContact {count}")
            contact.display()

            count += 1

    # Search contact
    def search_contact(self):

        print("\n--- Search Contact ---")

        search_name = input("Enter name to search : ").lower()

        found = False

        for contact in self.contacts:

            if contact.name.lower() == search_name:

                contact.display()
                found = True
                break

        if not found:
            print("Contact not found.")

    # Update contact
    def update_contact(self):

        print("\n--- Update Contact ---")

        update_name = input("Enter name to update : ").lower()

        found = False

        for contact in self.contacts:

            if contact.name.lower() == update_name:

                print("\nEnter New Details")

                contact.name = input("New Name : ")

                # Phone validation
                while True:

                    new_phone = input("New Phone : ")

                    if self.valid_phone(new_phone):
                        contact.phone = new_phone
                        break

                    else:
                        print("Phone number must contain exactly 10 digits.")

                # Email validation
                while True:

                    new_email = input("New Email : ")

                    if self.valid_email(new_email):
                        contact.email = new_email
                        break

                    else:
                        print("Enter a valid email address.")

                self.save_contacts()

                print("Contact updated successfully!")

                found = True
                break

        if not found:
            print("Contact not found.")

    # Delete contact
    def delete_contact(self):

        print("\n--- Delete Contact ---")

        delete_name = input("Enter name to delete : ").lower()

        found = False

        for contact in self.contacts:

            if contact.name.lower() == delete_name:

                self.contacts.remove(contact)

                self.save_contacts()

                print("Contact deleted successfully!")

                found = True
                break

        if not found:
            print("Contact not found.")


# Main Function
def main():

    book = ContactBook()

    while True:

        print("\n=================================")
        print("     MY CONTACT BOOK MANAGER")
        print("=================================")

        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice : ")

        if choice == "1":
            book.add_contact()

        elif choice == "2":
            book.view_contacts()

        elif choice == "3":
            book.search_contact()

        elif choice == "4":
            book.update_contact()

        elif choice == "5":
            book.delete_contact()

        elif choice == "6":
            print("Thank you for using Contact Book Manager.")
            break

        else:
            print("Invalid choice. Please try again.")


# Run Program
main()