from config.discordClient import client
from services import justWatchService
from views.movieSelectionView import getMovieSelectionView

def defineBotCommands():
    @client.command()
    async def hello(ctx):
        await ctx.send(f"Hello {ctx.author.nick}")

    @client.command()
    async def search(ctx, *args):
        movieOptions = justWatchService.search(query=' '.join(args))
        await ctx.send("Escolha o filme:", view=getMovieSelectionView(movieOptions))