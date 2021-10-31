import discord
import json
from aiohttp import request
from discord.ext import commands


class API(commands.Cog, name='API Commands'):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.is_nsfw()
    @commands.command(
        name='neko',
        aliases=['nsfw']
    )    
    async def pat(self, ctx, image):
        URL = "https://nekos.life/api/v2/img/"
        URL2 = URL + image

        async with request("GET", URL2, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                embed = discord.Embed(
                    description=f" {ctx.author.mention} **requested {image.capitalize()}**",
                    colour=discord.Colour.from_rgb(114, 137, 218))
                embed.set_image(
                    url=data["url"])
                await ctx.send(embed=embed)
                #await ctx.send(data["link"])
            else:
                await ctx.send("Unavailable")



def setup(bot):
    bot.add_cog(API(bot))
    