# book-recommendation-engine

The book recommendataion engine consists of two main components:
1. API layer built on python flask
2. Web page in html

The api is powered by NYTimes book api and firebase, where users' info are stored at.

Step-by-Step Guide on Deploying a Simple Flask App to Heroku
https://pybit.es/deploy-flask-heroku.html

The app is hosted at :http://book-recommendation-engine.herokuapp.com/



To run the app locally:
Set env variable: 
export FLASK_APP=flaskr
export FLASK_ENV=development

pip install -r requirements.txt

Run command line:
`flask run`
