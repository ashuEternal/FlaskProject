from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World Changed!!'

@app.route('/about/<username>')
def about(username):
    return f'<h1>This is the about page of {username}</h1>'