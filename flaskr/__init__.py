from flask import Flask, jsonify
from .book_request import get_categories, get_bestseller
import os
import pyrebase
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")

config = {
  "apiKey": os.getenv('FIREBASE_API_KEY'),
  "authDomain": "book-recommendation-engine.firebaseapp.com",
  "databaseURL": "https://book-recommendation-engine.firebaseio.com",
  "projectId": "book-recommendation-engine",
  "storageBucket": "book-recommendation-engine.appspot.com",
  "serviceAccount": "app/firebase-private-key.json",
  "messagingSenderId": "1052538486568"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)

@app.route('/categories')
def categories():
	return jsonify(get_categories())

@app.route('/bestseller/<category>')
def bestseller(category):
	return jsonify(get_bestseller(category))

@app.route('/<name>')
def hello_world(name):
   return 'Hello %s!' % name

@app.route('/newbook')
def add_book():
	db.child("book").push({"book": "hello"})
	return "Success"

if __name__ == '__main__':
   app.run()