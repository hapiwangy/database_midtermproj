from pymongo import MongoClient
import os
import pprint

path = os.getcwd() + r"\data"
mongod = r"C:\Users\yudan\Downloads\mongodb-win32-x86_64-windows-6.0.2\bin\mongod.exe"

os.system(f"{mongod} --dbpath={path}")
# client = MongoClient(host="localhost", port=27017)

# db = client.banned
# x = "accountname"
# y = "password"
# for STs in db.user.find():
#     print(STs)