import os.path
import os
import json
import discord as d
import sqlite3 as sq
import foxfunct as ff

# Foxhole Discord Bot By Tuxmasku
# Licensed under GNU
# Ver 0.0.1

# Constants
botTokenPath = './json/botToken.json'

print("""
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░██╗░░░░░██████╗░██████╗░░█████╗░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║██║░░░░░██║░░██║██████╔╝███████║██║░░╚═╝██║░░░██║██║░░░░░███████║
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║██║░░░░░██║░░██║██╔══██╗██╔══██║██║░░██╗██║░░░██║██║░░░░░██╔══██║
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║███████╗██████╔╝██║░░██║██║░░██║╚█████╔╝╚██████╔╝███████╗██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝""")
print("Foxhole Discord bot by Tuxmasku")
print("Ver 0.0.1 Licensed under GPL-3.0")

# Determine if token file is present and prompts user to create it if it does not exist.
if os.path.isfile(botTokenPath) and os.access(botTokenPath, os.R_OK):
    print("Bot Token File is present proceeding...")
else:
    botToken = input("Please input your bot token: ")   # requests input from user to place discord bot token
    tokenData = {"token": botToken}
    jsonData = json.dumps(tokenData)
    with open(botTokenPath, "w") as jsonFile:
        json.dump(tokenData, jsonFile)

