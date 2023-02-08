import discord
from itertools import cycle
from listabaneados import lista_baneados
from discord.ext import commands,tasks
from discord import Member
import TKEN

status = cycle(["En pruebas","Puedo no funcionar","Cuidado"])

class Melvinator_Live(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=discord.Intents().all())

        self.cogslist = ["cogs.tula","cogs.shipeo","cogs.avatar","cogs.melvin","cogs.ochoball","cogs.MessageEvents","cogs.MelvinGPT"]
     
    async def setup_hook(self):
      for ext in self.cogslist:
        if ext not in self.extensions:
          try:
            await self.load_extension(ext)
            print(f'Extension {ext} cargada con éxito')
          except Exception as e:
             print(f'Error al cargar la extensión {ext}\n{e}')
        else:
          print(f'Extension {ext} ya está cargada.')

    
    
    @tasks.loop(seconds=5)
    async def change_status(self):
        await self.change_presence(activity=discord.Game(next(status)))
    
    async def on_ready(self):
        print(f'{self.user} ha entrado!')
        synced = self.cogslist
        print("Slash Commands sincronizados:" + str(len(synced)))
        self.change_status.start()
        await self.setup_hook()

client=Melvinator_Live()
client.run(TKEN.TOKEN)