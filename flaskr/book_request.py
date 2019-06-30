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
best_seller_url = "%s/lists/current/{}.json%s" % (base_url, api_key_param)

def get_categories():
	response = requests.get(category_url)
	datas = json.loads(response.text)['results']
	list_names = {}
	for data in datas:
		list_names[data['list_name']] = data['list_name_encoded']
	return list_names

def get_bestseller(category):
	response = requests.get(best_seller_url.format(category))
	datas = json.loads(response.text)['results']
	return datas

ALL_CATEGORIES = get_categories()

if __name__ == '__main__':
   get_categories()
   ALL_CATEGORIES