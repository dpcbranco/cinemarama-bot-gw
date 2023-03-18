import os
from dotenv import load_dotenv
from config.discordBot import runClient
from controllers.botController import defineBotCommands

if os.getenv("ENV") == "LOCAL":
    load_dotenv()
token = os.getenv("DISCORD_BOT_TOKEN")

defineBotCommands()
runClient(token=token)