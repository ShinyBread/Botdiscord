import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
import aiohttp
from itertools import cycle

load_dotenv("Token.env")  
TOKEN = os.getenv('TOKEN')

status = cycle(["Tuki", "tuki"])

class ShinyBotTest(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=discord.Intents.all(),
            application_id=1115333103213355030
        )
        self.initial_extensions = []

    async def setup_extensions(self):
        for folder_name in os.listdir("cogs"):
            if os.path.isdir(os.path.join("cogs", folder_name)):
                for filename in os.listdir(os.path.join("cogs", folder_name)):
                    if filename.endswith(".py"):
                        cog = f"cogs.{folder_name}.{filename[:-3]}"
                        self.initial_extensions.append(cog)
                        await self.load_extension(cog)
                        print(f"Loaded cog: {cog}")
        await Shinybot.tree.sync()
    
    @tasks.loop(seconds=5)
    async def change_status(self):
        await self.change_presence(activity=discord.Game(next(status)))

    async def close(self):
        await super().close()
        await self.session.close()

    async def on_ready(self):
        print(f'{self.user} está listo!')
        await self.setup_extensions()

Shinybot = ShinyBotTest()
Shinybot.run(TOKEN)
