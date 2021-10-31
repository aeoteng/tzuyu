import discord
import json
#import random
from discord.ext import commands


class Storage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(aliases=['sk'])
    async def savekpop(self, ctx, idol, *, content):
        with open('./dib/kimg.json', 'r') as p:
            data = json.load(p)

        CAPITAL = str(idol).capitalize()

        if CAPITAL not in data:

            data[CAPITAL] = {}
            data[CAPITAL][str(0)] = str(content)

            with open('./dib/kimg.json', 'w') as p:
                json.dump(data, p, sort_keys=True,
                          indent=4, separators=(',', ': '))

            emojiTick = '✅'
            await ctx.message.add_reaction(emojiTick)
            #await print(f'Content Upload #: {}')
        
        elif CAPITAL in data:

            MAX = len(data[CAPITAL])
            INDEX = MAX + 1

            data[CAPITAL][str(INDEX)] = str(content)

            with open('./dib/kimg.json', 'w') as p:
                json.dump(data, p, sort_keys=True,
                          indent=4, separators=(',', ': '))

            emojiTick = '✅'
            #await ctx.message.add_reaction(emojiTick)
            await ctx.send(f"Uploaded in the **{CAPITAL}** Dictionary")
            #await print(f'Content Upload #: {index}')

        else:
            emojiX = '❌'
            await ctx.message.add_reaction(emojiX)
            #await ctx.send(f"{index} was already taken", delete_after=5)


def setup(bot):
    bot.add_cog(Storage(bot))
