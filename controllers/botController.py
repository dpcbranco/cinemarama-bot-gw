import discord
from config.discordBot import bot
from services import justWatchService
from views.movieSelectionView import getMovieSelectionView

def defineBotCommands():
    @bot.tree.command()
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.nick if interaction.user.nick else interaction.user.name}")

    @bot.tree.command()
    async def search(interaction: discord.Interaction, movie_search: str):
        if movie_search:
            movieOptions = justWatchService.search(query=movie_search)
            if movieOptions:
                await interaction.response.send_message("Escolha o filme:", view=getMovieSelectionView(movieOptions), ephemeral=True) 
            else:
                await interaction.response.send_message("Nenhum filme encontrado :(", ephemeral=True)