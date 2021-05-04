from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://geekyUtkarsh99:utkarsh99@cluster0.hkw3v.mongodb.net/test")

database = client['players']

users = database['users']


def checkDataBaseExistance(db):
    return database.list_collection_names()


def getUser(email):
    users = database['users']
    data = []
    cols = users.find({}, {"_id": 0, email: 1})
    i = 0
    for u in cols:
        data.append(u)
        i += 1
    return data


def insert_new_user(email):
    new_player = {
        email: {
            "x": 0.0,
            "y": 0.0
        }
    }
    data = users.find({}, {"_id": 0, email: 1})
    dats = []
    for i in data:
        dats.append(i)
    if dats is not None:
        return dats
    else:
        users.insert_one(new_player)
        return "registered successfully"
