from flask import Flask as fsk
import dataHandle as dh
import threading
from flask import jsonify
import mongoDataInteract as mdb
import json

app = fsk(__name__)
app.config["DEBUG"] = True

pname = 'abc'

roomList = json.load(open('rooms.json'))

# rList = roomList["rooms"]

player = json.load(open('players.json'))


@app.route('/', methods=['GET'])
def home():
    return 'initialize home'


@app.route('/checkSet', methods=['GET'])
def getDataBases():
    return str(mdb.getUser(None))


# search players information
@app.route('/pId/<unique_id>')
def getUser(unique_id):
    return jsonify(mdb.getUser(unique_id))


@app.route('/gameplay/<room_id>')
def showRoom(room_id):  # access room
    return jsonify(roomList[room_id])


@app.route('/gameplay/search/<player_id>')
def startSearch(player_id):  # get room information
    return jsonify(mdb.insert_to_searchQueue(player_id))


@app.route('/register/<email>')
def register_new(email):  # register new users
   return str(mdb.insert_new_user(email))


def check_redundancy(email):
    for i in player:
        if email == i:
            return False
    return True


if __name__ == "__main__":
    app.run(port=8081, host='0.0.0.0')
