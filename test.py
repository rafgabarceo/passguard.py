import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("SELECT master_username FROM master_user_password")
master_username = c.fetchone()
c.execute("SELECT master_password FROM master_user_password")
master_password = c.fetchone()
conn.commit()
conn.close()

for i in master_username:
    master_username = i
print(master_username)

