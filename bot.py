import discord
import os
from discord.ext import commands
import builtins
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True # for events on members (join, leave, update, etc.)
intents.message_content = True # required for prefix commands, automod, and anything on raw messages to function

class Bot(commands.Bot):
    def __init__(self):
        super.__init__()(command_prefix='.', intents=intents, help_command=None, case_insensitive=True, member_cache_flags=discord.MemberCacheFlags.all(), status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="Set your own"))

bot = Bot()
builtins.bot = bot

@bot.event
async def on_ready(): ### This is called when everything is ready, DO NOT put anything inside here such as presence changes, or loading cogs etc. This is only here for you to know when the bot is ready. 
    print(f"Successfully booted.")
    
@bot.event
async def setup_hook():
    # if you use cogs, uncomment the lines below
    '''
    for filename in os.listdir('./cogs'): # if your cogs folder isnt /cogs change the ./cogs to ./folder name
        if filename.endswith('.py'):
            cog_name = filename[:-3]
            try:
                await bot.load_extension(f'Loaded the cog: {cog_name}') 
            except Exception as e:
                print(e)
                pass
            print(f"{cog_name} loaded.")
            '''

@bot.command()
async def ping(ctx):
    await ctx.respond("Pong! {ctx.author.mention}")

async def bot_():
    await bot.start(BOT_TOKEN, reconnect=True)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if __name__ == '__main__':
    asyncio.run(bot_())
