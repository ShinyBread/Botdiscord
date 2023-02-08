import discord
import random
from discord.ext import commands
from discord import app_commands
from respuestas_melvin import respuestasMelvin

class ochoball(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="8ball", description='Haceme una pregunta tipo si o no y vere que te contesto')
    @app_commands.checks.cooldown(1, 120, key=lambda i: (i.user.id))
    async def ochoball(self, interaction: discord.Interaction, *, pregunta: str):
      embed = discord.Embed(title=f'Pregunta: {pregunta}\n Melvin dice: {random.choice(respuestasMelvin)}')
      await interaction.response.send_message(embed=embed)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(ochoball(client))