from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

mongo = MongoClient("mongodb://localhost:27017/")
matcha_database = mongo["matcha"]
users_collection = matcha_database["users"]

def add_user(user = None):
    if user == None:
        return None
    else:
        results = users_collection.insert_one(user)
        print("created contents: " + str(results.inserted_id))
        return 1

def username_exist(username = None):
    if username == None:
        return None
    else:
        if users_collection.find_one({'username': username}) == None:
            return None
        else:
            return True

def email_exist(email = None):
    if email == None:
        return None
    else:
        if users_collection.find_one({'email': email}) == None:
            return None
        else:
            return True

def get_user(user_id = None):
    if user_id == None:
        return None
    else:
        return users_collection.find_one({'_id': ObjectId(user_id)})

def validate_user(user_id = None):
    if user_id == None:
        return None
    else:
        user = {'_id': ObjectId(user_id)}
        validator = { '$set': { 'validated': datetime.utcnow() } }
        return users_collection.update_one(user, validator)

def username_password(username = None, password = None):
    if username == None or password == None:
        return None
    else:
        user = users_collection.find_one({'username': username, 'password': password})
        return str(user['_id'])

def email_password(email = None, password = None):
    if email == None or password == None:
        return None
    else:
        user = users_collection.find_one({'email': email, 'password': password})
        return str(user['_id'])

