import os
from dotenv import load_dotenv
from os.path import join, dirname
import pyrebase

dotenv_path = join(dirname(__file__), '.env')
FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")

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
		return "Username exists"
	update_user(username, { "name": username, "password": password, "category": "" })
	return "User created: %s" % username

def add_category(username, category):
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

if __name__ == '__main__':
   register()
   getusers()
   add_category()
   list_categories()