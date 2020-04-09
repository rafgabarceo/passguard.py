import getpass as pword
import sqlite3
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
    password = pword.getpass("Please enter your password: ")
    counter = counter + 1
print("Oops! You have inputted the wrong password 5 times. ")