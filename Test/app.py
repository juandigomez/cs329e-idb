from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book, engine
from create_db import create_books, session


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('hello.html')
	
@app.route('/book/')
def book():
	books = session.query(Book).all()
	return render_template('book.html', books = books)
	

if __name__ == '__main__':
	app.debug = True
	app.run(host = '127.0.0.1', port = 8080)
	

