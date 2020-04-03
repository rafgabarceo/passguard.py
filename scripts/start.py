import sys
import os.path
from os import path
print("Checking if database exists...")
if path.exists("database.db") == False:
    import initdb
else:
    import loginScreen