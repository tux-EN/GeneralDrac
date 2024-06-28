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
        params = {'cc': 'us'} # Country code
        res = rq.get(url, params=params)
        data = res.json()
        specials = data.get('specials', {}).get('items', [])
        if not specials:
            await ctx.send("No specials available at the moment.")
            return

        for item in specials:
            store_url = f"https://store.steampowered.com/app/{item['id']}/"
            embed = discord.Embed(title=item['name'], url=store_url, color=0x00ff00)
            embed.add_field(name="Discount", value=f"{item['discount_percent']}%", inline=True)
            embed.add_field(name="Original Price", value=f"${item['original_price']/100:.2f} {item['currency']}", inline=True)
            embed.add_field(name="Final Price", value=f"${item['final_price']/100:.2f} {item['currency']}", inline=True)
            embed.set_thumbnail(url=item['small_capsule_image'])
            await ctx.send(embed=embed)

    @commands.command()
    async def steam(self, ctx, *, game_name):
        search_url = "https://store.steampowered.com/api/storesearch"
        price_url = "https://store.steampowered.com/api/appdetails"
        search_params = {'cc': 'us', 'l': 'english', 'term': game_name}
        res = rq.get(search_url, params=search_params)
        data = res.json()

        items = data.get('items', [])
        if not items:
            await ctx.send("No games found.")
            return

        for item in items[:5]:
            price_params = {'appids': item['id'], 'cc': 'us', 'filters': 'price_overview'}
            price_res = rq.get(price_url, params=price_params)
            price_data = price_res.json()

            store_url = f"https://store.steampowered.com/app/{item['id']}/"
            embed = discord.Embed(title=item['name'], url=store_url, color=0x00ff00)

            if 'price_overview' in price_data[str(item['id'])]['data']:
                price_overview = price_data[str(item['id'])]['data']['price_overview']
                initial_price = price_overview['initial'] / 100
                final_price = price_overview['final'] / 100
                discount_percentage = ((initial_price - final_price) / initial_price) * 100

                embed.add_field(name="Original Price", value=f"${initial_price:.2f} {price_overview['currency']}",
                                inline=True)
                embed.add_field(name="Discount", value=f"{discount_percentage:.2f}%", inline=True)
                embed.add_field(name="Final Price", value=f"${final_price:.2f} {price_overview['currency']}", inline=True)
            else:
                embed.add_field(name="Price", value="Free", inline=True)

            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(SteamSale(bot))
