import sqlite3
import getpass as getpass
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