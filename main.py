from readData import *
from insertData import *
from updateData import *
from deleteData import *
import time

def menuOptions():
    options = ["1", "2", "3", "4", "5", "6"]
    userInput = ''

    while userInput not in options:
        print("Songs Menu Options\n1. Print all books \n2. Add Books \n3. Update Books \n4. Delete Books \n5. Filter Books \n6. Exit")

        userInput = input("Enter one of the options 1-6: ")
        if userInput not in options:
            print(f"{userInput} is not a valid choice. Try again.")
    return userInput


mainProgram = True 

while mainProgram:
    mainmenu = menuOptions()
    if mainmenu == "1":
        readBooks()
    elif mainmenu == "2":
        addBooks()
    elif mainmenu == "3":
        print("Which table do you want to update? \n1. Books \n2. Publishers \n3. Authors \n4. Genres")
        while True:
            userInput = input("Enter one of the options 1-4: ")
            if userInput == "1":
                updateBook()
                break
            elif userInput == "2":
                updatePublisher()
                break
            elif userInput == "3":
                updateAuthor()
                break
            elif userInput == "4":
                updateGenre()
                break
            else:
                print(f"{userInput} is not a valid choice. Try again.")
                
            
    elif mainmenu == "4":
        deleteBooks()
    elif mainmenu == "5":
        print("What would you like to filter:? \n1. Books by Name \n2. Books by Publisher \n3. Books by Author \n4. Books by Genre")
        while True:
            userInput = input("Enter one of the options 1-4: ")
            if userInput == "1":
                readByBookName()
                break
            elif userInput == "2":
                readByPublishers()
                break
            elif userInput == "3":
                readByAuthors()
                break
            elif userInput == "4":
                readByGenres()
                break
            else:
                print(f"{userInput} is not a valid choice. Try again.")
    else:
        break
    time.sleep(2)