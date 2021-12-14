# ========================================================== #
import discord
from discord.ext import commands
from pymongo import MongoClient
import time
import random
import os
from datetime import date, time, datetime, timedelta
from utils import inc_bal, is_register, rev_bal, rev_coin, check
# ========================================================== #
cluster = MongoClient(os.environ['mongo'])
economy = cluster["discord"]["economy"]
date_string = '31-01-2020 14:45:37'
format_str = '%d-%m-%Y %H:%M:%S'
datetime.strptime(date_string, format_str)
now = datetime.now()


# ========================================================== #
class Economy(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_message(self, msg):
    member = is_register(msg.author.id)
    
    if member is None:
      economy.insert_one(
        {
          "id": msg.author.id,
          "money": 300,
          "ycoin": 0
        })
    else:
      if msg.author.bot == True:
        economy.delete_one({"id": msg.author.id})
# ========================================================== ======= #
  @commands.command()
  #@commands.cooldown(1, 60+120, commands.BucketType.user)
  async def work(self, ctx):
    user = is_register(ctx.author.id)
    quant = int(random.randint(300, 690))
    embed = discord.Embed(title= "{} | Trabalho Justo!".format(check("luffy")), description="Foi difícil, mas isto lhe rendeu {}{}!".format(quant, check("berries")), color=0xff0000)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    d = user['money'] + quant
    inc_bal(d, ctx.author.id)
    await ctx.send(embed=embed)
  
  """@work.error
  async def on_work_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      tempo = timedelta(minutes=+360)
      tzd = tempo + now
      embed = discord.Embed(description= "Epa! Você deve esperar {} **minutos** para utilizar o comando novamente!".format(tzd.minute), color=0xff2323)
      await ctx.send(embed=embed)"""
    
  @commands.command(aliases=("bal",))
  async def balance(self, ctx):
    in2c = is_register(ctx.author.id)
    embed = discord.Embed(title=f"{ctx.author.name}'s Balance", color=0xff4444)
    embed.add_field(
      name = "{} Berries".format(check("berries")),
      value = f"{in2c['money']} Berries"
      )
    embed.add_field(
      name = "💎 Gemas", value = "{} gemas".format(in2c['ycoin'])
      )
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
 
  @commands.group()
  async def bank(self, ctx):
    pass
 
  @commands.is_owner()
  @bank.command(aliases=('a',))
  async def add(self, ctx, user: discord.User, count: int):
    member = is_register(user.id)
    if member is None:
      return await ctx.send("Usuário não registrado.")
    
    if count < 0:
      return await ctx.send("O valor deve ser positivo!")
    else:
      inc_bal(count, user.id)
      await ctx.send("Foram adicionados `{}` {} ao banco de {}!".format(count, check("berries"), f"**{user}**"))
      
  @commands.is_owner()
  @bank.command(aliases=("r",))
  async def remove(self, ctx, user: discord.User, count: int):
    ed = is_register(user.id)
    if ed is None:
      return await ctx.send("Usuário não registrado!")
    if count < 0:
      return await ctx.send("O valor deve ser positivo!")
    else:
      rev_bal(count, user.id)
      await ctx.send("Foram removidos `{}` {} berries de {}!".format(count, check("berries"), user))
  
  
  @bank.command(
    name = "reset",
    description = "Reseta todo seu money em troca de coins!", aliases = ("re",)
    )
  async def reset(self, ctx, user: discord.User):
    member = is_register(user.id)
    if user.id != ctx.author.id:
      return await ctx.send("Eiei! parei aí, você não pode resetar o money de outra pessoa!")
    if member['money'] == 0:
      return await ctx.send("Você não pode usar isto, pois você não tem **money** suficiente para esta ação!")
    if member is None:
      return await ctx.send("Você não está registrado!")
    else:
      #check = member['money']+(member['ycoin']%2)
      rev_bal(member['money'], user.id)
      rev_coin(member['ycoin'], user.id)
      #inc_coin(check, user.id)
      await ctx.send("Todo seu dinheiro foi resetado!")
   
def setup(client):
  client.add_cog(Economy(client))
