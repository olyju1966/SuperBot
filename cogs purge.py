from nextcord.ext import commands
from nextcord import Embed
import asyncio
class Purge(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='purge', help="supprimer les messages d'un salon")
  async def purge(self, ctx, limit = None):
    minperm = [
      'manage'
    ]
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in ctx.author.guild_permissions if p[1]])
    if not any(word in perm_string.lower() for word in minperm): return await ctx.send("Tu n'a pas les perms pour faire cela !")
    if not limit: 
      def check(m):
          return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
      while 1==1:
        await ctx.send("Combien de message veux tu supprimer?")
        nb = await self.bot.wait_for('message', check=check)
        try:
          limit = int(nb.content)
          break
        except ValueError:
          pass
    else:
      try:
        limit = int(limit)
      except ValueError:
        def check(m):
          return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
        while 1 == 1:
          await ctx.send("Combien de message veux tu supprimer?")
          nb = await self.bot.wait_for('message', check=check)
          try:
            limit = int(nb.content)
            break
          except ValueError:
            pass

    await ctx.channel.purge(limit=limit + 1)
    embed=Embed(title="suppression de message",description=f"{limit} messages effacés par {ctx.author.mention}",color=0xFF0000)
    await ctx.send(embed=embed,delete_after=4)
    
    
def setup(bot):
  bot.add_cog(Purge(bot))
