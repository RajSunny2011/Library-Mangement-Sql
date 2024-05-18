# Library Management System

## Overview 
This project is a Library Management System implemented in Python using the CustomTkinter GUI library and SQLite database. **This project is intended for learning purposes and should not be used as a production system.**

### Class Overview

-   **Base Class:** `LibraryApp` extends `customtkinter.CTk`, which itself is a modified version of `tkinter.Tk`. By extending `CTk`, `LibraryApp` inherits methods and properties that allow it to function as the main window of your application.

### Properties

-   **`PATH_TO_DATA`**: A class attribute that stores the path to the SQLite database file `Library.db`. This is where all data about books and users is stored.
-   **`conn`**: An instance attribute that holds the SQLite connection object. This connection is used to execute all database operations within the application.
-   **`cur`**: Another instance attribute representing the cursor object derived from `conn`. It's used to execute SQL commands.

### Initialization (`__init__`)

The `__init__` method is the constructor of the `LibraryApp` class:

-   **Window Configuration**: It sets the title, geometry (size), and background color of the main application window.
-   **Database Connection**: Establishes a connection to the SQLite database specified by `PATH_TO_DATA`.
-   **Table Initialization**: Calls `initialize_tables` to ensure the necessary database tables exist.
-   **Admin Account Check**: Verifies if an admin account exists by invoking `admin_exists`. Depending on the result, it either prompts to create an admin account or proceeds to the login page.
-   **Main Frame Setup**: A `CTkFrame` named `main_frame` is created and packed to fill the entire application window. This frame serves as the container for all other UI elements.

### Methods

The class includes several methods that manage the UI and database interactions:

-   **`initialize_tables`**: Creates the `Books` and `Users` tables if they do not already exist. This method ensures the application has the necessary database structure to operate.
    
-   **`admin_exists` and `create_admin_account`**: These methods manage the admin account setup. `admin_exists` checks for the presence of an admin user in the database, and `create_admin_account` provides the UI for creating an admin if none exists.
    
-   **`submit_admin_password`**: Takes the entered password, hashes it using SHA-256 for security, and stores it in the database. This is a critical security feature for protecting sensitive user information.
    
-   **`login_page`, `login`, `create_account_page`, and `create_account`**: These methods handle user authentication and account management. They provide the interface for user login, validate user credentials, and manage account creation, including input validation and error handling.
    
-   **User and Admin Interfaces**: `user_page` and `admin_page` setup the UI specific to regular users and admins, respectively. They allow operations like searching for books, issuing and returning books, and additional admin capabilities like editing or deleting book records.
    
-   **Book Management**: `issue_book`, `return_book`, `add_book`, `delete_book`, and related methods manage the lifecycle of book records within the library system.Clears all widgets from the main application window, typically called before rendering a new page.

## Executing
To just run the file you need python version 3.7 or higher the customtkinter pip package. Check the version of python using:

```batch
python --version
```

You can install the package using:

```batch
pip install customtkinter
```

*or*

run the "InstallRequirements.bat" script (only on windows) if you have virtualenv package installed. You can install the package using:

```batch
pip install virtualenv
```

#### InstallRequirements.bat

A batch script to create a virtual enviroment (.env) and install all packages in the enviroment from a "requirements.txt" file in the same directory.

 - ### To Run
     - If using the virtual enviroment made from "InstallRequirements.bat", run the "RunLMS.bat" file *or* Run the folowing command in WindowsCMD from the main folder:
    ```batch
    .\.env\Scripts\python.exe .\main.py
    ```
     - If not using a virtual enviroment, run the following command:
     ```batch
     python main.py
     ```
    
#### RunLMS.bat

A batch script to run the "main.py" with the python executable in the virtual enviroment made by the "InstallRequirements.bat".

## Compiling
To complie a package is needed, here pyinstaller is used, pyinstaller would be installed if "InstallRequirements.bat" was, else run the following command in WindowsCMD:

```batch
pip install pyinstaller
```

 - ### To Comlpile:
    Run the "Compile.bat" file *or* Run the following command in WindowsCMD:
    ```batch
    pyinstaller --onefile --noconsole --icon="icon.ico" -n LMS  main.py
    ```
    The "LMS.exe" executable will be in dist folder.

#### Compile.bat
A batch script to make the executable using pyinstaller. The options usedd are:
- `--onefile`: Packages the application into a single executable file.
- `--noconsole`: Ensures the application runs without a console window (useful for GUI applications).
- `-n LMS`: Names the output executable file `LMS.exe` (on Windows).
- `--icon="icon.ico"`: changes the deafult icon to the specified one.