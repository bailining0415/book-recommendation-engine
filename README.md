# book-recommendation-engine

The book recommendataion engine consists of two main components:
1. API layer built on python flask
2. Web page in html

The api is powered by NYTimes book api and firebase, where users' info are stored at.

Instruction to run the flask app:
Set env variable: 
export FLASK_APP=flaskr
export FLASK_ENV=development

pip install -r requirements.txt

`flask run`