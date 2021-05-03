import pymongo as mongodb

client = mongodb.MongoClient("mongodb+srv://geekyUtkarsh99:utkarsh99@cluster0.hkw3v.mongodb.net/test")

database= client.get_database('players')


def checkDataBaseExistance(db):
    return database.list_collection_names()

