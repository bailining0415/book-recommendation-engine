from flask import Flask, jsonify
from .book_request import ALL_CATEGORIES, get_bestseller
from .user import getusers, register, add_category, list_categories, list_recommendations

app = Flask(__name__)

@app.route('/categories')
def categories():
	return jsonify(ALL_CATEGORIES)

@app.route('/bestseller/<category>')
def bestseller(category):
	return jsonify(get_bestseller(category))

@app.route('/register/<username>/<password>')
def register_user(username, password):
	return register(username, password)

@app.route('/getusers')
def get_all_users():
	return jsonify(getusers())

@app.route('/setinterest/<username>/<category>')
def set_interest(username, category):
	return add_category(username, category)

@app.route('/listinterest/<username>')
def list_interest(username):
	res = list_categories(username)
	if res == None:
		return "User not found"
	return res

@app.route('/recommend/<username>')
def recommend(username):
	res = list_recommendations(username)
	if res == None:
		return "User not found"
	return jsonify(res)

if __name__ == '__main__':
   app.run()