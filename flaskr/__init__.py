# http://flask.pocoo.org/docs/1.0/quickstart/
from flask import Flask, jsonify, render_template, request, flash, url_for, redirect
from .book_request import ALL_CATEGORIES, get_bestseller
from .user import getusers, register, add_category, list_categories, list_recommendations

app = Flask(__name__)

@app.route('/categories')
def categories():
	return jsonify(ALL_CATEGORIES)

@app.route('/bestseller/<category>')
def bestseller(category):
	return jsonify(get_bestseller(category))

@app.route('/register', methods=['POST'])
def register_user():
	form = request.form
	username = ""
	password = ""
	for key,value in form.items():
		if key == "username":
			username = value
		if key == "password":
			password = value
	register(username, password)
	# if register(username, password):
	# 	flash("You have succesfully register %s" % username)
	# else:
	# 	flash("Username exists")
	return redirect(url_for('home'))

@app.route('/getusers')
def get_all_users():
	return jsonify(getusers())

@app.route('/setinterest', methods=['POST'])
def set_interest():
	form = request.form
	username = form["username"]
	category = form["category"]
	add_category(username, category)
	return redirect(url_for('home'))

@app.route('/listinterest/<username>')
def list_interest(username):
	res = list_categories(username)
	if res == None:
		return "User not found"
	return res

@app.route('/recommend', methods=['POST'])
def recommend():
	form = request.form
	username = form["username"]
	res = list_recommendations(username)
	if res == None:
		return "User not found"
	return render_template('recommendation.html', results = res)

@app.route('/')
def home():
	return render_template('index.html', categories = ALL_CATEGORIES)

if __name__ == '__main__':
   app.run()