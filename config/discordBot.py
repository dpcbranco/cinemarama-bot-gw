import discord
import os

from discord.ext import commands

bot = commands.Bot(
    command_prefix="$", intents=discord.Intents.all()
)

@bot.event
async def on_ready():
    print("Bot connected to Discord")
    if os.getenv("ENV") == "LOCAL":
        bot.tree.copy_global_to(guild=discord.Object(id=os.getenv("GUILD_ID")))
        await bot.tree.sync(guild=discord.Object(id=os.getenv("GUILD_ID")))


def runClient(token):        
    bot.run(token)