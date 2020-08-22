import discord
from discord.ext import commands
import random

class Fun(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command(
        name = 'say',
        description = 'Cette commande fera répéter ce que vous venez de dire par le bot !',
        aliases = ['repeat', 'parrot'],
        usage = '<text>'
    )
    @commands.is_owner()
    async def say_command(self, ctx, bot):
        #'usage' a seulement besoin de montrer les paramètres de la commande

        #Le paramètre self est juste une référence à la classe
        #ctx est le context relié à la commande

        #maintenant, on va prendre le message avec la commande
        msg = ctx.message.content

        #on extrait le  texte envoyé par l'utilisateur
        #ctx.invoked_with donne l'alias utilisé
        #ctx.prefix  donne le prefixe utilisé en invoquant la commande
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]

        #maintenant, on va vérifier si l'utilisateur a en effet écrit tu texte
        if text == '':
            #l'utilisateur n'a pas spécifié le texte
            await ctx.send(content = 'Tu dois spécifier le texte !')
            pass
        else:
            #l'utilisateur a spécifié le texte
            await ctx.send(content = f"{text}")
            pass
        await ctx.message.delete()
        return


    @commands.command(
        name = "coinflip",
        description = "Cette commande permet de lancer une pièce !",
        aliases = ['coin','pileouface']
    )
    async def coinflip_command(self,ctx):
        coin = random.randint(0,3)
        if (coin/2 == 0) or (coin/2 == 1):
            await ctx.send("Pile")
        else:
            await ctx.send("Face")
        return


    @commands.command(
        name = "de",
        description = "Cette commande permet de lancer un dé en spécifiant le nombre maximum (par défaut, 6)",
        aliases = ['dice'],
        usage = '[nombre maximum]'
    )            
    async def de_command(self,ctx,maximum=6):
        dice = random.randint(1,maximum)
        await ctx.send(dice)
        return


    @commands.command(
        name = "hug",
        description = "Cette commande permet d'envoyer une câlin à quelqu'un !",
        usage = '@mention'
    )
    async def hug_command(self,ctx,destinator : discord.Member):
        pseudo = destinator.mention
        writer = ctx.message.author.mention
        if pseudo == writer :
            await ctx.send(f"C'est triste de te voir seul {pseudo} :pensive:. Tiens, un câlin  pour te réconforter !")
            await ctx.send("https://tenor.com/view/robot-virtual-hug-loading-hug-sent-love-gif-17335633")
        else:
            await ctx.send(f"Un câlin gratuit pour {pseudo} de la part de {writer} !")
            await ctx.send("https://tenor.com/view/hug-hugs-ghost-hug-its-there-gif-4951192")
        return
    

    @commands.command(
        name = "slap",
        description = "Cette commande permet de giffler quelqu'un...parce que pourquoi pas....",
        usage = '@mention'
    )
    async def slap_command(self,ctx,destinator : discord.Member):
        pseudo = destinator.mention
        writer = ctx.message.author.mention
        if pseudo == writer :
            await ctx.send(f"Mais pourquoi t'infliger ça {pseudo} ??? :fearful: Bon, si tu insistes....")
            await ctx.send("https://tenor.com/view/crazy-slap-phone-slap-gif-15051103")
        else:
            await ctx.send(f"Mais, {writer}... pourquoi tant de haine envers {pseudo} ? M'enfin, il l'a surement mérité....")
            await ctx.send("https://tenor.com/view/slap-bears-gif-10422113")
        return


    @commands.command(
        name = "poke",
        description = "Cette commande permet de poke quelqu'un, mais n'y va pas trop fort, tu risque de le réveiller....",
        usage = '@mention'
    )
    async def poke_command(self,ctx,destinator : discord.Member):
        pseudo = destinator.mention
        writer = ctx.message.author.mention
        if pseudo == writer :
            await ctx.send(f"S'auto poker ? Tu va bien {pseudo} ? Ca n'a tellement aucun sens, qu'il n'existe même pas un GIF pour ça....")
            await ctx.send("https://tenor.com/view/lil-peep-poke-annoy-gif-10271400")
        else:
            await ctx.send(f"Aller !!! Réveille toi {pseudo}, {writer} a besoin de toi !!!")
            await ctx.send("https://tenor.com/view/milk-and-mocha-bear-couple-poke-mad-pissed-gif-12498610")
        return


    @commands.command(
        name = "feed",
        description = "Cette commande permet de me nourir, moi, pauvre bot....",
        usage = '<text>',
        aliases = ['eat']
    )
    async def feed_command(self,ctx):
        writer = ctx.message.author.mention
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]

        if text == '':
            await ctx.send(content = 'Tu dois spécifier le texte !')
            pass
        else:
            await ctx.send(content = f"Hmmm, ce/cette **{text}** était très bon(ne) ! Merci {writer} !!! ^^")
            await ctx.send(content = "https://tenor.com/view/bear-hungry-food-cute-gif-12983510")
            pass
        return

def setup(bot):
    bot.add_cog(Fun(bot))