# passguard.py
simple password manager

This is a Python-based password manager. This is for educational purposes only, and serves as partial-fulfilment of a requirement of LBYCPA1

# How does it work?
Passguard uses Python's built SQLite3 module for its database. SQLite3 is a lightweight, easy to use version of SQL. In order to encrypt the data, Passguard uses the cryptography module, and encrypts the database itself. It will only be accessible once the user inputs their password. 
