import discord
from discord.ext import commands
import random
import math


class Casino(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command(
        name = "casino",
        description = "Cette commande permet de jouer au casino"
    )
    async def casino_command(self,ctx):
        membre = ctx.message.author
        envoi = ctx.message.content
        print(f"{membre} used the 'casino' command")

        writer = ctx.message.author.mention
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]

        argent = 1000
        partie = True

        await ctx.send("Tu entres au casino et tu te place devant la table de la roulette.")

        def check(ms):
            return ms.channel == ctx.message.channel and ctx.message.author

        while partie:

            NombreMise = 50

            while NombreMise > 49 or NombreMise < 0:
                await ctx.send(content = "Entre le nombre sur lequel tu souhaite miser entre 0 et 49 : ")
                msg = await self.bot.wait_for('message', check=check)
                NombreMise = msg.content
                try:
                    NombreMise = int(NombreMise)
                except ValueError:
                    await ctx.send("Saisis un nombre entier entre 0 et 49")
                    continue
                except TypeError:
                    await ctx.send("Saisis un nombre entier entre 0 et 49")
                    continue
                if NombreMise > 49 or NombreMise < 0:
                    await ctx.send("Saisis un nombre entier entre 0 et 49")

            mise = 0
            while mise <= 0 or mise > argent:
                await ctx.send(f"Tu possède {argent}$")
                await ctx.send(content = "Rentre la somme que tu souhaite miser : ")
                msg = await self.bot.wait_for('message', check=check)
                mise = msg.content
                try:
                    mise = int(mise)
                except ValueError:
                    await ctx.send(f"Ecris un nombre entier positif inférieur à {argent}")
                    continue
                except TypeError:
                    await ctx.send(f"Ecris un nombre entier positif inférieur à {argent}")
                    continue
                if mise > argent :
                    await ctx.send(f"Mise une somme inférieure à {argent}$")

                win = random.randrange(50)
                if NombreMise == win:
                    mise *= 3
                    argent += mise
                    await ctx.send(f"Tu triples ta mise soit {mise} $ !")
                elif NombreMise % 2 == win % 2:
                    mise = math.ceil(mise/2)
                    argent -= mise
                    await ctx.send(f"Tu remportes la moitié de ta mise soit {mise}$ !\nLa bille était tombée sur {win}")
                else:
                    argent -= mise
                    await ctx.send(f"Tu perds la totalité de ta mise ! La bille était tombée sur {win}.")

                if argent > 0 :
                    await ctx.send(f"Il te reste {argent}$.")
                    await ctx.send(content = "Veux-tu continuer la partie ? Oui/oui ; Non/non")
                    msg = await self.bot.wait_for('message', check=check)
                    quitter = msg.content                    
                    if (quitter == "non") or (quitter == "Non"):
                        await ctx.send(f"Tu quitte le casino avec {argent}$.")
                        if argent > 1000:
                            argent = argent-1000
                            await ctx.send(f"Tu as fait un bénéfice de {argent}$ lors de cette session !")
                        elif argent == 1000:
                            await ctx.send("Tu pars du casino avec tes 1000$.")
                        else:
                            argent = 1000-argent
                            await ctx.send(f"Tu as perdu {argent}$ lors de cette session....")
                        partie = False
                else:
                    await ctx.send("Tu n'a plus d'argent, tu quittes le casino, ruiné.")
                    partie = False
                    break
                break


def setup(bot):
    bot.add_cog(Casino(bot))