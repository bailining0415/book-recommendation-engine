from flask import Flask, jsonify
from .book_request import get_categories, get_bestseller
from .user import getusers, register

app = Flask(__name__)

@app.route('/categories')
def categories():
	return jsonify(get_categories())

@app.route('/bestseller/<category>')
def bestseller(category):
	return jsonify(get_bestseller(category))

@app.route('/register/<username>/<password>')
def register_user(username, password):
	return register(username, password)

@app.route('/getusers')
def get_all_users():
	return jsonify(getusers())

if __name__ == '__main__':
   app.run()