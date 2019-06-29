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

def register(username, password):
	all_users = db.child("users").get().each()
	if all_users != None:
		for user in all_users:
			if user.key() == username:
				return "username exists"
	db.child("users").child(username).set({ "name": username, "password": password })
	return "User created: %s" % username

def getusers():
	all_users = db.child("users").get().each()
	user_list = []
	if all_users != None:
		for user in all_users:
			user_list.append(user.val())
	return user_list


if __name__ == '__main__':
   register()
   getusers()