import discord
import openai
import openai_API
from discord.ext import commands

openai.api_key = openai_API.API

class MelvinGPT(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.conversations = {}

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.channel.id == 1072614870593323028 and message.content.endswith("."):
            channel_id = str(message.channel.id)
            if channel_id not in self.conversations:
                self.conversations[channel_id] = []  # initialize conversation history for this channel
            mensajes = self.conversations[channel_id]
            mensaje_de_sistema="Your name is Melvinator and you are friendly and with a lot of sense of humor, your answers are short but precise. Your main language is spanish, but you are very good with other languages."
            mensajes.append({"role": "system", "content": mensaje_de_sistema })
            mensaje=message.content
            mensajes.append({"role": "user", "content": mensaje})
            
            # Call the OpenAI API to generate a response
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=mensajes)
            respuesta = response["choices"][0]["message"]["content"]
            mensajes.append({"role": "assistant", "content": respuesta})
            self.conversations[channel_id] = mensajes  # update conversation history for this channel
            await message.channel.send(respuesta)

async def setup(client) -> None:
    await client.add_cog(MelvinGPT(client))
