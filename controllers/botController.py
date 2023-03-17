from config.discordClient import client
from services import justWatchService
from views.movieSelectionView import getMovieSelectionView

def defineBotCommands():
    @client.command()
    async def hello(ctx):
        await ctx.send(f"Hello {ctx.author.nick}")

    @client.command()
    async def search(ctx, *args):
        movieSearch = ' '.join(args)
        
        if movieSearch:
            movieOptions = justWatchService.search(query=movieSearch)
            await ctx.message.delete()
            await ctx.send("Escolha o filme:", view=getMovieSelectionView(movieOptions))