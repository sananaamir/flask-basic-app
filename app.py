from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi! You've reached index! Go to https://sa-flask-basic-app.herokuapp.com/api/hello-world to see the api!"

@app.route('/api/hello-world')
def hello_world():
    return {'message':'Hello, world!'}