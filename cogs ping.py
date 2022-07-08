from nextcord.ext import commands
from nextcord import Embed
class Ping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='ping', help='voir en combien de temps le bot mets pour répondre')
  async def ping(self, ctx):
    embed=Embed(title='Pong !', description="Le ping est de "+str(round(self.bot.latency*1000))+" millisecondes" , color=0xFF5733).set_author(name="SuperBot", icon_url="https://cdn.discordapp.com/avatars/704637292022857780/074923f70804e0b7a8a99f2b7320223e.webp?size=1024")
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Ping(bot))
