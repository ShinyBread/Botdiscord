import discord
from discord.ext import commands
from discord import app_commands

class test(commands.Cog):
    def __init__(self, Shinybot:commands.Bot) -> None:
        self.Shinybot=Shinybot

    @app_commands.command(
        name= "test",
        description="prueba el bot"
    )
    async def test(self, interaction: discord.Interaction, texto: str, numero: int) -> None:
        await interaction.response.send_message(f'string: {texto} y numero: {numero}')

async def setup(Shinybot: commands.Bot) -> None:
    await Shinybot.add_cog(test(Shinybot))
