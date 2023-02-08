import discord
from discord.ext import commands
from listabaneados import lista_baneados

class MessageEvents(commands.Cog):
    def __init__(self, client):
        self.client= client

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.client.user:
            return
        if message.author.id in lista_baneados:
            return
        if "CL" in message.content:
            embed = discord.Embed(title="No hablen del CL, el esta preso")
            await message.channel.send(embed=embed)
        if "tuki" in message.content:
            await message.channel.send("Tuki")
            print("tuki")
        if "Tuki" in message.content:
            await message.channel.send("Tuki")
        if message.content.startswith("Hola"):
            await message.channel.send("Hola!")
        if message.content.startswith("alo"):
            await message.channel.send("alo")
        if message.content.endswith("once"):
            await message.channel.send("chupalo entonce")
        if message.content.endswith("11"):
            await message.channel.send("chupalo entonce")
        if "poto" in message.content:
            await message.channel.send("Poto")

async def setup(client) -> None:
    await client.add_cog(MessageEvents(client))
