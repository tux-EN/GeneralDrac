import os
import discord
from discord.ext import commands
import sqlite3 as sql
from dotenv import load_dotenv

# Foxhole Discord Bot By Tuxmasku
# Licensed under GNU
# Ver 0.0.1

# Constants
load_dotenv()

print("""
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░██╗░░░░░██████╗░██████╗░░█████╗░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║██║░░░░░██║░░██║██████╔╝███████║██║░░╚═╝██║░░░██║██║░░░░░███████║
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║██║░░░░░██║░░██║██╔══██╗██╔══██║██║░░██╗██║░░░██║██║░░░░░██╔══██║
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║███████╗██████╔╝██║░░██║██║░░██║╚█████╔╝╚██████╔╝███████╗██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝""")
print("Foxhole Discord bot by Tuxmasku")
print("Ver 0.1.1 Licensed under GPL-3.0")

#pulls discord token and foxhole API link from env file
discordToken = os.getenv("DISCORD_TOKEN")
foxSvr = os.getenv("FOXHOLE_SERVER")


#Creates a SQlite DB that stores data about items and storage
if not os.path.exists('fhstockpile.db'):
    ff.initstockpileDB('fhstockpile.db')

#intializes discord client def
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user} (ID: {bot.user.id})')
    for guild in bot.guilds:
        print(f'Connected to the following server: {guild.name}')

#test command will remove
@bot.command()
async def test(ctx):
    await ctx.send('test worked')

#bot help command will add as needed
@bot.command()
async def gdhelp(ctx):
    hmsg = f"""
!test: this command tests
!gdhelp: this command displays this
"""
    embed = discord.Embed(title=hmsg)
    await ctx.author.send(embed=embed)

@bot.command()
async def addstockpile(ctx, location: str, code: str):
    conn = sql.connect('fhstockpile.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO STOCKPILES (location, code) VALUES (?, ?)", (location, code))
    conn.commit()
    conn.close
    
    await ctx.send(f"added '{location} to stockpile DB")
    
@bot.command()
async def liststockpile(ctx):  
    conn = sql.connect('fhstockpile.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM STOCKPILES")
    rows = cur.fetchall()
    
    if not rows:
        await ctx.send("No stockpiles present")
    else:
        stockpileList = "\n".join([f"{row[0]} - {row[1]}" for row in rows])
        await ctx.send(f"**Stockpile List:**\n{stockpileList}")
    conn.close()
    
bot.run(discordToken)   