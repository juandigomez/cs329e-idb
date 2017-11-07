'''
This file defines the models for a book
'''
# for manipulating diff parts of Python's run-time environment
import sys
import os
# for writing mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base 

# for writing mapper code (create out foreign key relationship)
from sqlalchemy.orm import relationship

# for configuring code at the end of the file
from sqlalchemy import create_engine


# for creating an instance of the declarative_base class
# (the declarative base class will let SQLAlchemy know 
# that our classes are special SQLAlchemy classes that 
# corresponds to tables in our DB)
Base = declarative_base()

class Book(Base):
	__tablename__ = 'book'
	title = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	isbn = Column(String(80), nullable = False)
	author = Column(String(80), nullable = False)
	publication_date = Column(String(80), nullable = False)
	google_id = Column(String(80), nullable = False)
	image = Column(String(2048), nullable = False)
	description = Column(String(2048))

class Author(Base):
	__tablename__ = 'author'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	born = Column(String(80), nullable = False)
	education = Column(String(80))
	nationality = Column(String(80))
	description = Column(String(2048))
	alma_mater = Column(String(80))
	wiki = Column(String(2048))
	image = Column(String(2048))

class Publisher(Base):
	__tablename__ = 'publisher'
	name = Column(String(80), nullable = False)
	wiki = Column(String(2048))
	id = Column(Integer, primary_key = True)
	description = Column(String(2048))
	owner = Column(String(80))
	image = Column(String(2048))
	website = Column(String(2048))
	



SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:group8books@localhost/bookdb')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# try to run this file:
# python database_setup.py
# you may receive the following error:
# ImportError: No module named 'psycopg2'
# This indicates that you need to install 'psycopg2' module
# To install the 'psycopg2' module:
# pip install psycopg2
