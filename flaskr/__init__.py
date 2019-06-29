from flask import Flask
from .book_request import get_books

app = Flask(__name__)

@app.route('/')
def home():
	return get_books()

@app.route('/<name>')
def hello_world(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run()