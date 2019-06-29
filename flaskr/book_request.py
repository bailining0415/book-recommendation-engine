import requests
import os
from dotenv import load_dotenv
from os.path import join, dirname
import json

dotenv_path = join(dirname(__file__), '.env')
API_KEY = os.getenv("NYT_API_KEY")

url = "https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={}"

def get_books():
	response = requests.get(url.format(API_KEY))
	return response.text

if __name__ == '__main__':
   get_books()