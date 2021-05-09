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
        "y": 0.0,
        "status": "inactive"
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
    data = data.replace('\'', '\"')
    actives = json.loads(data)
    list_of_items = actives["actives"]
    checker = checkConcurancy(list_of_items, player_id)
    if checker:  # filter to check redundancy
        list_of_items.remove(player_id)
    list_of_items.append(player_id)
    searchRoom.update_one({"ref": 123}, {"$set": {
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


def checkConcurancy(list_items, player_id):
    for i in list_items:
        if i == player_id:
            return True
        else:
            return False


def create_room(player1, player2):  # create a new server room
    rooms = database["rooms"]
    newRoom = {

        "newRoomKey": [
            player1, player2
        ]

    }
    rooms.insert_one(newRoom)


def get_room_info(player_id):
    rooms = database["rooms"]
    cols = rooms.find({"newRoomKey": {"$eq": player_id}}, {"newRoomKey": 1})
    data = ""
    for i in cols:
        data += str(i)
    return data


def update_player(player_id, x, y):
    players = database["users"]

    players.find_and_modify({"email": player_id}, {"$set": {"x": x}})
    players.find_and_modify({"email": player_id}, {"$set": {"y": y}})

    return "success"


def delete_room(player_id):  # delete a room after usage
    rooms = database["rooms"]
    rooms.delete_one({"newRoomKey":{"$eq":player_id}})
    return "success"
