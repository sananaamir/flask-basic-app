from flask import (Flask, render_template)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/hello-world')
def hello_world():
    return {'message':'Hello, world!'}