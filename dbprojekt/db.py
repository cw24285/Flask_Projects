import sqlite3

conn = sqlite3.connect("Flask_Projects/dbprojekt/school_library.db")
print("Connected")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
print(cursor)

def add_book(conn): 
    title = input("Title: ") 
    author = input("Author: ") 
    genre = input("Genre: ") 
    year = int(input("Year published: ")) 
    pages = int(input("Pages: ")) 
    copies = int(input("Copies: ")) 

    cursor.execute("""INSERT INTO books
                    (title, author, genre, publication_year,
                     pages, available_copies)
                    VALUES (?,?,?,?,?,?)""",
                    (title, author, genre, year, pages, copies))
    print("Added") 
    print(cursor.lastrowid)

def get_all_book_titles():
    cursor.execute("SELECT * FROM books")
    for book in cursor:
        print(book["title"])

while True:

    makebook = input("Do you want to add a new book? y/n uwu")
    if makebook == "y":
        add_book(conn)
        get_all_book_titles()
    elif makebook == "n":
        break
    else:
        print("Not a real command.")

conn.commit()
    
conn.close()