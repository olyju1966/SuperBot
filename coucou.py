from discord.ext import commands
from requests import post
client = commands.Bot(command_prefix='/', description="Bot de ")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="faire la commande /help"))
    print(f"Bot prêt, {len(client.guilds)} serveurs")

@client.command()
async def coucou(ctx):
    payload: dict = {
      'content': "coucou"
    }
    post(f'https://discord.com/api/v10/channels/{ctx.channel.id}/messages', headers={'authorization': 'Bot ' + "token"}, data=payload)
    
client.run("token")
