import pymongo
from pymongo import MongoClient


def get_database():
    url="mongodb+srv://admin:isaproj2021@cluster0.ckhcy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = MongoClient(url)
    return client['proj']


def logData(message):
    dbname=get_database()
    user_collection=dbname['user']
    transaction_collection=dbname['transactions']
    
def getpwd(username):
    dbname=get_database()
    user_collection=dbname['user']
    record=user_collection.find_one({"username":username})
    return record['pwd']
