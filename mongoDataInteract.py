import pymongo as mongodb

client = mongodb.MongoClient("mongodb+srv://geekyUtkarsh99:utkarsh99@cluster0.hkw3v.mongodb.net/test")

database = client['players']


def checkDataBaseExistance(database):
    return database.list_collection_names()

