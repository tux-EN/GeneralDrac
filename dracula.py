import os
import sqlite3 as sql
import discord
import subprocess
from discord.ext import commands
from dotenv import load_dotenv
from dbfunc import init_db
import wavelink
import logging
import logging.handlers
import asyncio


print("Discord bot by Tuxmasku")
print("Ver 0.2.0 Licensed under GPL-3.0")

# initializes discord client intents
load_dotenv()
cogs: list = ["cogs.steamsale", "cogs.foxhole", "cogs.general","cogs.music"]
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
        nodes = [wavelink.Node(uri="http://0.0.0.0:2333", password="youshallnotpass")]
        await wavelink.Pool.connect(client=self, nodes=nodes)
        print(f"Logged in as {self.user}")



bot = bot()
async def main():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)




    if not os.path.exists(os.getenv("FOXHOLE_DB")):
        init_db(os.getenv("FOXHOLE_DB"))
        conn = sql.connect(os.getenv("FOXHOLE_DB"))
        cur = conn.cursor()
        cur.execute("CREATE TABLE STOCKPILES (location VARCHAR(255), code INT(6))")
        conn.close()

    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32*1024*1024, #32MB max size
        backupCount=5
    )
    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', date_format, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    await bot.start(os.getenv("DISCORD_TOKEN"))

asyncio.run(main())
