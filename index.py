from scripts.scripts import *

print("Checking if database exists...")
if path.exists("database.db") == False:
    print("Database does not exist!")
    initializeDatabase()
    createLoginInfo()
    loginScreen() 
    mainMenu()

loginScreen()
while True:
    mainMenu()