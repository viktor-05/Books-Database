from sqlConnect import *
import time

def updateBook():
    cursor.execute("SELECT * FROM books")
    record = cursor.fetchall()
    for row in record:
        print(row)
    
    idField = input("Enter the bookID of the book to be updated: ")

    fieldName = input("Which field do you like to update(Title, Year, Price): ").capitalize()
    if fieldName == "Title":
        newFieldValue = input(f"Enter the new value for the field {fieldName}: ").strip()
        print(f"The new field value entered is {newFieldValue}")
        newFieldValue = f"'{newFieldValue}'"
    elif fieldName == "Year":
        newFieldValue = int(input(f"Enter the new value for the field {fieldName}: ").strip())
        print(f"The new field value entered is {newFieldValue}")
    elif fieldName == "Price":
        newFieldValue = float(input(f"Enter the new value for the field {fieldName}: ").strip())
        print(f"The new field value entered is {newFieldValue}")

    #Update the table

    cursor.execute(f"UPDATE books SET {fieldName} = {newFieldValue} WHERE bookID = {idField}")

    conn.commit()

    print(f"record {idField} updated in the books table")
    time.sleep(2)

    cursor.execute(f"""SELECT b.bookID, b.title, b.year, b.price, p.name, a.fName, a.lName
    FROM books b, publishers p, authors a, write w 
    WHERE b.bookID = '{idField}' AND b.publisherID = p.publisherID AND a.authorID = w.authorID AND b.bookID = w.bookID
    """) 
    
    record = cursor.fetchone() #fetct all books that was selected above

    #iterate through all the records
    print(f"{'ID':<4} {'Title':<30} {'Year':<8} {'Price':<8}  {'Publisher':<25} {'Author':<20}")
    print(f"{record[0]:<4} {record[1]:<30} {record[2]:<8} £{record[3]:<8} {record[4]:<25} {record[5]+' '+record[6]:<20}")
    print("-" * 100)


def updatePublisher():
    cursor.execute("SELECT * FROM publishers")
    record = cursor.fetchall()
    for row in record:
        print(row)
    idField = input("Enter the pulisherID of the publisher to be updated: ")

    newFieldValue = input(f"Enter the new publisher name: ").strip()
    
    #Update the table
    cursor.execute(f"UPDATE publishers SET name = '{newFieldValue}' WHERE publisherID = {idField}")

    conn.commit()

    #returns the id of the song to be updated
    print(f"record {idField} updated in the publishers table")
    time.sleep(2)

    cursor.execute(f"SELECT * FROM publishers WHERE publisherID = '{idField}' ") 
    
    record = cursor.fetchone() #fetch the updated publisher

    #iterate through all the records
    print(f"{'ID':<4} {'Publisher':<25}")
    print(f"{record[0]:<4} {record[1]:<25} ")

def updateAuthor():
    cursor.execute("SELECT * FROM authors")
    record = cursor.fetchall()
    for row in record:
        print(row)
    idField = input("Enter the authorID of the author to be updated: ")

    newFieldValue = input(f"Enter the new author's first name: ").strip()
    newFieldValue1 = input(f"Enter the new author's last name: ").strip()
    
    #Update the table
    cursor.execute(f"UPDATE authors SET fName = '{newFieldValue}', lName = '{newFieldValue1}' Where authorID = {idField}")

    conn.commit()

    #returns the id of the song to be updated
    print(f"record {idField} updated in the authors table")
    time.sleep(2)

    cursor.execute(f"SELECT * FROM authors WHERE authorID = '{idField}' ") 
    
    record = cursor.fetchone() #fetch the updated publisher

    #iterate through all the records
    print(f"{'ID':<4} {'Author':<20}")
    print(f"{record[0]:<4} {record[1]+' '+record[2]:<20} ")

def updateGenre():
    cursor.execute("SELECT * FROM genres")
    record = cursor.fetchall()
    for row in record:
        print(row)
    idField = input("Enter the genresID of the genres to be updated: ")

    newFieldValue = input(f"Enter the new genre name: ").strip().capitalize()
    
    #Update the table
    cursor.execute(f"UPDATE genres SET gName = '{newFieldValue}' WHERE genreID = {idField}")

    conn.commit()

    #returns the id of the song to be updated
    print(f"record {idField} updated in the genres table")
    time.sleep(2)

    cursor.execute(f"SELECT * FROM genres WHERE genreID = '{idField}' ") 
    
    record = cursor.fetchone() #fetch the updated publisher

    #iterate through all the records
    print(f"{'ID':<4} {'Genre':<8}")
    print(f"{record[0]:<4} {record[1]:<25} ")

if __name__ == "__main__":
    updateBook()
    updatePublisher()
    updateAuthor()
    updateGenre()