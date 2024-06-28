import os
import sqlite3 as sql
from discord.ext import commands
from discord import Embed
from dotenv import load_dotenv
import os
load_dotenv()

class FoxHole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def addstock(self, ctx, location: str, code: str):
        conn = sql.connect(os.getenv("FOXHOLE_DB"))
        cur = conn.cursor()
        cur.execute("INSERT INTO STOCKPILES (location, code) VALUES (?, ?)", (location, code))
        conn.commit()
        conn.close()
        await ctx.send(f"Added {location} to the Foxhole database")

    @commands.command()
    async def stock(self, ctx):
        conn = sql.connect(os.getenv("FOXHOLE_DB"))
        cur = conn.cursor()
        cur.execute("SELECT * FROM STOCKPILES")
        rows = cur.fetchall()
        embed = Embed(
            title="Foxhole Stockpile Locations",
            description="Below is a list of stockpile locations",
            color=0x00ff00
        )
        for row in rows:
            embed.add_field(name=row[0], value=row[1], inline=False)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(FoxHole(bot))
