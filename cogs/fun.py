import discord
from discord.ext import commands
import random
import math

avis = [
    "Euh... oui, pourquoi pas....",#Oui
    "Je ne vois pas de mal à ça :woman_shrugging:",#Oui
    "Oh ! Surtout pas, t'a vraiment crû que j'allais te laisser faire ça ??? :cold_sweat:",#Non
    "*S'enfuit loin*",#Non
    "Bah j'en sais rien moi.... Pourquoi tu me le demande ?",#Neutre
    "Fait ce qu'il te plaira le plus ^^",#Neutre
    "Je suis d'accord avec le fait de ne pas être d'accord d'être d'accord avec toi",#Non
    "Je ne suis pas dans la capacité de délivrer mon désacord sur cette proposition"#Oui
]



class Fun(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command(
        name = 'say',
        description = 'Cette commande fera répéter ce que vous venez de dire par le bot !',
        aliases = ['repeat', 'parrot'],
        usage = '<text>'
    )
    async def say_command(self, ctx, bot):
        membre = ctx.message.author
        envoi = ctx.message.content
        print(f"{membre} used the 'say' command => {envoi}")
        if ctx.message.author.id == 373731794635456512:
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
                await ctx.message.delete()
                await ctx.send(content = 'Tu dois spécifier le texte !')
                pass
            else:
                #l'utilisateur a spécifié le texte
                await ctx.message.delete()
                await ctx.send(content = f"{text}")
                pass
            return

        else :
            await ctx.send(f"Au secour Tjibzo ! {membre.name} essaye de corrompre ma parole ! :cold_sweat: :cold_sweat: :cold_sweat:")
        


    @commands.command(
        name = "coinflip",
        description = "Cette commande permet de lancer une pièce !",
        aliases = ['coin','pileouface']
    )
    async def coinflip_command(self,ctx):
        membre = ctx.message.author
        print(f"{membre} used the 'coinflip' command")
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
        membre = ctx.message.author
        print(f"{membre} used the 'de' command")
        dice = random.randint(1,maximum)
        await ctx.send(dice)
        return


    @commands.command(
        name = "hug",
        description = "Cette commande permet d'envoyer une câlin à quelqu'un !",
        usage = '@mention'
    )
    async def hug_command(self,ctx,destinator : discord.Member):
        membre = ctx.message.author
        print(f"{membre} used the 'hug' command")
        pseudo = destinator.mention
        writer = ctx.message.author.mention
        if pseudo == writer :
            await ctx.send(f"C'est triste de te voir seul {pseudo} :pensive:. Tiens, un câlin  pour te réconforter !")
            await ctx.send("https://media.giphy.com/media/39iwnazvFkW3YpggDf/giphy.gif")
        elif pseudo == '<@714478143632703510>':
            await ctx.send(f"Oh, c'est gentil de penser à moi {writer} :blush:")
            await ctx.send(f"*Fait un câlin à {writer} en retour*")
            await ctx.send("https://media.giphy.com/media/3ornk0ndWxpVYILAVq/giphy.gif")
        else:
            await ctx.send(f"Un câlin gratuit pour {pseudo} de la part de {writer} !")
            await ctx.send("https://media.giphy.com/media/3ornk0ndWxpVYILAVq/giphy.gif")
        return
    

    @commands.command(
        name = "slap",
        description = "Cette commande permet de giffler quelqu'un...parce que pourquoi pas....",
        usage = '@mention'
    )
    async def slap_command(self,ctx,destinator : discord.Member):
        membre = ctx.message.author
        print(f"{membre} used the 'slap' command")
        pseudo = destinator.mention
        writer = ctx.message.author.mention
        if pseudo == writer :
            await ctx.send(f"Mais pourquoi t'infliger ça {pseudo} ??? :fearful: Bon, si tu insistes....")
            await ctx.send("https://tenor.com/WqEQ.gif")
        elif pseudo == '<@714478143632703510>':
            await ctx.send(f"Non mais ça va pas {writer} !")
            await ctx.send(f"*Giffle {writer}*")
            await ctx.send("https://media.giphy.com/media/lDxwNkTqImoFy/giphy.gif")
        else:
            await ctx.send(f"Mais, {writer}... pourquoi tant de haine envers {pseudo} ? M'enfin, il l'a surement mérité....")
            await ctx.send("https://media.giphy.com/media/lDxwNkTqImoFy/giphy.gif")
        return


    @commands.command(
        name = "poke",
        description = "Cette commande permet de poke quelqu'un, mais n'y va pas trop fort, tu risque de le réveiller....",
        usage = '@mention'
    )
    async def poke_command(self,ctx,destinator : discord.Member):
        membre = ctx.message.author
        print(f"{membre} used the 'poke' command")
        pseudo = destinator.mention
        writer = ctx.message.author.mention
        if pseudo == writer :
            await ctx.send(f"S'auto poker ? Tu va bien {pseudo} ? Ca n'a tellement aucun sens, qu'il n'existe même pas un GIF pour ça....")
            await ctx.send("https://media.giphy.com/media/3owzWe1Y3z1MgOWhJ6/giphy.gif")
        elif pseudo == '<@714478143632703510>':
            await ctx.send(f"Je suis là, je suis là, ne t'inquiète pas {writer} :wink:")
        else:
            await ctx.send(f"Aller !!! Réveille toi {pseudo}, {writer} a besoin de toi !!!")
            await ctx.send("https://media.giphy.com/media/3owzW0P44Shp1cenQs/giphy.gif")
        return


    @commands.command(
        name = "feed",
        description = "Cette commande permet de me nourir, moi, pauvre bot....",
        usage = '<text>',
        aliases = ['eat']
    )
    async def feed_command(self,ctx):
        membre = ctx.message.author
        envoi = ctx.message.content
        print(f"{membre} used the 'feed' command => {envoi}")

        writer = ctx.message.author.mention
        msg = ctx.message.content

        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]

        manger = [
            f"Hmmm, ce/cette**{text}** était très bon(ne) ! Merci {writer} !!! ^^",
            f"Putain ce/cette**{text}** est dégueulasse ! C'est quoi cette merde {writer} ???"
        ]

        if text == '':
            await ctx.send(content = 'Tu dois spécifier le texte !')
            pass
        elif (text == ' Tjibzo') or (text == 'tjibzo') or (text == ' [0x]Tjibzo') or (text == ' Tjibzette') or (text == ' <@!373731794635456512>'):
            await ctx.send(content = "Va périr tes grands morts toi")
            await ctx.send(content = "https://tenor.com/view/lightning-palpatine-sheev-palpatine-power-star-wars-gif-16503984")
        elif (text == ' caca') or (text == ' merde') or (text == ' pisse') or (text == ' Caca') or (text == ' Merde') or (text == ' Pisse'):
            await ctx.send(f"Putain mais t'es dégeulasse {writer} ! Me donner ça à manger ???")
            await ctx.send(content = "https://media.giphy.com/media/KWV7mrud6Dq4o/giphy.gif")
        elif (text == ' AlskBot') or (text == ' <@!714478143632703510>'):
            await ctx.send(f'Comme ça tu essaye de me faire manger moi-même. Bien. *Arrache et jette dans un compacteur un bras de {writer}*')
            await ctx.send('https://tenor.com/view/sidious-smile-evil-grin-gif-9517476')
        else:
            mess = random.choice(manger)
            if mess == f"Hmmm, ce/cette**{text}** était très bon(ne) ! Merci {writer} !!! ^^" :
                await ctx.send(mess)
                await ctx.send(content = "https://tenor.com/view/mandalorian-star-wars-baby-yoda-eat-eating-gif-15599282")
            else:
                await ctx.send(mess)
                await ctx.send(content = "https://media.giphy.com/media/KWV7mrud6Dq4o/giphy.gif")
            pass
        return


    @commands.command(
        name = 'avis',
        description = "Cette commande permet de connaître l'avis du bot !",
        aliases = ['advice'],
        usage = '<text>'
    )
    async def avis_command(self,ctx):
        membre = ctx.message.author
        envoi = ctx.message.content
        print(f"{membre} used the 'avis' command => {envoi}")
        mess = random.choice(avis)
        await ctx.send(mess)
        return


    @commands.command(
        name = "russianroll",
        description = "Cette commande permet de jouer à la roulette russe !",
        aliases = ['rr','russian']
    )
    async def russianroll_command(self,ctx):
        membre = ctx.message.author
        envoi = ctx.message.content
        print(f"{membre} used the 'russianroll' command")

        number = random.randint(1,12)
        if (number/2 == 1) or (number/2 == 2) or (number/2 == 3) or (number/2 == 4):
            await ctx.send(f"{membre.name} a perri en tentant de jouer avec la vie...")
            await ctx.send("https://tenor.com/binWd.gif")
            return
        else:
            await ctx.send(f"{membre.name} a survécu, la Force est avec lui !")
            await ctx.send("https://tenor.com/beT1P.gif")
            return


        
        

def setup(bot):
    bot.add_cog(Fun(bot))