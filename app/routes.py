from app import app
from flask import render_template, request, session, redirect, url_for
from datetime import datetime
import models

@app.route('/')
@app.route('/index')
def index():
	
	print(session)
	user = {'username':'Mosima'}
	return render_template('index.html', title = 'Welcome', user = user)


@app.route('/logout')
def logout():
	session.clear()
	print(session)
	return render_template('index.html', title = 'Welcome')


@app.route('/login', methods=['GET', 'POST'])
def login():

	if request.form:
		username = request.form["username"]
		password = request.form['password']

		user_id = models.user.username_password(username, password)
		session['user_id'] = user_id
		print(user_id)
		if user_id == None:
			return render_template('login.html', title = 'Welcome', user = user_id)
		return render_template('welcome.html', title = 'logger', user = {'username': user_id})

	else:
		return render_template('login.html', title = 'Welcome')


@app.route('/register', methods=['GET', 'POST'])
def register():
	
	if request.form:
		firstname = request.form["firstname"]
		lastname = request.form["lastname"]
		username = request.form["username"]
		email = request.form["email"]
		password = request.form['password']
		confirm_password = request.form['confirm-password']

		registration_errors = {}
		registration_errors.clear

		if models.user.username_exist(username):
			registration_errors.update({'username': 'username already exist.'})		
		if models.user.email_exist(email):
			registration_errors.update({'email': 'email already exist.'})
		if len(password) == 0:
			registration_errors.update({'password': 'password can not be empty.'})
		if password != confirm_password:
			registration_errors.update({'confirm_password': 'passwords do no match.'})
		
		if len(registration_errors) == 0:
			userdata = {
				'username' : username,
				'firstname' : firstname,
				'lastname' : lastname,
				'email' : email,
				'password' : password,
				'registration_date': datetime.utcnow() 
			}
			models.user.add_user(userdata)
			return render_template('welcome.html', title = 'logger', user = userdata)
		else:
			print(registration_errors)
			return render_template('register.html', title = 'Register', errors = registration_errors)

	else:
		return render_template('register.html', title = 'Register')


@app.route('/chat')
def chat():
    return render_template("chat.html")