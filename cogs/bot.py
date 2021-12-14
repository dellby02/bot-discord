import discord
from discord.ext import commands, tasks
from pymongo import MongoClient
from time import sleep
from datetime import date, time, datetime
from pathlib import Path
from utils import check
import os
from pytz import timezone

date_now = datetime.now()
fuso = timezone('America/Sao_Paulo')
date_2 = date_now.astimezone(fuso)
hour = date_2.strftime("%H:%M:%S")
date_now2 = date_2.strftime("%d/%m/%Y")

cluster = MongoClient(os.environ['mongo'])
data = cluster["discord"]["users"]
  
class Bot(commands.Cog):
  def __init__(self, client):
    self.client = client
 
    
  @commands.command()
  async def time(self, ctx):
    meses = {
      "1": "Janeiro",
      "2": "Fevereiro",
      "3": "Março",
      "4": "Abril",
      "5": "Maio",
      "6": "Junho",
      "7": "Julho",
      "8": "Agosto",
      "9": "Setembro",
      "10": "Outubro",
      "11": "Novembro",
      "12": "Dezembro"
    }
    data = date_now2.month
    
    if data == 1:
      data = meses['1']
    elif data == 2:
      data = meses['2']
    elif data == 3:
      data = meses['3']
    elif data == 4:
      data = meses['4']
    elif data == 5:
      data = meses['5']
    elif data == 6:
      data = meses['6']
    elif data == 7:
      data = meses['7']
    elif data == 8:
      data = meses['8']
    elif data == 9:
      data = meses['9']
    elif data == 10:
      data = meses['10']
    elif data == 11:
      data = meses['11']
    elif data == 12:
      data = meses['12']
    
    hora = hour
    
    embed = discord.Embed(title="Data e Hora | ☀️" if now.hour <= 17 else "Data e Hora | 🌃", color=0xf49e12 if now.hour <= 17 else 0xe6e1d7
    )
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/876156458817978378/919731090455920701/download_1.png")
    embed.add_field(
      name ="📆 | Data", value="{} de {} de {}".format(date_now2.day, data, date_now2.year)
      )
    embed.add_field(
      name = "⏰ | Hora", value= "{}".format(hora)
      )
    embed.set_footer(text="{} | Hoje às {}:{}".format(ctx.author.id, hour, now.minute), icon_url=ctx.author.avatar_url)
    
    await ctx.send(embed=embed)
    
    
  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == message.author.bot:
      return
    
    stats = cluster["discord"]["stats"]
    guilds = cluster["discord"]["guilds"]
    users = cluster["discord"]["users"]
    
    if message:
      check_user = users.find_one({"id": message.author.id})
      if check_user is None:
        
        users.insert_one(
          {
            "id": message.author.id,
            "user_name": message.author.name,
            "user_discriminator": message.author.discriminator,
            "type": "User"
          })
     
      if message.guild:
        check_guild = guilds.find_one({"id": message.guild.id})
        
        if check_guild is None:
          
          guilds.insert_one(
            {
              "id": message.guild.id,
              "guild_name": message.guild.name,
              "owner_guild": message.guild.owner_id,
              "type": "Guild"
            })

    
def setup(client):
  client.add_cog(Bot(client))
