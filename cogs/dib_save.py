import discord
import json
from discord.ext import commands


class Storage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['upl'])
    async def save(self, ctx, index, *, content):
        with open('./dib/img.json', 'r') as p:
            data = json.load(p)

        if str(ctx.author.id) not in data:

            data[str(ctx.author.id)] = []
            data[str(ctx.author.id)].append({
                'authorID': int(ctx.author.id),
                'content': str(content),
                'index': int(index),
                'guildID': int(ctx.guild.id),
                'guildName': str(ctx.guild.name)
                })

            with open('./dib/img.json', 'w') as p:
                json.dump(data, p, sort_keys=True,
                          indent=4, separators=(',', ': '))

            emojiTick = '✅'
            await ctx.message.add_reaction(emojiTick)
            await print(f'Content Upload #: {index}')
        
        elif str(ctx.author.id) in data:
            data[str(ctx.author.id)].append({
                'authorID': int(ctx.author.id),
                'content': str(content),
                'index': int(index),
                'guildID': int(ctx.guild.id),
                'guildName': str(ctx.guild.name)
                })

            with open('./dib/img.json', 'w') as p:
                json.dump(data, p, sort_keys=True,
                          indent=4, separators=(',', ': '))

            emojiTick = '✅'
            await ctx.message.add_reaction(emojiTick)
            await print(f'Content Upload #: {index}')

        else:
            emojiX = '❌'
            await ctx.message.add_reaction(emojiX)
            await ctx.send(f"{index} was already taken", delete_after=5)


def setup(bot):
    bot.add_cog(Storage(bot))
