import os
import os.path
import json
import discord

botTokenPath='./json/botToken.json'


print("FoxHole Discord bot by Tuxmasku ver 0.0.1")

if os.path.isfile(botTokenPath) and os.access(botTokenPath, os.R_OK):
    print("Bot Token File is present proceeding...")
else:
    botToken=input("Please input your bot token: ")
    tokenData={"token": botToken}
    jsonData=json.dumps(tokenData)
    with open(botTokenPath, "w") as jsonFile:
        json.dump(tokenData, jsonFile)