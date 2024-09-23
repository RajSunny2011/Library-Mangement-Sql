import sys
from PySide6 import QtGui, QtCore as QtC
from PySide6.QtWidgets import (QWidget,QGridLayout,QLineEdit,QPushButton,QApplication)
import hashlib
import datetime
import sqlite3

class LibraryApp(QWidget):
    PATH_TO_DATA = "Library.db"

    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect(self.PATH_TO_DATA)
        self.cur = self.conn.cursor()
        self.layout = QGridLayout(self)
        self.initialize_tables()
        # self.layout.setVerticalSpacing()
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
        password_entry = QLineEdit()
        self.layout.addWidget(password_entry)
        button = QPushButton("Create")
        self.layout.addWidget(button)

    def login_page(self):
        # Clear screen
        self.clear_screen()
        self.layout = QGridLayout(self)

        # Username Entry
        user_entry = QLineEdit(self)
        user_entry.setPlaceholderText("Username")

        # Password Entry
        password_entry = QLineEdit(self)
        password_entry.setPlaceholderText("Password")
        password_entry.setEchoMode(QLineEdit.Password)  # Mask the password input

        # Login Button
        login_button = QPushButton("Login")
        # login_button.clicked.connect(lambda: self.login(user_entry.text(), password_entry.text()))

        # Create Account Button
        create_acc_button = QPushButton("Create new account")
        create_acc_button.clicked.connect(self.create_account_page)

        # Layout
        self.layout.addWidget(user_entry,0,0,1,1,QtC.Qt.AlignLeft)
        self.layout.addWidget(password_entry,1,0,1,1,QtC.Qt.AlignLeft)
        self.layout.addWidget(login_button,2,0,1,1,QtC.Qt.AlignLeft)
        self.layout.addWidget(create_acc_button,3,0,1,1,QtC.Qt.AlignLeft)
        self.layout.setRowStretch(5,1)

        self.setWindowTitle("Login Page")

    def create_account_page(self):
        # Clear screen
        self.clear_screen()
        self.layout = QGridLayout(self)


        # Username Entry
        user_entry = QLineEdit(self)
        user_entry.setPlaceholderText("Username")

        # Password Entry
        password_entry = QLineEdit(self)
        password_entry.setPlaceholderText("Password (min 8 chars)")
        password_entry.setEchoMode(QLineEdit.Password)  # Mask the password input

        # Password ReEntry
        re_password_entry = QLineEdit(self)
        re_password_entry.setPlaceholderText("Confirm your Password")
        re_password_entry.setEchoMode(QLineEdit.Password)

        # Back to Login Button
        login_button = QPushButton("Back to Login")
        login_button.clicked.connect(self.login_page)

        # Create Account Button
        create_acc_button = QPushButton("Create new account")
        create_acc_button.clicked.connect(self.create_account_page)

        # Layout
        self.layout.addWidget(user_entry,0,0,1,1,QtC.Qt.AlignCenter)
        self.layout.addWidget(password_entry,1,0,1,1,QtC.Qt.AlignCenter)
        self.layout.addWidget(re_password_entry,2,0,1,1,QtC.Qt.AlignCenter)
        self.layout.addWidget(login_button,3,0,1,1,QtC.Qt.AlignCenter)
        self.layout.addWidget(create_acc_button,4,0,1,1,QtC.Qt.AlignCenter)
        self.layout.setRowStretch(5,1)

        self.setWindowTitle("Create Account Page")
    
    
    def clear_screen(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)

if __name__ == "__main__":
    app = QApplication([])

    widget = LibraryApp()
    widget.resize(800, 500)
    widget.show()

    sys.exit(app.exec())