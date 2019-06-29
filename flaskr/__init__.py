from flask import Flask, jsonify
from .book_request import get_categories, get_bestseller

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

if __name__ == '__main__':
   app.run()