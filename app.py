from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book, Author, Publisher, engine
from create_db import create_books, session
import subprocess
import json
import os
import test
# create a flask object (flask needs an object to represent the application)
app = Flask(__name__) 
 
# The route decorator '@app.route()' maps a function to a route on your website.  
# decorators are used to map a function, index(), to a web page, / or  
# i.e., when someone types in the home address of the web site, 
# flask will run the function index() 
# summary: type in a URL, flask check the URL, finds the associate function with it, runs the function,  collect responses, and send back the results to the browser.

# General
@app.route('/')
def index():
	return render_template("index.html")

# Summary Pages
@app.route('/aboutus/')
def aboutus():
	return render_template('aboutus.html')
	
@app.route('/books/')
def books():
	books = session.query(Book).all()
	return render_template('books.html', books = books)

@app.route('/books/<int:book_id>')
def singlebook(book_id):
    single_book = session.query(Book).get(book_id)
    return render_template('singlebook.html', book_id = book_id, book = single_book)

@app.route('/authors/')
def authors():
    authors = session.query(Author).all()
    return render_template('authors.html', authors = authors)

@app.route('/authors/<int:author_id>')
def singleauthor(author_id):
    single_author = session.query(Author).get(author_id)
    return render_template('singleauthor.html', author_id = author_id, author = single_author)
	
@app.route('/publishers/')
def publishers():
    publishers = session.query(Publisher).all()
    return render_template('publishers.html', publishers = publishers)

@app.route('/publishers/<int:pub_id>')
def singlepublisher(pub_id):
    single_publisher = session.query(Publisher).get(pub_id)
    return render_template('singlepublisher.html', pub_id = pub_id, publisher = single_publisher)
	
@app.route('/unit_tests')
def unit_tests(name = None):
  output = subprocess.getoutput("python test.py")
  return json.dumps({'output': str(output)})
	
"""# Individual author pages	
@app.route('/authors-Garth_Nix/')
def nix():
	return render_template('nix.html')
	
@app.route('/authors-Orson_Scott_Card/')
def card():
	return render_template('card.html')
	
@app.route('/authors-Douglas_Adams/')
def adams():
	return render_template('adams.html')

# Individual book pages
@app.route('/books-Enders_Game/')
def endersgame():
    return render_template('endersgame.html')

@app.route('/books-Restaurant/')
def restaurant():
    return render_template('restaurant.html')

@app.route('/books-Goldenhand/')
def goldenhand():
    return render_template('goldenhand.html')

# Individual Publisher Pages
@app.route('/palgravemacmillan/')
def palgravemacmillan():
    return render_template('palgravemacmillan.html')

@app.route('/delreybooks/')
def delreybooks():
    return render_template('delreybooks.html')

@app.route('/allenandunwin/')
def allenandunwin():
    return render_template('allenandunwin.html')"""


# The following functions handle caching problems
# that prevent the local host from displaying
# the updated static files.
# Pasted directly from https://gist.github.com/Ostrovski/f16779933ceee3a9d181
def static_file_hash(filename):
  return int(os.stat(filename).st_mtime)

@app.url_defaults
def hashed_url_for_static_file(endpoint, values):

    if 'static' == endpoint or endpoint.endswith('.static'):

        filename = values.get('filename')

        if filename:

            if '.' in endpoint:  # has higher priority

                blueprint = endpoint.rsplit('.', 1)[0]

            else:

                blueprint = None  # can be None too



            if blueprint:

                static_folder = app.blueprints[blueprint].static_folder

            else:

                static_folder = app.static_folder



            param_name = 'h'

            while param_name in values:

                param_name = '_' + param_name

            values[param_name] = static_file_hash(os.path.join(static_folder, filename))

   



# If deploying to GCP, uncomment the first if statement and comment out the second
#if __name__ == '__main__':


#    app.run(host='127.0.0.1', port=8080, debug=True)

	
#If Deploying locally, uncomment the second if statement and comment out the first
if __name__ == "__main__":
	app.run()
 
