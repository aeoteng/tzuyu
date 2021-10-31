import discord
import json
from aiohttp import request
from discord.ext import commands


class API(commands.Cog, name='API Commands'):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(
        name='kiss', 
        aliases=['smooch']
    )
    async def kiss(self, ctx, member: discord.Member):
        URL = "https://nekos.life/api/v2/img/kiss"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(
                    description=f" {ctx.author.mention} **kissed ** {member.mention}",
                    colour=ctx.author.color)
                embed.set_image(
                    url=data["url"])
                await ctx.send(embed=embed)
                #await ctx.send(data["link"])
            else:
                await ctx.send("Unavailable")



def setup(bot):
    bot.add_cog(API(bot))