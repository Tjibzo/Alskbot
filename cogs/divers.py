import discord
from discord.ext import commands
import random

class Divers(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command(
        name = "bienvenue",
        description = "Cette commande permet de souhaiter la bienvenue à un nouveau membre !",
        usage = "@mention"
    )
    # créer la commande !bienvenue
    async def bienvenue_command(self,ctx, new_member: discord.Member):
        membre = ctx.message.author
        print(f"{membre} used the 'bienvenue' command")
        # récupère le nom
        pseudo = new_member.mention
        # exécuter le message de bienvenue
        await ctx.send(f"Bienvenue à {pseudo} sur le serveur discord ! N'oublie pas de faire la commande `$regles`")
        return


    @commands.command(
        name = "regles",
        description = "Cette commande permet de faire une liste des règles du server."
    )
    # créer la commande !regles
    async def regles_command(self,ctx):
        membre = ctx.message.author
        print(f"{membre} used the 'regles' command")
        await ctx.send("Les règles:\n1.Pas d'insultes\n2.Pas de double compte\n3.Pas de spam")
        return


    @commands.command(
        name = "tjibzo",
        description = "Cette commande sers à en savoir plus sur mon créateur !"
    )
    async def tjibzo_command(self,ctx):
        membre = ctx.message.author
        print(f"{membre} used the 'tjibzo' command")
        await ctx.send("Mon créateur est Tjibzo.\n" \
            "Elle est passionnée par l'informatique, la physique et les maths. Elle aime aussi faire des montages vidéos.\n" \
                "Ses deux devises sont :\n" \
                    "> Ce qui ne me tue pas me rend plus fort(e)\n" \
                        "> Je gagne ou j'apprends, mais je ne perd jamais")
        return


def setup(bot):
    bot.add_cog(Divers(bot))