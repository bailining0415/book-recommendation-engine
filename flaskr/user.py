# With help of reference link https://blog.upperlinecode.com/flask-and-firebase-and-pyrebase-oh-my-f30548d68ea9

import os
from dotenv import load_dotenv
from os.path import join, dirname
from .book_request import ALL_CATEGORIES, get_bestseller
import pyrebase
import json
import operator

dotenv_path = join(dirname(__file__), '.env')
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
	FIREBASE_API_KEY = os.environ.get('FIREBASE_API_KEY', None)

config = {
  "apiKey": os.environ['FIREBASE_API_KEY'],
  "authDomain": "book-recommendation-engine.firebaseapp.com",
  "databaseURL": "https://book-recommendation-engine.firebaseio.com",
  "projectId": "book-recommendation-engine",
  "storageBucket": "book-recommendation-engine.appspot.com",
  "serviceAccount": "firebase-private-key.json",
  "messagingSenderId": "1052538486568"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# extract only needed data from books api response to render
def construct_book(book, cat):
	return {
		"title": book["title"],
		"description": book["description"],
		"book_image": book["book_image"],
		"rank": book["rank"],
		"author": book["author"],
		"category": cat
	}

def validate_category(category):
	return category in ALL_CATEGORIES.values()

def update_user(username, data):
	db.child("users").child(username).set(data)

def getusers():
	all_users = db.child("users").get().each()
	user_list = []
	if all_users != None:
		for user in all_users:
			user_list.append(user.val())
	return user_list

def getuser(username):
	all_users = getusers()
	for user in all_users:
		if user["name"] == username:
			return user
	return None

def register(username, password):
	if getuser(username) != None:
		return False
	update_user(username, { "name": username, "password": password, "category": "" })
	return True

def add_category(username, category):
	if not validate_category(category): return "Invalid category"
	user = getuser(username)
	if user != None:
		if user["category"]:
			user["category"] += ","
		user["category"] += category
		update_user(username, user)
		return "Success"
	return "User not found"

def list_categories(username):
	user = getuser(username)
	if user != None:
		return user["category"].split(",")
	return None

def list_recommendations(username):
	categories = list_categories(username)
	if categories == None:
		return None
	all_books = []
	for cat in categories:
		res = get_bestseller(cat)
		top_books = res["books"][:3]
		for b in top_books:
			book = construct_book(b, cat)
			all_books.append(book)
	# https://stackoverflow.com/questions/26924812/python-sort-list-of-json-by-value
	results = sorted(all_books, key=lambda k: k['rank'], reverse=False)
	return results

if __name__ == '__main__':
   register()
   getusers()
   add_category()
   list_categories()
   list_recommendations()