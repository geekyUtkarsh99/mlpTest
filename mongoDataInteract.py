from pymongo import MongoClient
import json

client = MongoClient("mongodb+srv://geekyUtkarsh99:utkarsh99@cluster0.hkw3v.mongodb.net/test")

database= client['players']


def checkDataBaseExistance(db):
    return database.list_collection_names()


def getUser():
    users = database['users']
    data = []
    cols = users.find()
    dats = json.load(cols)
    i = 0
    for u in cols:
        data.append(u)
        i+=1
    return dats