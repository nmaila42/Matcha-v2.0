import pymongo

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "matcha_db" in dblist:
  print("The database exists.")