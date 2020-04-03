#will contain all functions required for the program
import sqlite3
import getpass as getpass
import time
import sys
import os.path
from os import path

def initializeDatabase():
    print("Creating database")
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    print("Creating master_table table")
    c.execute("CREATE TABLE master_user_password (master_username, master_password)")
    print("Creating login table")
    c.execute("CREATE TABLE user_password (username, password, website)")
    print("Creating secure notes table")

    conn.commit()
    conn.close()

def createLoginInfo():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    master_username = input("Please enter your master username: ")
    master_password = getpass.getpass("Please enter your master password: ")
    print(master_password)
    master_tuple = (master_username, master_password)
    print(master_tuple)
    c.execute('SELECT * FROM master_user_password')
    c.execute('INSERT into master_user_password VALUES (?, ?)', master_tuple)
    a = c.fetchone()
    print(a)

    conn.commit()
    conn.close()
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

    print("Welcome to Passguard.py!".center(100,"="))
    while counter < 5: 
        username = input("Please enter your username: ")
        password = getpass.getpass("Please enter your password: ")
        counter = counter + 1
    print("Oops! You have inputted the wrong password 5 times. ")