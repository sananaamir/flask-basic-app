from flask import Flask

app = Flask(__name__)

@app.route('/api/hello-world')
def hello_world():
    return {'message':'Hello, world!'}