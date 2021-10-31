import discord
import json
import random
from aiohttp import request
from discord.ext import commands


class API(commands.Cog, name='API Commands'):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(
        name='kpop',
        aliases=[
            'kapi',
            'idol']
    )
    async def kpop(self, ctx, idol):
        URL = "https://api.maknae.xyz/v1/idols/all/"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                CAPITAL = str(idol).capitalize()
                MAX = len(data[str(CAPITAL)])
                INDEX = random.randint(0, MAX-1)

                embed = discord.Embed(title=f"{CAPITAL}" ,colour=0xFF0000)
                embed.set_image(url=data[str(CAPITAL)][f"{INDEX}"])
                await ctx.send(embed=embed)
                #await ctx.send(data[f"{idol}"][f"{INDEX}"])
            elif response.status == 404:
                await ctx.send("Unavailable")



def setup(bot):
    bot.add_cog(API(bot))