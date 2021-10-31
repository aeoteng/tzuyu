import discord
from discord.ext import commands
import random
from aiohttp import request
import DiscordUtils

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Commands
    @commands.command()
    async def help(self, ctx):
        URL = "https://api.maknae.xyz/v1/idols/all/"
         
        async with request("GET", URL, headers={}) as response:
            if response.status == 200:
                data = await response.json()

                MAX = len(data["Tzuyu"])
                INDEX = random.randint(0, MAX-1)

                Normal_embed = discord.Embed(
                    title="Normal Commands",
                    description="Usable in all channels",
                    color=ctx.author.color)
                Normal_embed.set_thumbnail(url=data["Tzuyu"][f"{INDEX}"])
                Normal_embed.add_field(
                    name="kpop [idol name]",
                    value="Idol names are dependent on the Maknae API",
                    inline=False
                )
                Normal_embed.add_field(
                    name="wink [@mention]",
                    value="This simply just winks at who is tagged",
                    inline=False
                )
                Normal_embed.add_field(
                    name="pat [@mention]",
                    value="This simply just pats on who is tagged",
                    inline=False
                )
                Neko_embed = discord.Embed(
                    title="NEKO Commands",
                    description="Only usable in NSFW channels",
                    color=ctx.author.color
                )
                Neko_embed = discord.Embed(
                    title="NEKO Commands",
                    description="Only usable in NSFW channels",
                    color=ctx.author.color)
                Neko_embed.set_thumbnail(url=data["Tzuyu"][f"{INDEX}"])
                Neko_embed.add_field(
                    name="neko [NSFW args]",
                    value='''solog, feet, smallboobs, lewdkemo, gasm, solo, cum, les,erokemo, bj, pwankg, ero, hololewd, gecg, holo, tits, nsfw_neko_gif, eroyuri, holoero, pussy, Random_hentai_gif, yuri, keta, hentai, feetg, eron, erok, kemonomimi, cum_jpg, nsfw_avatar, erofeet, blowjob, spank, kuni, femdom, boobs, trap, lewd, pussy_jpg, anal, futanari, ngif, lewdk
                    ''',
                    inline=False
                )
                Neko_embed.add_field(
                    name="neko [SFW args]",
                    value='''smug, woof, 8ball, goose, cuddle, avatar, slap, pat, poke, feed, fox_girl, lizard, neko, baka, hug, meow, kiss, wallpaper, tickle, classic, waifu
                    ''',
                    inline=False
                )
                DEV_embed = discord.Embed(
                    title="DEV Commands",
                    description="Usable only by OWNER",
                    color=ctx.author.color)
                DEV_embed.set_thumbnail(url=data["Tzuyu"][f"{INDEX}"])
                DEV_embed.add_field(
                    name="n/a",
                    value="n/a",
                    inline=False
                )
	   	
                paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
                paginator.add_reaction('⏮️', "first")
                paginator.add_reaction('⏪', "back")
                paginator.add_reaction('🔐', "lock")
                paginator.add_reaction('⏩', "next")
                paginator.add_reaction('⏭️', "last")
                embeds = [Normal_embed, Neko_embed, DEV_embed]
                await paginator.run(embeds)

            elif response.status == 404:
                await ctx.send("Unavailable")
       
def setup(bot):
    bot.add_cog(Help(bot))