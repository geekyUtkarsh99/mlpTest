from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://geekyUtkarsh99:utkarsh99@cluster0.hkw3v.mongodb.net/test")

database= client['players']

users = database['users']


def checkDataBaseExistance(db):
    return database.list_collection_names()


def getUser():
    users = database['users']
    data = []
    cols = users.find({},{"_id":0,"pid1":1})
    i = 0
    for u in cols:
        data.append(u)
        i+=1
    return data


def insert_new_user(email):
    new_player = {
        email: {
            "x": 0.0,
            "y": 0.0
        }
    }
    data = users.find({},{email:1})
    return data