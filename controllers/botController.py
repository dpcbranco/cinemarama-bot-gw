from config.discordBot import bot
from services import justWatchService
from views.movieSelectionView import getMovieSelectionView

def defineBotCommands():
    @bot.command()
    async def hello(ctx):
        await ctx.send(f"Hello {ctx.author.nick if ctx.author.nick else ctx.author.name}")

    @bot.command()
    async def search(ctx, *args):
        movieSearch = ' '.join(args)

        if movieSearch:
            movieOptions = justWatchService.search(query=movieSearch)
            await ctx.message.delete()
            if movieOptions:
                await ctx.send("Escolha o filme:", view=getMovieSelectionView(movieOptions)) 
            else:
                await ctx.send("Nenhum filme encontrado :(")