import json
import threading
import logging

activePlayers = json.load(open('search.json'))

roomsHandle = json.load(open('rooms.json'))


def check_redundancy(player_id):
    entries = activePlayers["actives"]
    for i in entries:
        if player_id == i:
            return False
    return True


# search query 1
def addActivePlayers(player_id):
    entries = activePlayers["actives"]
    bools = check_redundancy(player_id)
    if bools:
        entries.append(str(player_id))
        activePlayers["actives"] = entries
        with open('search.json', 'w') as file:
            json.dump(activePlayers, file)
        createRooms()
    return searchRoom(player_id)


def createRooms():
    while len(activePlayers["actives"]) > 1:
        entries = activePlayers["actives"]
        if len(entries) % 2 == 0 and not len(entries) == 0:  # even
            print(entries)
            p1 = entries[0]
            p2 = entries[1]
            key = "newRoomKey" + str(p1) + str(p2)
            room_new = {
                key: [str(p1), str(p2)]
            }
            roomsHandle.update(room_new)
            with open('rooms.json', 'w') as file:
                json.dump(roomsHandle, file)
            entries.remove(str(p1))
            entries.remove(p2)
            activePlayers["actives"] = entries
            with open('search.json', 'w') as file:
                json.dump(activePlayers, file)


def searchRoom(player_id):
    for i in roomsHandle:
        if player_id in i:
            return roomsHandle[i]
