import discord
from discord import app_commands
from dotenv import load_dotenv
import os
from discord.ext import commands
import asyncio

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True # for events on members (join, leave, update, etc.)
intents.message_content = True # required for prefix commands, automod, and anything on raw messages to function

# to add more to ur bot refer to this https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=commands%20bot#discord.ext.commands.Bot
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None, case_insensitive=True, member_cache_flags=discord.MemberCacheFlags.all(), status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name="Set your own"))

@bot.event
async def on_ready(): ### This is called when everything is ready, DO NOT put anything inside here such as presence changes, or loading cogs etc. This is only here for you to know when the bot is ready. 
    print(f"Successfully booted {bot.user.name}")
    await bot.tree.sync() # now, YOU DO NOT do this everytime your bot boots. if your bots public or has bunch of / commands this just spams the discord api and is unecessary dependant on what your bot is

@bot.event
async def setup_hook():
    # if you use cogs, uncomment the lines below
    '''
    for filename in os.listdir('./cogs'): # if your cogs folder isnt /cogs change the ./cogs to ./folder name
        if filename.endswith('.py'):
            cog_name = filename[:-3]
            try:
                await bot.load_extension(f'Loaded cogs.{cog_name}') 
            except Exception as e:
                print(e)
                pass
            print(f"{cog_name} loaded.")
            '''

@bot.command()
async def sync_commands(ctx): # command usage on discord in our instance would be .sync_commands
    await bot.tree.sync()
    await asyncio.sleep(3) # will delay the response from the bot by 3 seconds
    await ctx.send("Synced commands.")

bot.run(BOT_TOKEN)