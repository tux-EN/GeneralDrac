import sqlite3 as sql
from discord.ext import commands



class FoxHole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def addstock(self, ctx, location: str, code: str):
        conn = sql.connect('foxhole.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO STOCKPILES (location, code) VALUES (?, ?)", (location, code))
        conn.commit()
        conn.close()
        await ctx.send(f"Added {location} to the database")


async def setup(bot):
    await bot.add_cog(FoxHole(bot))
