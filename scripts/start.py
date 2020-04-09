import sys
import os.path
from os import path
print("Checking if database exists...")
if path.exists("database.db") == False:
    from scripts import initdb
else:
    from scripts import loginScreen