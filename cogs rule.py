from nextcord.ext import commands
from nextcord import Embed
class Réglement(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='réglement', help='réglement deja tout fait avec une reaction a cocher')
  async def réglement(self, ctx):
    minperm = [
      'admin'
    ]
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in ctx.author.guild_permissions if p[1]])
    if not any(word in perm_string.lower() for word in minperm): return await ctx.send("Tu n'a pas les perms pour faire cela !")
    embed = Embed(title='réglement du serveur', description="merci de respecter le reglement et de cliquer sur la reaction", colour=0xe74c3c).add_field(name = "1. insulte", value = "intedit d'insulter que se soit en voc ou dans les channel", inline=False).add_field(name = "2. spam", value = "interdit de spam dans les channel sauf dans ceux prevu pour le spam", inline=False)  .add_field(name = "3. question personnel", value = "merci de ne poser aucune question sur : le nom? l'âge, localiter,...", inline=False).add_field(name = "4. pub:", value = "merci de ne pas faire de pub dans le serveur sauf dans les channel prevu pour les pubs", inline=False) .add_field(name = "5. menace:", value = "intedit de menacer un membre ou le staff du serveur", inline=False).add_field(name = "6. copiage de pseudo:", value = "interdit de se faire passer pour un autre membre du serveur", inline=False).add_field(name = "7. racisme et autre:", value = "merci de ne pas faire des propos rasiste ou sexisme dans le serveur", inline=False)
    
    message = await ctx.send(embed=embed)
    await message.add_reaction('✅')
    

def setup(bot):
  bot.add_cog(Réglement(bot))
  
#reglement deja fait
