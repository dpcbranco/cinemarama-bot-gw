import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")

client = commands.Bot(
    command_prefix="$", intents=discord.Intents.all()
)

@client.event
async def on_ready():
    print("Bot connected to Discord")

client.run(token)