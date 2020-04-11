#will contain all functions required for the program
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
passguardWelcome = "Welcome to Passguard.py!".center(100,"=")
passguard = "Passguard.py".center(100,"=")
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def initializeDatabase():
    print("Creating database")
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    print("Creating master_table table")
    c.execute("CREATE TABLE master_user_password (master_username, master_password)")
    print("Creating login table")
    c.execute("CREATE TABLE user_password (name, username, password, website)")
    print("Creating secure notes table")
    c.execute("CREATE TABLE secure_notes (title, notes)")
    conn.commit()
    conn.close()
    cls()

def initializeCrypto():
    pass

def createLoginInfo():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    master_username = input("Please enter your master username: ")
    master_password = input("Please enter your master password: ")
    master_tuple = (master_username, master_password)
    c.execute('INSERT INTO master_user_password (master_username, master_password) VALUES (?, ?)', master_tuple)
    conn.commit()
    conn.close()
    #cls()

def loginScreen():
    conn = sqlite3.connect("database.db")
    counter = 0
    c = conn.cursor()

    #Grab username and password from the master_user_password database
    c.execute("SELECT master_username FROM master_user_password")
    master_username = c.fetchone()
    c.execute("SELECT master_password FROM master_user_password")
    master_password = c.fetchone()
    conn.commit()
    conn.close()
    #Grab username and password from the master_user_password database

    # #iterate over tuple to get main element 
    for element in master_username: 
        master_username = element
    for element in master_password:
        master_password = element
    #iterate over tuple to get main element
    print()
    while counter < 5: 
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if username == master_username and password == master_password:
            break
        counter = counter + 1
        print(f"Oops! Wrong username and password. You have {5-counter} attempts left.")
    if counter == 5:
        print("Exiting program")
        os._exit(1) #exit when too many tries.
    cls()

def mainMenu():
    cls()
    print("Passguard.py - Main Menu".center(100,"="))
    checker = 0
    while checker == 0:
        x = input("What would you like to do today?\n[1] Logins\n[2] Notes\n[3] Close program\n")
        if x == '1':
            cls()
            passwordMenu()
        if x == '2':
            cls()
            print("Notes")
        if x == '3':
            cls()
            os._exit(1)

def passwordMenu():
    while True:
        print("Passguard.py - Login Info".center(100,"="))
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT name, username, website FROM user_password")
        a = c.fetchall()
        conn.commit()
        conn.close
        print(tabulate(a, headers=['name','username','website'], tablefmt='github'))
        userChoice = input("\nWhat would you like to do?\n[1] View Login Info\n[2] Add new login\n[3] Delete login\n[4] Back to main menu\n")
        if userChoice == '1':
            viewLogin()
        if userChoice == '2':
            createItem()
        if userChoice == '3':
            deleteLogin()
        if userChoice == '4':
            cls()
            break


def createItem():
    cls()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    while True: #enters while loop to continue forever the input if name keeps existing.
        new_name = input("Please enter the name of login: ")
        name_checker = new_name,
        #name checker
        c.execute('SELECT name FROM user_password WHERE name = ?', name_checker,)
        data_checker = c.fetchone() 
        if data_checker != None:
            print("Name already exists!")
            continue
        else: 
            break
    new_username = input("Please enter your username: ")
    new_password_choice = input("Would you like to generate a random password?: ")
    if new_password_choice == 'yes' or 'Yes': 
        while True:
            try:
                length = int(input("How long would you want your password to be? Please input a length: "))
            except:
                print("You did not input a valid integer!")
            else:
                break
        new_password = passwordGenerator(length) #will pass the variable length into the function. The value of the function will become the password
    else:
        new_password = input("Please input your password: ")
    new_website = input("Please entire url: ")
    new_tuple = (new_name, new_username, new_password, new_website)
    c.execute('INSERT INTO user_password (name, username, password, website) VALUES (?, ?, ?, ?)', new_tuple)
    conn.commit()
    conn.close()
    cls()
 
def passwordGenerator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(choice(characters) for x in range(length))
    print("Your password is: ", password)
    return password

def viewLogin():
    #find desired input
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    userChoice = input("Input name: "),
    cls()
    #find desired input#
    while True:
        c.execute("SELECT * FROM user_password WHERE name=?", userChoice)
        choiceList = [c.fetchone()] #saving as a list will ensure that tabulate iterates properly
        conn.commit()
        try:
            print(tabulate(choiceList, headers=['name','username','password','website url']))
        except:
            cls()
            print("Name does not exist!")
            break
        else:
            userChoice = input("\n[1] Copy username to clipboard\n[2] Copy password to clipboard\n[3] Edit name\n[4] Edit username [5] Edit password\n[6] Edit website\n[7] Exit\n")
            #storing values#
            counter = 0
            for element in choiceList: #getting the data by brute force
                for item in element:
                    if counter == 0:
                        name = item
                        counter += 1
                        continue
                    if counter == 1:
                        username = item
                        counter += 1
                        continue
                    if counter == 2:
                        password = item
                        counter += 1
                        continue
                    if counter == 3:
                        website = item
                        counter += 1
                        continue
            if userChoice == '1':
                print("Copying username to clipboard...")
                pyperclip.copy(username)
                cls()
            if userChoice == '2':
                print("Copying password to clipboard")
                pyperclip.copy(password)
                print("Copied!")
                cls()
            if userChoice == '3':
                editInfo = input("Enter edit: ")
                tuple_edit = (editInfo, name)
                cls()
                continue
            if userChoice == '4':
                editInfo = input("Enter edit: ")
                tuple_edit = (editInfo, username)
                c.execute("UPDATE user_password SET username = ? WHERE username = ?", tuple_edit)
                conn.commit()
                cls() 
                continue
            if userChoice == '5':
                new_password_choice = input("Would you like to generate a random password?: ")
                if new_password_choice == 'yes' or 'Yes': 
                    while True:
                        try:
                            length = int(input("How long would you want your password to be? Please input a length: "))
                        except:
                            print("You did not input a valid integer!")
                        else:
                            break
                    editInfo = passwordGenerator(length)
                else: 
                    editInfo = input("Enter edit: ")
                tuple_edit = (editInfo, name)
                c.execute("UPDATE user_password SET password = ? WHERE name = ?", tuple_edit)
                conn.commit()
                userChoice = editInfo,
                cls()
                continue
            if userChoice == '6':
                editInfo = input("Enter edit: ")
                tuple_edit = (editInfo, name)
                c.execute("UPDATE user_password SET name = ? WHERE name = ?", tuple_edit)
                conn.commit()
                cls()
            if userChoice == '7':
                cls()
                break

def editLogin():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    userEntry = input("Enter the name of the entry to edit")
    userChoice = input("What do you want to edit?: ")
    userAppend = input("What do you want to edit it to?: ")
    userFinal = userChoice, userAppend, userEntry,
    c.executemany("UPDATE user_password SET ? = ? WHERE name = ?",userFinal)
    a = c.fetchone()
    print("Updating!")

def deleteLogin():
    while True:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        userEntry = input("Please input the name you want to delete: ")
        userEntryChecker = userEntry,
        c.execute("SELECT name FROM user_password WHERE name = ?", userEntryChecker)
        fetcher = c.fetchone()
        if fetcher == None:
            print("Does not exist! Please enter a valid name")
            continue
        userVeri = input("Please input the name of entry again. Remember, you cannot undo this!\n")
        if userEntry == userVeri:
            userEntry = userEntry,
            c.execute("DELETE FROM user_password WHERE name = ?", userEntry)
            conn.commit()
            conn.close()
            cls()
            break
        else:
            failSafe = input("Not the same! If you don't want to continue, please type: exit\n")
            failSafe.lower
            if failSafe == 'exit':
                cls()
                break
            else:
                continue

def notesMenu():
    pass



