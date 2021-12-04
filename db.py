import pymongo
from pymongo import MongoClient
from pymongo.message import insert
import Model


def get_database():
    url="mongodb+srv://admin:isaproj2021@cluster0.ckhcy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = MongoClient(url)
    return client['proj']


def logData(message):
    dbname=get_database()
    user_collection=dbname['user']
    transaction_collection=dbname['transactions']

def getAll(username):
    dbname=get_database()
    user_collection=dbname['user']
    record=user_collection.find_one({"username":username})
    user=Model.User(record['username'],record['dob'],record['email'],record['amount'])
    return user
    
def getpwd(username):
    dbname=get_database()
    user_collection=dbname['user']
    record=user_collection.find_one({"username":username})
    return record['pwd']

def insert_transactions(tag,nonce,cyphertext):
    dbname=get_database()
    transaction_collection=dbname['transactions']
    transaction_collection.insert_one({"tag":tag,"nonce":nonce,"encrypted_data":cyphertext})

# d=getAll("niyantha23")  
# print(d.amount)