from app import app
from flask import render_template, request

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Mosima'}
    return render_template('index.html', title = 'Welcome', user = user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = {'username':'Mosima'}
    print(request.form["username"])
    return render_template('welcome.html', title = 'logger', user = user)

