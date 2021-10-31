import os
from keep_alive import keep_alive
from discord.ext import commands

def get_prefix(bot, message):
    pref="!"
    return commands.when_mentioned_or(*pref)(bot, message)

bot = commands.Bot(
	command_prefix=get_prefix,
	case_insensitive=True
)

bot.author_id = 486086967411474433

@bot.remove_command('help')
@bot.event 
async def on_ready():
    print("I'm in")
    print(bot.user)


extensions = [
	'cogs.cog_dev',
    'cogs.api_pat',
    'cogs.api_kpop',
    'cogs.api_wink',
    'cogs.api_neko',
    'cogs.cog_help',
    'cogs.api_page',
    'cogs.dib_save',
    'cogs.dib_open',
    'cogs.sus_save',
    'cogs.sus_open',
    'cogs.api_kiss'
]

if __name__ == '__main__':
	for extension in extensions:
		bot.load_extension(extension)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('> Please use required args or check in **help**')

    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('> Invalid or Unavailable Command')

keep_alive()  # Starts a webserver to be pinged.
my_secret = os.environ['TOKEN']
bot.run(my_secret)  # Starts the 