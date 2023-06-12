import discord
from discord.ext import commands
from discord import app_commands

class test(commands.Cog):
    def __init__(self, Shinybot:commands.Bot) -> None:
        self.Shinybot=Shinybot

    @app_commands.command(
        name= "introduce",
        description="describete"
    )
    async def introduce(self, interaction: discord.Interaction, nombre: str, edad: int) -> None:
        await interaction.response.send_message(f'Mi nombre es: {nombre} y mi edad es: {edad}')

async def setup(Shinybot: commands.Bot) -> None:
    await Shinybot.add_cog(test(Shinybot))
