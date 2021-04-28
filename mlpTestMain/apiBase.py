from flask import Flask as fsk
import dataHandle as dh
import threading
from flask import jsonify
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


# search players information
@app.route('/pId/<unique_id>')
def getUser(unique_id):
    return jsonify(player[unique_id])


@app.route('/gameplay/<room_id>')
def showRoom(room_id):  # access room
    return jsonify(roomList[room_id])


@app.route('/gameplay/search/<player_id>')
def startSearch(player_id):  # get room information
    return jsonify(dh.addActivePlayers(player_id))


@app.route('/register/<email>')
def register_new(email):  # register new users
    new_player = {
        email: {
            "x": 0.0,
            "y": 0.0
        }
    }
    check_duplicate = check_redundancy(email)
    if check_duplicate:
        player.update(new_player)
        with open('players.json', 'w') as file:
            json.dump(player, file)
        return "success"
    return "failed to create id"


def check_redundancy(email):
    for i in player:
        if email == i:
            return False
    return True


if __name__ == "__main__":
    app.run(port=8081, host='0.0.0.0')

