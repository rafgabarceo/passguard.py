import sqlite3

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

from scripts import loginScreen
loginScreen