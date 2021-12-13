import discord
from discord.ext import commands, tasks
from discord.ext.commands import AutoShardedBot
import os
from manter_vivo import manter_vivo
#import config
import dns.resolver

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

intents = discord.Intents.default()
intents.members = True

client: discord.Client() = AutoShardedBot(command_prefix="!", case_insensitive = True, intents=intents)
#client.remove_command("help")

@client.event
async def on_ready():
  ready_message = "\033[1;32m• O seu Bot está Online! •\033[m\n{}\n\033[1;30m->\033[m\033[1;31mNome do Bot: {}".format("=" * 20, client.user.id)
  print(ready_message)
  game = discord.Streaming(name="😳 | Observando se as lolis estão no porão.", url="https://twitch.tv/123")
  await client.change_presence(
    status= discord.Status.online,
    activity=game
  )
  
  
  
for file in os.listdir("./cogs"):
  if file.endswith(".py"):
    client.load_extension(f'cogs.{file[:-3]}')

manter_vivo()
client.run(os.environ['token'])