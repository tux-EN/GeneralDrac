import os
import sqlite3 as sql
import discord
from discord.ext import commands
from dotenv import load_dotenv

#  Variables for the bot
cogs: list = ["cogs.steamsale", "cogs.foxhole", "cogs.general"]
load_dotenv()
fox_db = 'foxhole.db'

print("Discord bot by Tuxmasku")
print("Ver 0.2.0 Licensed under GPL-3.0")

#  Function that initializes a SQLite DB
def init_db(filename):
    conn = None
    try:
        conn = sql.connect(filename)
        print(sql.sqlite_version)
        print(f"{filename} created")
    except sql.error as e:
        print(e)
    finally:
        if conn:
            conn.close()

# Creates a SQlite DB that stores data about items and storage
if not os.path.exists(fox_db):
    init_db(fox_db)
    conn = sql.connect(fox_db)
    cur = conn.cursor()
    cur.execute("CREATE TABLE STOCKPILES (location VARCHAR(255), code INT(6))")
    conn.close()


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

bot = bot()
bot.run(os.getenv("DISCORD_TOKEN"))
