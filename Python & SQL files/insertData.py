from sqlConnect import *
import time

from readData import *


def addBooks():

    # create ad empty list
    books = []

    title = input("Enter the book title: ").strip()
    books.append(title)
    year = int(input("Enter the year of the book publication: ").strip())
    books.append(year)
    price = float(input("Enter the price: ").strip())
    books.append(price)

    # print("To enter the publisher check the table below.\nIf you find it, enter the ID, if not, add a new publisher record.")
    # time.sleep(2)
    # readPublishers()
    # check = input("Press 1 to enter the ID or 2 to add new publisher: ")
    # if check == "1":
    #     pubID = int(input("Enter the publisher ID: "))
    #     books.append(pubID)
    # elif check == "2":
    #     pubName = input("Enter the publisher name: ")
    #     publisher.append(pubName)
    #     cursor.execute("INSERT INTO publishers VALUES(NULL, ?)", publisher)
    #     cursor.execute("SELECT bookID FROM books ORDER BY bookID DESC LIMIT 1")
    #     row = cursor.fetchone()
    #     books.append(row[0])

    #add the publisher ID or insert new if doesn't exist
    pubName = input("Enter the publisher name: ").strip().title()
    cursor.execute(f"SELECT * FROM publishers WHERE name = '{pubName}'")
    row = cursor.fetchone()
    if row is None:
        cursor.execute("INSERT INTO publishers VALUES(NULL, ?)", (pubName,))
        books.append(cursor.lastrowid)
    else:
        books.append(row[0])

    cursor.execute(f"INSERT INTO books VALUES(NULL, ?, ?,?, ?)", books) 
    lastBookID = cursor.lastrowid
        
    #add an author to the book or create new if doesn't exist
    fName = input("Enter the author first name: ").strip().capitalize()
    lName = input("Enter the author last name: ").strip().capitalize()
    cursor.execute(f"SELECT * FROM authors WHERE fName = '{fName}' AND lName = '{lName}'")
    row = cursor.fetchone()
    if row is None:
        cursor.execute("INSERT INTO authors VALUES(NULL, ?, ?)", (fName, lName))
        cursor.execute("INSERT INTO write VALUES(?, ?)", (cursor.lastrowid, lastBookID))
    else:
        cursor.execute("INSERT INTO write VALUES(?, ?)", (row[0], lastBookID))

     #add a genre to the book or create new if doesn't exist
    loop = True
    while loop:
        genre = input("Enter the genre name: ").strip().capitalize()
        cursor.execute(f"SELECT * FROM genres WHERE gName = '{genre}'")
        row = cursor.fetchone()
        if row is None:
            cursor.execute("INSERT INTO genres VALUES(NULL, ?)", (genre,))
            cursor.execute("INSERT INTO books_genres VALUES(?, ?)", (cursor.lastrowid, lastBookID))
        else:
            cursor.execute("INSERT INTO books_genres VALUES(?, ?)", (row[0], lastBookID))
        while True:
            addMore = input("Do you want to add another genre to the book Y/N? ").strip().upper()
            if  addMore == "Y":
                continue
            elif addMore == "N":
                loop = False
                break
            else:
                print(f'The answer "{addMore}" is not valid, please enter "Y" or "N".')
    
    print (f'Title" {title}" added to books tables')
    time.sleep(2)

    cursor.execute("""SELECT b.bookID, b.title, b.year, b.price , p.name, a.fName, a.lName, g.gName
    FROM books b, authors a, genres g
    JOIN publishers p USING(publisherID)
    JOIN write USING(authorID, bookID)
    JOIN books_genres USING(genreID, bookID)
    """) 

    print(cursor.fetchall()[-1])

    conn.commit() #save changes permanently  



if __name__ == "__main__":
    addBooks()