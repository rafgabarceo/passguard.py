    
import sqlite3
import getpass as getpass
import time
import sys
import os.path
from tabulate import tabulate
from os import path
import pyperclip
import string
from random import *


def viewLogin():
    while True:
        #find desired input
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        userChoice = input("Input name: "),
        #cls()
        c.execute("SELECT * FROM user_password WHERE name=?", userChoice)
        choiceList = [c.fetchone()] #saving as a list will ensure that tabulate iterates properly
        conn.commit()
        conn.close()
        #find desired input
        print(tabulate(choiceList, headers=['name','username','password','website url']))
        userChoice = input("\n[1] Copy username to clipboard\n[2] Copy password to clipboard\n[3] Edit name\n[4] Edit password\n[5] Edit website\n[6] Exit\n")
        if userChoice == '1':
            counter = 0
            for element in choiceList:
                for item in element: #brute force; will get the 2nd index in the tuple
                    counter += 1
                    if counter == 2:
                        print(f"Copying username to clipboard...")
                        pyperclip.copy(item)
                        print("Copied!")
                        #cls()
                        break
        if userChoice == '2':
            counter = 0 #initialize counter
            for element in choiceList:
                for item in element: #brute force; will get the 3rd index in the tuple
                    counter += 1
                    if counter == 3:
                        print(f"Copying password to clipboard...")
                        pyperclip.copy(item)
                        print("Copied!")
                       # cls()
                        break
        if userChoice == '3':
            editInfo = input("Enter edit: ")
            counter = 0
            for element in choiceList:
                for item in element:
                    counter += 1
                    if counter == 1:
                        return item
            tuple_edit = (item, editInfo, userChoice)
            c.executemany("UPDATE user_password SET name = ? WHERE name = ?", tuple_edit)
            conn.commit()
            conn.close()
        if userChoice == '4':
            pass 
        if userChoice == '5':
            pass
        if userChoice == '6':
            pass
        if userChoice == '7':
            break

viewLogin()