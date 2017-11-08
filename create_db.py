import json, logging
# using SQLAlchmey, creating a new DB is as easy
# as creating a new object in Python.

# import the following dependencies from SQLAlchmey
# and the empty database we created into our environment 
from sqlalchemy.orm import sessionmaker
from models import Base, Book, Author, Publisher, engine

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
    id_count = 0

    for oneBook in book['Books']:
        title = oneBook['title']
        if 'isbn' in oneBook:
            isbn = oneBook['isbn']
        if 'publication_date' in oneBook:
            publication_date = oneBook['publication_date']
        google_id = oneBook['google_id']
        name = oneBook['authors'][0]['name']
        image = oneBook['image_url']
        if 'description' in oneBook:
            description = oneBook['description']
		
        newBook = Book(description = description, image = image, author = name, google_id = google_id, publication_date = publication_date, isbn = isbn, title = title, id = id_count)
		# After I create the book, I can then add it to my session. 
        session.add(newBook)
		# commit the session to my DB.
        session.commit()
        id_count += 1

def create_authors():
    book = load_json('books.json')
    id_count = 0

    for oneBook in book['Books']:
        oneAuthor = oneBook['authors'][0]
        if 'born' in oneAuthor:
            born = oneAuthor['born']
        name = oneAuthor['name']
        if 'education' in oneAuthor:
            education = oneAuthor['education']
        else:
            education = "N/A"
        if 'nationality' in oneAuthor:
            nationality = oneAuthor['nationality']
        else:
            nationality = "N/A"
        if 'description' in oneAuthor:
            description = oneAuthor['description']
        else:
            description = "N/A"
        if 'alma_mater' in oneAuthor:
            alma_mater = oneAuthor['alma_mater']
        else:
            alma_mater = "N/A"
        if 'wikipedia_url' in oneAuthor:
            wiki = oneAuthor['wikipedia_url']
        else:
            wiki = "N/A"
        if 'image_url' in oneAuthor:
            image = oneAuthor['image_url']
        else:
            image = ""

        newAuthor = Author(born = born, name = name, education = education, nationality = nationality, description = description, alma_mater = alma_mater, wiki = wiki, image = image, id = id_count)
        if session.query(Author.id).filter(Author.name==newAuthor.name).count() > 0:
            session.add(newAuthor)
            session.commit()
            id_count += 1

def create_publisher():
    book = load_json('books.json')
    id_count = 0

    for oneBook in book['Books']:
        onePublisher = oneBook['publishers'][0]
        name = onePublisher['name']
        if 'wikipedia_url' in onePublisher:
            wiki = onePublisher['wikipedia_url']
        else:
            wiki = "N/A"
        if 'description' in onePublisher:
            description = onePublisher['description']
        else:
            description = "N/A"
        if 'owner' in onePublisher:
            owner = onePublisher['owner']
        else:
            owner = "N/A"
        if 'image_url' in onePublisher:
            image = onePublisher['image_url']
        else:
            image = ""
        if 'website' in onePublisher:
            website = onePublisher['website']
        else:
            website = "N/A"

        newPublisher = Publisher(name = name, wiki = wiki, description = description, owner = owner, image = image, website = website, id = id_count)
        if session.query(Publisher.id).filter(Publisher.name==newPublisher.name).count() > 0:
            session.add(newPublisher)
            session.commit()
            id_count += 1

		
create_books()
create_authors()
create_publisher()


