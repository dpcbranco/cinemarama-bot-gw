import discord

from discord.ext import commands

bot = commands.Bot(
    command_prefix="$", intents=discord.Intents.all()
)

@bot.event
async def on_ready():
    print("Bot connected to Discord")


def runClient(token):        
    bot.run(token)