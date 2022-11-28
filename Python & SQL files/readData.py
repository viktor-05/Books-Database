from sqlConnect import *

def readBooks():
    #Retrieve the inserted books
    cursor.execute("""SELECT b.bookID, b.title, b.year, b.price , p.name, a.fName, a.lName, g.gName
    FROM books b, authors a, genres g
    JOIN publishers p USING(publisherID)
    JOIN write USING(authorID, bookID)
    JOIN books_genres USING(genreID, bookID)
    """) 

   
    row = cursor.fetchall() #fetct all books that was selected above
    #iterate through all the records
    print(f"{'ID':<4} {'Title':<42} {'Year':<8} {'Price':<8}  {'Publisher':<25} {'Author':<20} {'Genre'}")
    for record in row:
        print(f"{record[0]:<4} {record[1]:<42} {record[2]:<8} £{record[3]:<8} {record[4]:<25} {record[5]+' '+record[6]:<20} {record[7]}")
        print("-" * 130)


def readByPublishers():
    loop = True
    while loop:
        publisher = input("Enter the publisher name: ").title().strip()

        cursor.execute(f"""SELECT b.bookID, b.title, b.year, b.price , p.name, a.fName, a.lName
        FROM books b, authors a
        JOIN publishers p on p.publisherID = b.publisherID AND p.name = '{publisher}'
        JOIN write USING(authorID, bookID)
        """) 
            
        row = cursor.fetchall() #fetct all books that was selected above
        #iterate through all the records
        if len(row) == 0:
            print(f'There is not any record with the publisher "{publisher}".\nTry other publisher, please.')
            
        else:
            print(f"{'ID':<4} {'Title':<42} {'Year':<8} {'Price':<8}  {'Publisher':<25} {'Author':<20}")
            for record in row:
                print(f"{record[0]:<4} {record[1]:<42} {record[2]:<8} £{record[3]:<8} {record[4]:<25} {record[5]+' '+record[6]:<20}")
                print("-" * 112)
                loop = False
            


def readByGenres():
    loop = True
    while loop:
    
        genre = input("Enter the genre name: ").strip().capitalize()

        cursor.execute(f"""SELECT b.bookID, b.title, b.year, b.price , p.name, a.fName, a.lName, g.gName
        FROM books b, authors a, genres g
        JOIN publishers p USING(publisherID)
        JOIN write USING(authorID, bookID)
        JOIN books_genres bg on bg.bookID = b.bookID AND bg.genreID = g.genreID AND g.gName = '{genre}'
        """) 
        
        row = cursor.fetchall() #fetct all books that was selected above

        if len(row) == 0:
            print(f'There is not any record with the genre "{genre}".\nTry other genre, please.')
        else:
            #iterate through all the records
            print(f"{'ID':<4} {'Title':<42} {'Year':<8} {'Price':<8}  {'Publisher':<25} {'Author':<20} {'Genre'}")
            for record in row:
                print(f"{record[0]:<4} {record[1]:<42} {record[2]:<8} £{record[3]:<8} {record[4]:<25} {record[5]+' '+record[6]:<20} {record[7]}")
                print("-" * 132)
                loop = False


def readByAuthors():
    loop = True
    while loop:
        fName = input("Enter the author's first name: ").strip().capitalize()
        lName = input("Enter the author's last name ").strip().capitalize()

        cursor.execute(f"""SELECT b.bookID, b.title, b.year, b.price , p.name, a.fName, a.lName
        FROM books b, authors a
        JOIN publishers p USING(publisherID)
        JOIN write w on w.bookID = b.bookID AND w.authorID = a.authorID AND a.fName = '{fName}' AND a.lName = '{lName}'
        """) 
        
        row = cursor.fetchall() #fetct all books that was selected above

        if len(row) == 0:
            print(f'There is not any record with the author "{fName} {lName}".\nTry other author, please.')
        else:
            #iterate through all the records
            print(f"{'ID':<4} {'Title':<42} {'Year':<8} {'Price':<8}  {'Publisher':<25} {'Author':<20}")
            for record in row:
                print(f"{record[0]:<4} {record[1]:<42} {record[2]:<8} £{record[3]:<8} {record[4]:<25} {record[5]+' '+record[6]:<20}")
                print("-" * 112)
                loop = False


def readByBookName():
    
    loop = True
    while loop:
        title = input("Enter the book title: ").strip()
        
        cursor.execute(f"""SELECT b.bookID, b.title, b.year, b.price, p.name, a.fName, a.lName
        FROM books b, publishers p, authors a, write w 
        WHERE b.title = '{title}' AND b.publisherID = p.publisherID AND a.authorID = w.authorID AND b.bookID = w.bookID
        """) 
        
        row = cursor.fetchall() 

        if len(row) == 0:
            print(f'There is not any record with the book "{title}".\nTry other book, please.')
        else:
            for record in row:
                print(f"{'ID':<4} {'Title':<42} {'Year':<8} {'Price':<8}  {'Publisher':<25} {'Author':<20}")
                print(f"{record[0]:<4} {record[1]:<42} {record[2]:<8} £{record[3]:<8} {record[4]:<25} {record[5]+' '+record[6]:<20}")
                print("-" * 112)
                loop = False
       


if __name__ == "__main__":
    readBooks()
    readByPublishers()
    readByAuthors()
    readByGenres()
    readByBookName()