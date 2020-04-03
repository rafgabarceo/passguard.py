#will contain all functions required for the program
import sqlite3
import getpass as getpass
import time
import sys
import os.path
from tabulate import tabulate
from os import path
import pyperclip
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
    checker = 0
    while checker == 0:
        x = input("What would you like to do today?\n[1] Logins\n[2] Notes\n[3] Close program\n")
        if x == '1':
            passwordMenu()
        if x == '2':
            print("Notes")
        if x == '3':
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
        print(a)
        print(tabulate(a, headers=['name','username','website'], tablefmt='github'))
        userChoice = input("\nWhat would you like to do?\n[1] View Login Info\n[2] Add new login\n[3] Edit login\n[4] Delete login\n[5] Exit\n")
        if userChoice == '1':
            viewLogin()
        if userChoice == '2':
            createItem()
        if userChoice == '3':
            deleteLogin()
        if userChoice == '4':
            deleteLogin()
        if userChoice == '5':
            break


def createItem():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    new_name = input("Please enter the name of login: ")
    new_username = input("Please enter your username: ")
    new_password = input("Please enter your password: ")
    new_website = input("Please entire url: ")
    new_tuple = (new_name, new_username, new_password, new_website)
    c.execute('INSERT INTO user_password (name, username, password, website) VALUES (?, ?, ?, ?)', new_tuple)
    conn.commit()
    conn.close()

def viewLogin():
    #find desired input
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    userChoice = input("Input name: "),
    cls()
    c.execute("SELECT * FROM user_password WHERE name=?", userChoice)
    choiceList = [c.fetchone()] #saving as a list will ensure that tabulate iterates properly
    choiceCopy = c.fetchone()
    conn.commit()
    conn.close()
    #find desired input
    print(tabulate(choiceList, headers=['name','username','password','website url']))
    userChoice = input("\n[1] Copy username to clipboard\n[2] Copy password to clipboard\n[3] Exit without doing anything\n")
    if userChoice == 1:
        pyperclip.copy(choiceCopy.index(1))
def editLogin():
    pass

def deleteLogin():
    pass

def notesMenu():
    pass




