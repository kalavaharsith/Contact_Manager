## Project Explanation: Concepts & Execution

This project demonstrates core backend development principles using Python. It serves as a practical implementation of Object-Oriented Programming (OOP) combined with persistent data storage and strict input validation.

### Core Concepts Demonstrated

* **Object-Oriented Programming (OOP):** The code is modularized into two distinct classes. The `Contact` class acts as the data model, managing individual attributes (name, phone, email). The `ContactBook` class acts as the controller, managing the list of contacts and handling all business logic (CRUD operations).
* **Persistent File Handling (I/O):** Python's built-in `open()` function is used to read and write data to `contacts.txt`. The data is formatted as comma-separated values, ensuring that records survive after the script terminates.
* **Regular Expressions (Regex):** The `re` module is used to enforce strict formatting rules. It evaluates user input against a standard email pattern to prevent invalid data entry.
* **State Management & Data Sanitization:** The application loads file data into memory (a Python list) on startup. During this process, string methods like `.strip()` and `.split(',')` are used to clean hidden newline characters and parse the text into usable variables.

### How the Code Works

1. **Initialization:** When the script runs, an instance of `ContactBook` is created. Its initialization method automatically checks if `contacts.txt` exists and loads any saved records into memory.
2. **The Command Loop:** A `while True:` loop keeps the main menu active, acting as the user interface and waiting for numerical input (1-6).
3. **Adding a Contact (Create):** The program prompts for a name, phone, and email. It uses internal `while` loops to force the user to re-enter the phone and email until they pass the validation checks (10 digits for the phone, Regex for the email). Once validated, a `Contact` object is instantiated, appended to the list, and saved to the file.
4. **Modifying Data (Read, Update, Delete):** For searching, updating, or deleting, the program iterates through the `self.contacts` list. It uses `.lower()` on both the user's search query and the stored names to ensure the search is case-insensitive. If a match is found, the contact is updated or removed, and the `save_contacts()` method is called to sync the changes to the text file.
