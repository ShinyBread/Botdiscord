import discord
import openai
import openai_API
from discord.ext import commands

openai.api_key = openai_API.API

class MelvinGPT(commands.Cog):
    def __init__(self, client):
        self.client= client
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.client.user:
            return
        if message.channel.id==1072614870593323028:
            if message.content.startswith("!pregunta"):
                prompt = message.content

                pregunta_melvin = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=350,
                n=1,
                stop=None,
                temperature=0.6,
                ).choices[0].text
            await message.channel.send(f'MelvinGPT a: {message.author.mention}{pregunta_melvin}')

async def setup(client) -> None:
    await client.add_cog(MelvinGPT(client))