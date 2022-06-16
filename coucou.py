from nextcord.ext import commands

class Coucou(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def coucou(self, ctx):
    await ctx.send('coucou')

def setup(bot):
  bot.add_cog(Coucou(bot))
