import discord

from discord.ext import commands

client = commands.Bot(
    command_prefix="$", intents=discord.Intents.all()
)

@client.event
async def on_ready():
    print("Bot connected to Discord")


def runClient(token):        
    client.run(token)