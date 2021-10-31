import discord
import json
import random
from discord.ext import commands


class Storage(commands.Cog, name='API Commands'):

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command(
        name='openkpop',
        aliases=['ok']
    )
    async def open(self, ctx, idol):
        with open('./dib/kimg.json', 'r') as p:
            data = json.load(p)



            CAPITAL = str(idol).capitalize()
            MAX = len(data[str(CAPITAL)])
            INDEX = random.randint(0, MAX-1)

            if CAPITAL in data:
                embed = discord.Embed(title=f"{CAPITAL}" ,colour=0xFF0000)
                embed.set_image(url=data[str(CAPITAL)][f"{INDEX}"])
                await ctx.send(embed=embed)
            
         
def setup(bot):
    bot.add_cog(Storage(bot))