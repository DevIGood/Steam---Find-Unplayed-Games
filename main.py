import requests
import random
import json
import os

global Key, mySteamID

try:
    with open("data.json", "r") as file:
        jsonText = json.load(file)
        Key = jsonText['Key']
        mySteamID = jsonText['mySteamID']
    file.close()
except FileNotFoundError:
    jsonText = {
    	"Key": " ",
    	"mySteamID": " "
    }
    jsonTextIndent = json.dumps(jsonText, indent=4)

    with open("data.json", "w+") as file:
        file.write(jsonTextIndent)
    file.close()

    print(" --- Fill in required data in data.json ---")
    raise

def readJson():
    try:
        with open("unplayed_games.json", "r") as file:
            jsonText = json.load(file)
        file.close()
        return jsonText
    except FileNotFoundError:
        print(" --- Run 'Update list' to make it work ---")
        raise

def writeJson(jsonText):
    with open("unplayed_games.json", "w+") as file:
        file.write(jsonText)
    file.close()

def printGameList():
    jsonText = readJson()
    for x in range(len(jsonText['response']['games'])):
        print(jsonText['response']['games'][x]['name'],)

def pickRandomGame():
    randGame = []
    jsonText = readJson()
    for x in range(len(jsonText['response']['games'])):
        randGame.append(jsonText['response']['games'][x]['name'],)
    print(random.choice(randGame))

def updateList():
    URL = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={Key}&steamid={mySteamID}&include_appinfo=1&format=json"
    req = requests.get(url = URL)
    jsonText = req.json()
    for x in reversed(jsonText['response']['games']):
        if (x['playtime_forever'] != 0):
            jsonText['response']['games'].remove(x)
    jsonText = json.dumps(jsonText, indent=4)
    writeJson(jsonText)

while True:
    choice = int(input("\n1)Print games you haven't played\n2)Pick random game to play\n3)Update list\n4)Exit\n\nYour choice = "))
    if choice == 1:
        os.system('cls')
        printGameList()
    elif choice == 2:
        os.system('cls')
        pickRandomGame()
    elif choice == 3:
        os.system('cls')
        updateList()
    elif choice == 4:
        os.system('cls')
        break
    else:
        os.system('cls')
        print("Wrong input")