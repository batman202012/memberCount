from typing import Literal
from redbot.core import commands
from redbot.core import checks
from redbot.core.bot import Red
from redbot.core.config import Config
import discord
import asyncio

class memberCount(commands.Cog):
     """
     Member Count Cog
     """

     def __init__(self, bot: Red) -> None:
          self.bot = bot
          self.config = Config.get_conf(
               self,
               identifier=None,
               force_registration=True,
          )
    
     async def members(self, ctx):
          activeGuilds = self.bot.guilds
          channel = self.bot.get_channel(<channel id>)
          sum = 0
          for s in activeGuilds:
              sum += len(s.members)
          await channel.edit(name='❎ MEMBERS: {} ❎'.format(int(sum)))
          print("count adjusted")
          await asyncio.sleep(1)
          
     @commands.Cog.listener()
     async def on_member_join(self, member):
          print("joined")
          await self.members()

     @commands.Cog.listener()
     async def on_member_remove(self, member):
          print("left")
          await self.members()
    

                    
