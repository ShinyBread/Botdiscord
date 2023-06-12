import discord
import random
from discord.ext import commands
from discord import app_commands
from respuestas_bot import respuestasBot

class ochoball(commands.Cog):
    def __init__(self, Shinybot:commands.Bot) -> None:
        self.Shinybot=Shinybot
    
    @app_commands.command(
            name="8ball", 
            description='Haceme una pregunta tipo si o no y vere que te contesto'
            )
    @app_commands.checks.cooldown(1, 15, key=lambda i: (i.user.id))
    
    async def ochoball(self, interaction: discord.Interaction, *, pregunta: str):
        embed = discord.Embed(title=f'Pregunta: {pregunta}\n Melvin dice: {random.choice(respuestasBot)}')
        await interaction.response.send_message(embed=embed)

async def setup(Shinybot: commands.Bot) -> None:
    await Shinybot.add_cog(ochoball(Shinybot))