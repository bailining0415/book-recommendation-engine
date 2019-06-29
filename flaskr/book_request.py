import requests
import os
from dotenv import load_dotenv
from os.path import join, dirname
import json

dotenv_path = join(dirname(__file__), '.env')
API_KEY = os.getenv("NYT_API_KEY")

base_url = "https://api.nytimes.com/svc/books/v3"
api_key_param = "?api-key=%s" % API_KEY
category_url = "%s/lists/names.json%s" % (base_url, api_key_param)

def get_categories():
	response = requests.get(category_url)
	datas = json.loads(response.text)['results']
	list_names = []
	for data in datas:
		list_names.append(data['list_name'])
	return list_names

if __name__ == '__main__':
   get_categories()