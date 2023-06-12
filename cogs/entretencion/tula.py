import discord
import random
from discord.ext import commands
from discord import app_commands

class tula(commands.Cog):
    def __init__(self, Shinybot:commands.Bot) -> None:
        self.Shinybot=Shinybot
    
    @app_commands.command(
            name='tula', 
            description='indica el porte de tu monstruo'
            )
    
    async def pilin(self, interaction: discord.Interaction, member: discord.Member = None):
        if member == None:
            member = interaction.user

        embed = discord.Embed(title=f"A {member.name} le mide {random.randint(5, 50)}cms")
        await interaction.response.send_message(embed=embed)

async def setup(Shinybot: commands.Bot) -> None:
    await Shinybot.add_cog(tula(Shinybot))