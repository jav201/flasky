from flask import Flask, make_response, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Hola Mundo</h1>'

# Index storing a cookie
# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie</h1>')
#     response.set_cookie('answer', '42')
#     return response
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello {0} </h1>'.format(name)