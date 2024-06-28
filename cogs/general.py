import discord
from discord.ext import commands
#  General cog that contains the help command and other general commands
class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = "Command Help",
            description = "Below is a list of commands for this bot",
            color = 0x00ff00
        )
        embed.add_field(name="!help", value="Displays this message", inline=False)
        embed.add_field(name="!ping", value="Checks if bot is alive", inline=False)
        embed.add_field(name="!addstock location code", value="Foxhole Command: Adds a stockpile to the database", inline=False)
        embed.add_field(name="!stock", value="Foxhole Command: Displays a list of stockpile locations", inline=False)
        embed.add_field(name="!steamsale", value="Displays the current steam sale(Currently inop)", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

async def setup(bot):
    await bot.add_cog(General(bot))