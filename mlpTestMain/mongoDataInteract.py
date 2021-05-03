import pymongo as mongodb

client = mongodb.MongoClient("mongodb+srv://utkarsh:utkarsh99@cluster0.hkw3v.mongodb.net/test")

database = client["players"]


def checkDataBaseExistance(database):
    return client.list_database_names()