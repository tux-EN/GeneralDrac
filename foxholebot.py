import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import foxfunction as ff

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
print("Ver 0.0.1 Licensed under GPL-3.0")

#pulls discord token and foxhole API link from env file
discordToken = os.getenv("DISCORD_TOKEN")
foxSvr = os.getenv("FOXHOLE_SERVER")

#Creates a SQlite DB that stores data about items and storage
ff.createSqliteDatabase('foxhole.db')

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
    
    

bot.run(discordToken)   