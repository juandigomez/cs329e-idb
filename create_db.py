import json, logging
# using SQLAlchmey, creating a new DB is as easy
# as creating a new object in Python.

# import the following dependencies from SQLAlchmey
# and the empty database we created into our environment 
from sqlalchemy.orm import sessionmaker
from models import Base, Book, engine

# bind the engine to the base class. This makes the connection
# between our class definitions and the corresponding tables 
# within our database
Base.metadata.bind = engine

# create session maker object to establish a link 
# of communication between our code execution and 
# the engine we just created
DBSession = sessionmaker(bind=engine)

# in order to create, read, update or delete information 
# on our database, SQLAlchmey executes database operations
# via an interface called a session.
# A session allows us to write down all the commands 
# we want to execute but not send them to the DB 
# until we call "commit"
# create an instance of DBSession
session = DBSession()
id_count = 0

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_books():
    book = load_json('books.json')

    for oneBook in book:
        title = oneBook['title']
        isbn = oneBook['isbn']
        publication_date = oneBook['publication_date']
        google_id = oneBook['google_id']
        author = oneBook['authors']['name']
        image = oneBook['image_url']
        description = oneBook['description']
		
        newBook = Book(title = title, id = id_count, isbn = isbn, author = author, publication_date = publication_date, google_id = google_id,image = image, description = description)
		# After I create the book, I can then add it to my session. 
        session.add(newBook)
		# commit the session to my DB.
        session.commit()
        id_count += 1

def create_authors():
    author = load_json('books.json')

    for oneBook in author:
        born = oneBook['authors']['born']
        name = oneBook['authors']['name']
        education = oneBook['authors']['education']
        nationality = oneBook['authors']['nationality']
        description = oneBook['authors']['description']
        alma_mater = oneBook['authors']['alma_mater']
        wiki = oneBook['authors']['wikipedia_url']
        image = oneBook['authors']['image_url']

        newAuthor = Author(born = born, name = name, education = education, nationality = nationality, description = description, alma_mater = alma_mater, wiki = wiki, image = image, id = id_count)

        session.add(newAuthor)
        session.commit()
        id_count += 1

def create_publisher():
    publisher = load_json('books.json')

    for oneBook in publisher:
        publisher_item = oneBook['publishers']
        name = publisher_item['name']
        wiki = publisher_item['wikipedia_url']
        description = publisher_item['description']
        owner = publisher_item['owner']
        image = publisher_item['image_url']
        website = publisher_item['website']

        newPublisher = Publisher(name = name, wiki = wiki, description = description, owner = owner, image = image, website = website, id = id_count)

        session.add(newPublisher)
        session.commit()
        id_count += 1

		
create_books()
create_authors()
create_publisher()


