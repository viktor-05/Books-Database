from sqlConnect import *


# ...........................
cursor.execute(
    """

  CREATE TABLE "publishers" (
	"publisherID"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	PRIMARY KEY("publisherID" AUTOINCREMENT)
)
"""
)

cursor.execute(
    """ 

CREATE TABLE "books" (
	"bookID"	INTEGER NOT NULL UNIQUE,
	"title"		TEXT,
	"year"	INTEGER,
	"price" INTEGER,
	"publisherID"	INTEGER NULL,
	PRIMARY KEY("bookID" AUTOINCREMENT),
	CONSTRAINT fk_publisher 
    FOREIGN KEY(publisherID) 
    REFERENCES publishers(publisherID) ON DELETE CASCADE
)"""
)
# ...............................
cursor.execute(
    """
CREATE TABLE "authors" (
	"authorID"	INTEGER NOT NULL UNIQUE,
	"fName"	TEXT,
	"lname"	TEXT,
	PRIMARY KEY("authorID" AUTOINCREMENT)
)"""
)



# ...........................
cursor.execute(
    """

  CREATE TABLE "write" (
	"authorID"	INTEGER,
	"bookID"	INTEGER,
	CONSTRAINT fk_book 
    FOREIGN KEY(bookID) 
    REFERENCES books(bookID) ON DELETE CASCADE, 
  CONSTRAINT fk_author 
    FOREIGN KEY(authorID) 
    REFERENCES authors(authorID) ON DELETE CASCADE
)
"""
)

# ...........................
cursor.execute(
    """

  CREATE TABLE "genres" (
	"genreID"	INTEGER NOT NULL UNIQUE,
	"gName"	TEXT,
	PRIMARY KEY("genreID" AUTOINCREMENT)
)
"""
)

# ...........................
cursor.execute(
    """

  CREATE TABLE "books_genres" (
	"genreID"	INTEGER,
	"bookID"	INTEGER,
	CONSTRAINT fk_book 
    FOREIGN KEY(bookID) 
    REFERENCES books(bookID) ON DELETE CASCADE, 
  CONSTRAINT fk_genre 
    FOREIGN KEY(genreID) 
    REFERENCES genres(genreID) ON DELETE CASCADE
)
"""
)

