import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import hashlib
import datetime
import sqlite3

class LibraryApp(QtWidgets.QWidget):
    PATH_TO_DATA = "Library.db"

    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect(self.PATH_TO_DATA)
        self.cur = self.conn.cursor()
        self.initialize_tables()
        self.layout = QtWidgets.QVBoxLayout(self)
        if not self.admin_exists():
            self.create_admin_account()
        else:
            self.login_page()

    def initialize_tables(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS Books (Book_ID INT, Name VARCHAR, Author VARCHAR, Availability BOOLEAN, Issuer VARCHAR, Last_Issued DATE);")
        self.cur.execute("CREATE TABLE IF NOT EXISTS Users (Username VARCHAR, Password CHARACTER(64));")
        self.conn.commit()

    def admin_exists(self):
        self.cur.execute("SELECT * FROM Users WHERE Username='Admin';")
        return bool(self.cur.fetchone())
    
    def create_admin_account(self):
        password_entry = QtWidgets.QLineEdit()
        self.layout.addWidget(password_entry)
        button = QtWidgets.QPushButton("Create")
        self.layout.addWidget(button)

    def login_page(self):
        # Clear screen if needed
        self.clear_screen()

        # Username Entry
        user_entry = QtWidgets.QLineEdit(self)
        user_entry.setPlaceholderText("Username")

        # Password Entry
        password_entry = QtWidgets.QLineEdit(self)
        password_entry.setPlaceholderText("Password")
        password_entry.setEchoMode(QtWidgets.QLineEdit.Password)  # Mask the password input

        # Login Button
        login_button = QtWidgets.QPushButton("Login", self)
        # login_button.clicked.connect(lambda: self.login(user_entry.text(), password_entry.text()))

        # Create Account Button
        create_acc_button = QtWidgets.QPushButton("Create new account", self)
        # create_acc_button.clicked.connect(self.create_account_page)

        # Layout
        # layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(user_entry)
        self.layout.addWidget(password_entry)
        self.layout.addWidget(login_button)
        self.layout.addWidget(create_acc_button)

        # self.setLayout(layout)
        self.setWindowTitle("Login Page")

    def clear_screen(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = LibraryApp()
    widget.resize(800, 500)
    widget.show()

    sys.exit(app.exec())