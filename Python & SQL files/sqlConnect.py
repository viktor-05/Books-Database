import sqlite3  

# create db if it does not exists

conn = sqlite3.connect(r"Project\Books Databse\books.db")

# cursor

cursor = conn.cursor()