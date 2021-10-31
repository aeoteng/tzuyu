import discord
import json
from aiohttp import request
from discord.ext import commands


class API(commands.Cog, name='API Commands'):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(
        name='pat',
        aliases=['boop']
    )    
    async def pat(self, ctx, member: discord.Member):
        URL = "https://some-random-api.ml/animu/pat"

        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(
                    description=f" {ctx.author.mention} **pats** {member.mention}",
                    colour=discord.Colour.from_rgb(114, 137, 218))
                embed.set_image(
                    url=data["link"])
                await ctx.send(embed=embed)
                #await ctx.send(data["link"])
            else:
                await ctx.send("Unavailable")



def setup(bot):
    bot.add_cog(API(bot))