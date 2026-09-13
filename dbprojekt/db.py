import sqlite3

conn = sqlite3.connect("Flask_Projects/dbprojekt/school_library.db")
print("Connected")

cursor = conn.cursor()
print(cursor)

cursor.execute("SELECT * FROM books") 
books = cursor.fetchall() 
print(books[0]) 

conn.close()