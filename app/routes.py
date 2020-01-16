from app import app
from flask import render_template, request
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
database = myclient["matcha"]
collection = database["users"]

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Mosima'}
	return render_template('index.html', title = 'Welcome', user = user)


@app.route('/login', methods=['GET', 'POST'])
def login():
	user = {'username' : 'Mosima', 'password' : '123456'}
	
	if request.form:
		username = request.form["username"]
		password = request.form['password']

		if user['username'] == username and user['password'] == password:
			return render_template('welcome.html', title = 'logger', user = user)
		return render_template('login.html', title = 'Welcome', user = user)

	else:
		return render_template('login.html', title = 'Welcome', user = user)


@app.route('/register', methods=['GET', 'POST'])
def register():
	
	if request.form:
		firstname = request.form["firstname"]
		lastname = request.form["lastname"]
		username = request.form["username"]
		password = request.form['password']
		confirm_password = request.form['confirm-password']
		
		userdata = {
			'username' : username,
			'firstname' : firstname,
			'lastname' : lastname,
			'password' : password
		}

		results = collection.insert_one(userdata)
		print("created contents: " + str(results.inserted_id))
		return render_template('welcome.html', title = 'logger', user = userdata)

	else:
		return render_template('register.html', title = 'Register')


@app.route('/chat')
def chat():
    return render_template("chat.html")