from flask import Flask, jsonify
from .book_request import get_categories

app = Flask(__name__)

@app.route('/categories')
def home():
	return jsonify(get_categories())

@app.route('/<name>')
def hello_world(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run()