from pymongo import MongoClient
from flask import jsonify
import json

client = MongoClient("mongodb+srv://geekyUtkarsh99:utkarsh99@cluster0.hkw3v.mongodb.net/test")

database = client['players']

users = database['users']


def checkDataBaseExistance(db):
    return database.list_collection_names()


def getUser(email):
    users = database['users']
    data = ""
    cols = users.find({"email": email}, {"_id": 0})
    for u in cols:
        data += str(u)
    return data


def insert_new_user(email):
    new_player = {
        "email": email,
        "x": 0.0,
        "y": 0.0
    }
    data = users.find_one({"email": email}, {"_id": 0})
    # check availability
    if data is not None:
        return "player exists"
    else:
        users.insert_one(new_player)
        return "success"


def insert_to_searchQueue(player_id):  # insert a new player in queue
    searchRoom = database["search"]
    cols = searchRoom.find({}, {"_id": 0, "actives": 1})
    data = ""
    for i in cols:
        data += str(i)
    data = data.replace('\'', '\"');
    actives = json.loads(data)
    list_of_items = actives["actives"]
    list_of_items.append(player_id)
    searchRoom.update_one({"ref": 123}, {"#set": {
        "actives": list_of_items}})
    while len(list_of_items) > 1:
        if len(list_of_items) % 2 == 0 and not len(list_of_items) == 0:
            player1 = list_of_items[0]
            player2 = list_of_items[1]
            create_room(player1, player2)
            list_of_items.remove(player1)
            list_of_items.remove(player2)
            searchRoom.update_one({"ref": 123}, {"$set": {
                "actives": list_of_items}})

    return "check success"


def create_room(player1, player2):
    rooms = database["rooms"]
    key = "newRoomKey" + str(player1) + str(player2)
    newRoom = {

        key: [
            player1, player2
        ]

    }
    rooms.insert_one(newRoom)
