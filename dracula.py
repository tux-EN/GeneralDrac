import discord
import foxfunction as ff
import os
import sqlite3 as sql
from discord.ext import commands
from dotenv import load_dotenv

# Constants
load_dotenv()
fox_db = 'foxhole.db'
drac_db = 'dracula.db'


print("Discord bot by Tuxmasku")
print("Ver 0.1.2 Licensed under GPL-3.0")

# pulls discord token and foxhole API link from env file

discordToken = os.getenv("DISCORD_TOKEN")
foxSvr = os.getenv("FOXHOLE_SERVER")

# Creates a SQlite DB that stores data about items and storage
if not os.path.exists(fox_db):
    ff.init_db(fox_db)
    conn = sql.connect(fox_db)
    cur = conn.cursor()
    cur.execute("CREATE TABLE STOCKPILES (location VARCHAR(255), code INT(6))")
    print("Foxhole DB created")
    conn.close()

if not os.path.exists(drac_db):
    ff.init_db(drac_db)
    print("Dracula DB created")

# initializes discord client intents for bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
# Init bot's prefix for commands.
bot = commands.Bot(command_prefix='!', intents=intents)


# bot init
@bot.event
async def on_ready():
    print(f'logged in as {bot.user} (ID: {bot.user.id})')
    for guild in bot.guilds:
        print(f'Connected to the following server: {guild.name}')


# test command will remove
@bot.command()
async def test(ctx):
    await ctx.send('test worked')


# bot help command will add as needed
@bot.command()
async def gdhelp(ctx):
    hmsg = f"""**Help Menu**\n
!test: this command test function will be removed
!gdhelp: this command displays this text
!addstockpile: Adds stockpile to DB (Command is "!addstockpile location code")
!liststockpile: Lists stockpiles and their codes
"""
    embed = discord.Embed(title=hmsg)
    await ctx.author.send(embed=embed)


@bot.command()
async def addstockpile(ctx, location: str, code: str):
    ff.add_stockpile(ctx, location, code)
    await ctx.send(f"added '{location} to stockpile DB")


@bot.command()
async def liststockpile(ctx):
    conn = sql.connect(fox_db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM STOCKPILES")
    rows = cur.fetchall()

    if not rows:
        await ctx.send("No stockpiles present")
    else:
        stockpile_list = "\n".join([f"{row[0]} - {row[1]}" for row in rows])
        await ctx.send(f"**Stockpile List:**\n{stockpile_list}")
    conn.close()

bot.run(discordToken)
