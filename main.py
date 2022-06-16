import nextcord
from nextcord.ext import commands
import asyncio
import json
from nextcord import Embed

default_intents = nextcord.Intents.default()
default_intents.members = True
owners = () #ids des owner du bot
client = commands.Bot(intents=default_intents, command_prefix=[#prefix du bot], owner_ids=owners, help_command=None)
blacklistfile = 'cogs/json/blacklist.json'
badwordfile = 'badword.txt'
@client.event
async def on_ready():
  global blacklist
  global lkick
  print('Online')
  print('blacklist loading.')
  with open(blacklistfile, 'r') as file:
    print('file opened')
    blacklist = json.load(file)
  print('file loaded beginning all load without console radint')
  while not client.is_closed():
    await asyncio.sleep(10)
    with open(blacklistfile, 'r') as file:
      blacklist = json.load(file)
  await client.change_presence(activity=client.Game(name="faire la commande /help"))

@client.event
async def on_command_completion(ctx):
    await ctx.message.delete()
    
@client.listen()
async def on_message(message):
    with open(badwordfile, "r") as f:
      badwordlist = f.read().split(', ')
    if any(word in message.content.lower() for word in badwordlist):
      await message.delete()
      return await message.channel.send('merci de ne pas dire cela.')
    if message.content == "<@704637292022857780>":
        embed = Embed(title="Mes différents prefix sont", description="`s/<commande>, /<commande>, SuperBot <commande> et superbot <commande>`", color=0xf10404)
        return await message.channel.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound): return await ctx.send("Cette commande n'existe pas")
  elif isinstance(error, commands.BotMissingPermissions): return await ctx.send("Le bot n'a pas la permission nécessaire pour exécuter cette commande!")


@client.event
async def on_message(message):
  if message.author.id == client.user.id: 
      return
  if not message.guild:
    prefixlist = [
      'superbot',
      's/',
      '/'
    ]
    if any(word in message.content.lower() for word in prefixlist):
      await message.author.send('Les commandes en mp ne sont pas la le mp sert uniquement a parler au staff de SuperBot')
  else:
    await client.process_commands(message)

client.run("#token du bot")
