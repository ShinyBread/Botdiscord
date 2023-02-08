import discord
import random
from discord.ext import commands
from discord import app_commands

class shipeo(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
    @app_commands.command(name="shipeo", description="shipea con un user")
    @app_commands.checks.cooldown(1, 120, key=lambda i: (i.user.id))
    async def on_message(self, interaction: discord.Interaction, member: discord.Member = None):
      if member == None:
        member = interaction.user

      shipeado = str(random.choice(interaction.guild.members))
      shipeador = str(f'{member.name}#{member.discriminator}')

      embed = discord.Embed(title=f'{shipeador} ha sido shipeado con {shipeado}')
      await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(shipeo(client))