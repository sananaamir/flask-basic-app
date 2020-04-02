from flask import (Flask, render_template)
import json
import sqlite3
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/hello-world')
def hello_world():
    return {'message':'Hello, world!'}

@app.route('/api/users')
def get_users():
    conn = sqlite3.connect('TEST_DB.db')
    c = conn.cursor()

    create_example_user_data(c, conn)
    
    c.execute("SELECT * FROM users")
    users = c.fetchall()

    return {'users': users}

def get_example_users_file():
    data = []
    with open('example_users.json') as json_data:
        data = json.load(json_data)

    return data

def create_example_user_data(c, conn):
    users = get_example_users_file()

    #Create table
    c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT, firstName TEXT, lastName TEXT, gender TEXT)')

    for user in users:
        c.execute("INSERT INTO users (email, firstName, lastName, gender) VALUES(?,?,?,?)", (user['email'], user['firstName'], user['lastName'], user['gender']))
    conn.commit()