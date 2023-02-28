import discord
from itertools import cycle
from discord.ext import commands, tasks
from webserver import keep_alive
import TKEN
import os

status = cycle(["Tuki", "tuki", "Melvinator_V.1.2!!"])

class Melvinator_Live(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents().all())

    async def load_cogs(self):
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                cog_name = file[:-3]
                try:
                    await self.load_extension(f"cogs.{cog_name}")
                    print(f"Extension {cog_name} loaded successfully")
                except Exception as e:
                    print(f"Failed to load extension {cog_name}: {e}")
    
    @tasks.loop(seconds=5)
    async def change_status(self):
        await self.change_presence(activity=discord.Game(next(status)))
    
    async def on_ready(self):
        print(f"{self.user} has logged in.")
        await self.load_cogs()
        self.change_status.start()

client = Melvinator_Live()

keep_alive()
client.run(TKEN.TOKEN)
