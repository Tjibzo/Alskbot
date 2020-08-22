from discord.ext import commands
from datetime import datetime as d

class Basic(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    
    #Définir une nouvelle commande
    @commands.command(
        name = 'ping',
        description = 'Cette commande permet de tester le temps de réponse du bot',
        aliases = ['p']
    )
    async def ping_command(self,ctx):
        start = d.timestamp(d.now()) 
        #Prend l'horodatage de quand la commande a été utilisée

        msg = await ctx.send(content = 'Pinging...')
        #Envoie un message à l'utilisateur dans le salon dans lequel la commande a été exécutée
        #Notifies l'utilisateur le pinging a commencé

        await msg.edit(content=f"Pong!\nL'aller-retour du message a pris {(d.timestamp( d.now() ) - start ) * 1000}ms.")
        #Le ping a été effectué et la durée de l'aller-retour est affiché en ms
        return


    @commands.command(
        name = "test",
        description = "Cette commande permet de vérifier que je fonctionne bien !"
    )
    async def test_command(self,ctx):
        await ctx.send("Je fonctionne ! ^^")
        return


def setup(bot):
    bot.add_cog(Basic(bot))
    #Ajoute les commande Basic au bot
    #Note : la fonction "setip" doit être dans tous les fichiers cog