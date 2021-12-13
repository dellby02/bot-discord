import discord
from discord.ext import commands
import random
#from config import adiction, division, mult, resto, percentage
from config import potencia, raiz, sub
from datetime import datetime, date, time, timedelta

class Utility(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=("rl",))
  async def rateloli(self, ctx, *, user: discord.Member):
    
    if rate < 5:
      embed = discord.Embed(
        description=f'<@{ctx.author.id}>, a classificação de {user.mention} caiu em `{rate}`, então eu diria que ele(a) é uma péssima loli.', 
        color=0xff2324,
        title= "🤠 | Que chato..."
        )
      embed.set_footer(text=f"A pedido de: {ctx.author.id}", icon_url=ctx.author.avatar_url)
      embed.set_thumbnail(url=user.avatar_url)
      await ctx.send(embed=embed)
      
    if rate >= 6:
      embed = discord.Embed(
        description=f'<@{ctx.author.id}>, a classificação de {user.mention} caiu em `{rate}`, ulala.. que tal vir pro porão ? 😳', 
        color=0xff2324,
        title = "😳 | Oo-ni-chan?"
        )
      embed.set_footer(text=f"A pedido de: {ctx.author.id}", icon_url=ctx.author.avatar_url)
      embed.set_thumbnail(url=user.avatar_url)
      await ctx.send(embed=embed)
    
  
  @rateloli.error
  async def on_rateloli_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(description="Você precisa mencionar o usuário.", color=0xff0000)
      await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
      embed = discord.Embed(
        description="O usuário que você mencionou não existe ou você mencionou errado",
        color= 0xff0000
        )
      await ctx.send(embed=embed)

  @commands.command(aliases=("rg",))
  async def rategay(self, ctx, *, user: discord.Member):
      
    rate = random.randint(0, 10)
    
    if rate < 5:
      embed = discord.Embed(
        description=f'<@{ctx.author.id}>, a classificação de {user.mention} caiu em `{rate}`, então eu diria que ele não é gay.', 
        color=0xff2324,
        title= "👊 | Então é macho!"
        )
      embed.set_footer(text=f"A pedido de: {ctx.author.id}", icon_url=ctx.author.avatar_url)
      embed.set_thumbnail(url=user.avatar_url)
      await ctx.send(embed=embed)
      
    if rate >= 6:
      embed = discord.Embed(
        description=f'<@{ctx.author.id}>, a classificação de {user.mention} caiu em `{rate}`, e cara.. vamo assumir logo? 😳', 
        color=0xff2324,
        title= "🏳️‍🌈 | Vai assumir quando?"
        )
      embed.set_footer(text="A pedido de: {} | Hoje às {}:{}".format(ctx.author.name, datetime.now().hour, datetime.now().minute), icon_url=ctx.author.avatar_url)
      embed.set_thumbnail(url=user.avatar_url)
      await ctx.send(embed=embed)
  
  @rategay.error
  async def on_rategay_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(description="Você precisa mencionar o usuário.", color=0xff0000)
      await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
      embed = discord.Embed(
        description="O usuário que você mencionou não existe ou você mencionou errado",
        color= 0xff0000
        )
      await ctx.send(embed=embed)
  
  @commands.command()
  async def userinfo(self, ctx, user: discord.User = None):
    if user is None:
      user = ctx.author
    data_str = "%d/%m/%Y às %H:%M:%S"
    joined = user.joined_at.strftime(data_str)
    embed = discord.Embed(color=0xff0000, url=user.avatar_url)
    embed.set_author(name=user, url="https://i.imgur.com/YoZl5ef.png")
    embed.add_field(
      name = "🆔 do Discord", value= "`{}`".format(user.id), inline=False
      )
    embed.add_field(
      name = "🏷️ | Nome no Discord", value= "{}".format(user.name), inline = False
      )
    embed.add_field(
      name = "👤 Entrou Aqui", value= "{}".format(joined)
      )
    await ctx.send(embed=embed)
      

def setup(client):
  client.add_cog(Utility(client))