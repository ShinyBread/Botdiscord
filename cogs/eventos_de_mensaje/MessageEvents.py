import discord
from discord.ext import commands

class MessageEvents(commands.Cog):
    def __init__(self, Shinybot: commands.Bot) -> None:
        self.Shinybot = Shinybot
        self.respuestas = {
            "CL": (discord.Embed(title="No hablen del CL, él está preso"), False),
            "tuki": ("Tuki", False),
            "Tuki": ("Tuki", False),
            "Hola": ("Hola!", "startswith"),
            "alo": ("alo", "startswith"),
            "once": ("chupalo entonce", "endswith"),
            "11": ("chupalo entonce", "endswith"),
            "poto": ("Poto", False)
        }

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.Shinybot.user:
            return

        content = message.content

        for keyword, (respuesta, match_type) in self.respuestas.items():
            if match_type == "startswith" and content.startswith(keyword):
                if isinstance(respuesta, discord.Embed):
                    await message.channel.send(embed=respuesta)
                else:
                    await message.channel.send(respuesta)
                break
            elif match_type == "endswith" and content.endswith(keyword):
                if isinstance(respuesta, discord.Embed):
                    await message.channel.send(embed=respuesta)
                else:
                    await message.channel.send(respuesta)
                break
            elif match_type is False and keyword in content:
                if isinstance(respuesta, discord.Embed):
                    await message.channel.send(embed=respuesta)
                else:
                    await message.channel.send(respuesta)
                break

async def setup(Shinybot: commands.Bot) -> None:
    await Shinybot.add_cog(MessageEvents(Shinybot))