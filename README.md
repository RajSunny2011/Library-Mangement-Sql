# Library Management System

This project is a Library Management System implemented in Python using CustomTkinter GUI library and SQLite database for data storage. This system allows librarians to efficiently manage books, users, issues and returns of books.

### Class Overview

-   **Base Class:** `LibraryApp` extends `customtkinter.CTk`, which itself is a modified version of `tkinter.Tk`.

#### Attributes:

-   **`PATH_TO_DATA`**: A class attribute that stores the path to SQLite database file named Library.db.
-   **`conn`**: An instance attribute representing a connection object used for executing all SQL queries and commands within the app.
-   **`cur`**: Another instance attribute which serves as cursor derived from self.conn. It's responsible for fetching records or results.

#### Methods:

##### Initialization:

-   **Window Configuration**: It sets the title, geometry (size), and background color of the main application window.
-   **Database Connection**: Establishes a connection to the SQLite database specified by `PATH_TO_DATA`.
-   **Table Initialization**: Calls `initialize_tables` to ensure the necessary database tables exist.
-   **Admin Account Check**: Verifies if an admin account exists by invoking `admin_exists`. Depending on the result, it either prompts to create an admin account or proceeds to the login page.
-   **Main Frame Setup**: A `CTkFrame` named `main_frame` is created and packed to fill the entire application window. This frame serves as the container for all other UI elements.

##### **Create and Manage Tables**
- **`initialize_tables`** method creates the `Books` and `Users` tables if they do not already exist. This method ensures the application has the necessary database structure to operate.
- **`build_table`** method creates the table (treeview) widget with special styling to match customTkinter's styling.
- **`populate_table`** method fills the table widget with the data in the `Books` table.
##### **Admin Account Management**:
- **`admin_exists` and `create_admin_account`** methods manage the admin account setup. `admin_exists` checks for the presence of an admin user in the database, and `create_admin_account` method provides the UI for creating an admin if none exists.
- **`submit_admin_password`** method takes the entered password, hashes it using SHA-256 for security, and stores it in the database. This is a critical security feature for protecting sensitive user information.


##### **Authentication and Account Management**:
- **`login_page`, `login`, `create_account_page`, and `create_account`** methods handle user authentication and account management. They provide the interface for user login, validate user credentials, and manage account creation, including input validation and error handling.

##### **User and Admin Interfaces**:
- **`user_page`** and **`admin_page`** methods setup the UI specific to regular users and admins, respectively. They allow operations like searching for books, issuing and returning books, and additional admin capabilities like editing or deleting book records.
    
##### **Book Management**:
- **`issue_book`**, **`return_book`**, **`add_book`**, and **`delete_book`** methods manage the lifecycle of book records within the library system.Clears all widgets from the main application window, typically called before rendering a new page.

## Getting Started
To get started with this project:

- Make sure you have Python 3.x installed on your computer.
- Install the customtkinter and SQLite packages using pip.
- Download or copy files from this repository into a folder.
- Open terminal (Windows Command Prompt) navigate to that directory where you have placed these files.
- Run the command: python main.py. This will start your library management system, without creating an executable.

You can compile this python script into standalone executable using PyInstaller with following command:

```
pyinstaller --onefile --noconsole -n LMS.exe main.py
```