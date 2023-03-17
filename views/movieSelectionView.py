import discord
from discord.ui import Button, View

async def button_callback(interaction):
    await interaction.response.send_message("Filme adicionado a sua lista!")

def getMovieSelectionView(movieOptions):
    view = View(timeout=60000)
    options = [Button(label=movieTitle, custom_id=movieId) for movieId, movieTitle in movieOptions.items()]
    for movieOption in options:
        movieOption.callback = button_callback
        view.add_item(movieOption)
    
    return view