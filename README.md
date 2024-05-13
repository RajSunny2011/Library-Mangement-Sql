# Library Management System

## Overview 
This project is a Library Management System implemented in Python using the CustomTkinter GUI library and SQLite database. **This project is intended for learning purposes and should not be used as a production system.**

> ### `__init__`
> 
> This function initializes the LibraryApp class instance. It sets up the main window properties, establishes a connection to the SQLite database, checks if the admin exists, and decides whether to display the login or admin account creation interface.
> 
> ### `initialize_tables`
> 
> Sets up the database tables if they do not exist already. This includes creating tables for `Books` and `Users` with appropriate fields.
> 
> ### `admin_exists`
> 
> Checks the database to see if an admin user exists by querying the `Users` table. Returns `True` if an admin is found, `False` otherwise.
> 
> ### `create_admin_account`
> 
> Prompts the user to create an admin account if none exists. It sets up the interface elements for entering and submitting the admin password.
> 
> ### `submit_admin_password`
> 
> Processes the admin password, hashes it, and stores it in the database. It then calls the `login_page` function to transition to the login interface.
> 
> ### `login_page`
> 
> Sets up the login interface where users can enter their username and password. It also provides a button to navigate to the account creation page.
> 
> ### `login`
> 
> Verifies the user credentials against the database. If successful, transitions the user to either the admin or regular user interface depending on their role.
> 
> ### `create_account_page`
> 
> Displays the interface for creating a new user account, including fields for username, password, and password confirmation.
> 
> ### `create_account`
> 
> Processes the new account creation by checking input validity, hashing the password, and storing the new user details in the database. Returns to the login page on success.
> 
> ### `build_table`
> 
> Configures and returns a styled ttk Treeview widget that displays the list of books. It sets up the table structure and styles.
> 
> ### `populate_table`
> 
> Fetches and displays the book records in the Treeview table. It can optionally filter books based on a search keyword.
> 
> ### `user_page`
> 
> Builds the user interface for regular users, featuring the book table and options to search for books and logout.
> 
> ### `issue_book`
> 
> Handles the book issuing process. Checks book availability and updates the database record to mark the book as issued to the current user.
> 
> ### `admin_page`
> 
> Sets up the admin interface with additional management options like editing, deleting, and adding books.
> 
> ### `delete_book`
> 
> Allows the admin to delete a selected book from the database.
> 
> ### `modify_book_window`
> 
> Displays a popup window for editing the details of a selected book.
> 
> ### `modify_book`
> 
> Updates the book details in the database based on the input from the `modify_book_window`.
> 
> ### `add_book_window`
> 
> Displays a popup window for adding a new book to the database.
> 
> ### `add_book`
> 
> Processes adding a new book to the database, ensuring there are no duplicates, and commits the details to the database.
> 
> ### `return_book`
> 
> Handles the process of returning a book, updating its status in the database as available and clearing the issuer field.
> 
> ### `clear_screen`
> 
> Clears all widgets from the main application window, typically called before rendering a new page.
