import json # For interacting with json
from pathlib import Path # For paths
import platform # For stats
import logging
import json
import asyncio
import discord
import inspect
import random
import datetime
import youtube_dl 
import time
import os
from discord.ext.commands import has_permissions, MissingPermissions, BotMissingPermissions


from discord.ext import commands
from discord.utils import get

client = commands.Bot(
    command_prefix='/',
    description="Bot de ",
    owner_ids=()#id des owner
)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="faire la commande /help"))
    print(f"Bot prêt, {len(client.guilds)} serveurs")

@client.command()
async def coucou(ctx):
    """ renvoit coucou """
    
    await ctx.send("coucou")
    
    def read_json(filename):
    with open(f"{filename}.json", "r") as f:
        data = json.load(f)
    return data

def write_json(data, filename):
    with open(f"{filename}.json", "w") as f:
        json.dump(data, f, indent=4)

def get_token() -> Optional[str]:
    if client.is_ready():
        return

    with open("token") as f:
        return f.read()
    
client.run(get_token())
