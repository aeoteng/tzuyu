import discord
import json
from discord.ext import commands


class Storage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['opn'])
    async def open(self, ctx, index):
        with open('./dib/img.json', 'r') as p:
            data = json.load(p)

        for q in data[str(ctx.author.id)]:
            if index == q['index']:
                embed = discord.Embed(
                    title=f"Content: {q['index']}", 
                    description=f"Guild: {q['guildName']}", 
                    colour=discord.Colour.blue()
                )
                embed.set_image(url=q['content'])

                await ctx.send(embed=embed)
                await print(f"Content Requested #: {index}")

            else:
                emojiX = '❌'
                await ctx.message.add_reaction(emojiX)
                await ctx.send("**You don't own this content**", delete_after=5)

    @commands.command()
    async def dm(self, ctx, index):
        with open('./dib/img.json', 'r') as p:
            data = json.load(p)

        for q in data[str(ctx.author.id)]:
            if index == q['index']:
                embed = discord.Embed(title=f"Content: {q['index']}", 
                                      description=f"Guild: {q['guildName']}", 
                                      colour=discord.Colour.blue())
                embed.set_image(url=q['content'])

                emojiTick = '✅'
                await ctx.author.send(embed=embed)
                await ctx.message.add_reaction(emojiTick)
                await print(f"Content Requested #: {index}")

            else:
                emojiX = '❌'
                await ctx.message.add_reaction(emojiX)
                await ctx.send("**You don't own this content**", delete_after=5)


def setup(bot):
    bot.add_cog(Storage(bot))
