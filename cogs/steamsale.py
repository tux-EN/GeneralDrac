import requests as rq
import discord
from discord.ext import commands


class SteamSale(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def steamsale(self, ctx):
        url = "https://store.steampowered.com/api/featuredcategories"
        response = rq.get(url)
        data = response.json()


async def setup(bot):
    await bot.add_cog(SteamSale(bot))
