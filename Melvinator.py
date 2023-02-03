import discord
import asyncio
import random
from discord import SelectOption
from discord.ext import commands, tasks
from discord import Member
from discord import app_commands
from discord import SelectOption
from discord.ext.commands import has_permissions, MissingPermissions
import TKEN
from respuestas_melvin import respuestasMelvin
from lista_melvins import listaMelvin
from listabaneados import lista_baneados
from webserver import keep_alive
from itertools import cycle
import datetime

button = discord.ui.Button
intents = discord.Intents.all()
Melvinator = commands.Bot(command_prefix='!', intents=intents)
status = cycle(['Tuki', 'tuki'])


@Melvinator.event
async def on_ready():
    print(f'{Melvinator.user} ha entrado!')
    synced = await Melvinator.tree.sync()
    print("Slash Commands sincronizados:" + str(len(synced)))
    change_status.start()


@tasks.loop(seconds=5)
async def change_status():
    await Melvinator.change_presence(activity=discord.Game(next(status)))


@Melvinator.tree.command(name="melvin", description="Genera un melvin al azar")
@app_commands.checks.cooldown(1, 30, key=lambda i: (i.user.id))
async def on_message(interaction: discord.Interaction):
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


@Melvinator.tree.command(name='avatar', description='Muestra avatar del usuario')
async def user_avatar(interaction: discord.Interaction, member: discord.Member = None):
    if member == None:
        member = interaction.user
    if interaction.channel.id == 1020788728781864971:
        embed = discord.Embed(title=f'Avatar de {member.name}')
        embed.set_image(url=member.avatar)
        await interaction.response.send_message(embed=embed)


@Melvinator.tree.command(name='tula', description='indica el porte de tu monstruo')
@app_commands.checks.cooldown(1, 120, key=lambda i: (i.user.id))
async def pilin(interaction: discord.Interaction, member: discord.Member = None):
    if member == None:
        member = interaction.user

    embed = discord.Embed(title=f"A {member.name} le mide {random.randint(5, 50)}cms")
    await interaction.response.send_message(embed=embed)


@Melvinator.event
async def on_message(message):
    args = message.content.split(" ")[1:]
    if message.author == Melvinator.user:
        return

    if "CL" in message.content:
        embed = discord.Embed(title="No hablen del CL, el esta preso")
        await message.channel.send(embed=embed)
    if "tuki" in message.content:
        await message.channel.send("Tuki")
    if "Tuki" in message.content:
        await message.channel.send("Tuki")
    if message.content.startswith("Hola"):
        await message.channel.send("Hola!")
    if message.content.startswith("alo"):
        await message.channel.send("alo")
    if message.content.startswith("alo"):
        await message.channel.send("alo")
    if message.content.endswith("once"):
        await message.channel.send("chupalo entonce")
    if message.content.endswith("11"):
        await message.channel.send("chupalo entonce")
    if "poto" in message.content:
        await message.channel.send("Poto")


@Melvinator.tree.command(name="ship", description="shipea con un user")
@app_commands.checks.cooldown(1, 120, key=lambda i: (i.user.id))
async def on_message(interaction: discord.Interaction, member: discord.Member = None):
    if member == None:
        member = interaction.user

    shipeado = str(random.choice(interaction.guild.members))
    shipeador = str(f'{member.name}#{member.discriminator}')

    embed = discord.Embed(title=f'{shipeador} ha sido shipeado con {shipeado}')
    await interaction.response.send_message(embed=embed)


@Melvinator.tree.command(name="8ball", description='Haceme una pregunta tipo si o no y vere que te contesto')
@app_commands.checks.cooldown(1, 120, key=lambda i: (i.user.id))
async def on_message(interaction: discord.Interaction, *, pregunta: str):
    embed = discord.Embed(title=f'Pregunta: {pregunta}\n Melvin dice: {random.choice(respuestasMelvin)}')
    await interaction.response.send_message(embed=embed)


keep_alive()
Melvinator.run(TKEN.TOKEN)