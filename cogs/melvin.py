import discord
import discord
import asyncio
import random
from discord.ext import commands
from discord import app_commands
from lista_melvins import listaMelvin

class melvin(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="melvin", description="Genera un melvin al azar")
    @app_commands.checks.cooldown(1, 30, key=lambda i: (i.user.id))
    async def generar_melvin(self, interaction: discord.Interaction):
        embed = discord.Embed(title=f'al {interaction.user.name} le gusta el pico')
        afortunado = str(random.choice(interaction.guild.members))
        autor = str(f'{interaction.user.name}#{interaction.user.discriminator}')
        print(autor, afortunado)  # esta weas es pa testear

        if autor == afortunado:
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.defer()
            await asyncio.sleep(0.1)
            await interaction.followup.send(random.choice(listaMelvin))


async def setup(client: commands.Bot) -> None:
    await client.add_cog(melvin(client))