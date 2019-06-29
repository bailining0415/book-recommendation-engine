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
  "serviceAccount": "firebase-private-key.json",
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

@app.route('/register/<username>/<password>')
def register(username, password):
	all_users = db.child("users").get().each()
	if all_users != None:
		for user in all_users:
			if user.key() == username:
				return "username exists"
	db.child("users").child(username).set({ "name": username, "password": password })
	return "User created: %s" % username

@app.route('/getuser')
def get_users():
	all_users = db.child("users").get().each()
	user_list = []
	if all_users != None:
		for user in all_users:
			user_list.append(user.val())
	return jsonify(user_list)

if __name__ == '__main__':
   app.run()