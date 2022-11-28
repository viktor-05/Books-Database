from sqlConnect import *
import time
from readData import readBooks

def deleteBooks():
    
    idField = input("Enter the BookID of the books to be deleted: ")

    cursor.execute(f"DELETE FROM books WHERE bookID={idField}")
    conn.commit()
    #return the id of the deleted song
    print(f"Record {idField} deleted form the songs table")
    

if __name__ == "__main__":
    deleteBooks()