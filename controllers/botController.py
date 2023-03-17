from config.discordClient import client

def defineBotCommands():
    @client.command()
    async def hello(ctx):
        await ctx.send(f"Hello {ctx.author.nick}")