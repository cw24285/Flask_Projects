import sqlite3

conn = sqlite3.connect("Flask_Projects/dbprojekt/school_library.db")
print("Connected")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
print(cursor)

#cursor.execute("SELECT title FROM books") 
#books = cursor.fetchall() 
#print(books[0]) 

#cursor.execute("SELECT * FROM books")
#one = cursor.fetchone()
#print(one)

#wanted = input("Which genre? ")
#cursor.execute("SELECT * FROM books WHERE genre = ?", (wanted,)) 
#for book in cursor:
    #print(book["title"])

cursor.execute("""INSERT INTO books 
                  (title, author, genre, publication_year, pages, available_copies) 
                  VALUES (?, ?, ?, ?, ?, ?)""", 
               ("Aue", "Becky Manawatu", "Fiction", 2019, 344, 2))
print("Added") 
conn.commit()
    
conn.close()