import discord
import foxfunction as ff
import os
import sqlite3 as sql
from discord.ext import commands
from dotenv import load_dotenv

#Init Variables
fox_db = 'foxhole.db'
dracula_db = 'dracula.db'
conn = None
cogs: list = ["cogs.steamsale", "cogs.foxhole"]

print("Discord bot by Tuxmasku")
print("Ver 0.2.0 Licensed under GPL-3.0")

# pulls discord token and foxhole API link from env file


# Creates a SQlite DB that stores data about items and storage
if not os.path.exists(fox_db):
    ff.init_db(fox_db)
    conn = sql.connect(fox_db)
    cur = conn.cursor()
    cur.execute("CREATE TABLE STOCKPILES (location VARCHAR(255), code INT(6))")
    print("Foxhole DB created")
    conn.close()

if not os.path.exists(dracula_db):
    ff.init_db(dracula_db)
    print("Dracula DB created")

# initializes discord client intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


#  Bot class that inherits from commands.Bot
class bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="!",
            intents = intents,
            help_command = None
        )
#  Setup hook that loads cogs from the cogs list
    async def setup_hook(self) -> None:
        for cog in cogs:
            await self.load_extension(cog)
            print(f"Loaded {cog}")
        print("Bot is ready")
#  On ready event that prints the bot's name to confirm token
    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")

#loads env file
load_dotenv()

bot = bot()
bot.run(os.getenv("DISCORD_TOKEN"))
