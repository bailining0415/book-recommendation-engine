# book-recommendation-engine

The book recommendataion engine consists of two main components:
1. API layer built on python flask
2. Web page in html

The api is powered by NYTimes book api and firebase, where users' info are stored at.

Step-by-Step Guide on Deploying a Simple Flask App to Heroku
https://pybit.es/deploy-flask-heroku.html

The app is hosted at :http://book-recommendation-engine.herokuapp.com/

Breakdown of the app:

__init__.py is the main file of the flask app, it defines the routes of the app and render the web page based on url and user input.

book_request.py contains the logic to fetch info from nytimes book api including categories and bestsellers. 

user.py defines how the app interacts with user database in firebase, including creating user, storing user preferences.

database schema:
username: string,
password: string,
categories: string(comma separated)


To run the app locally:
Set env variable: 
export FLASK_APP=flaskr
export FLASK_ENV=development

pip install -r requirements.txt

Run command line:
`flask run`
