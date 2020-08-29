from discord.ext import commands
import discord
import random

#Ces couleurs sont des constantes trouvées dans la librairie discord.js
colors = {
  'DEFAULT': 0x000000,
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'GREY': 0x95A5A6,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_GREY': 0x979C9F,
  'DARKER_GREY': 0x7F8C8D,
  'LIGHT_GREY': 0xBCC0C0,
  'DARK_NAVY': 0x2C3E50,
  'BLURPLE': 0x7289DA,
  'GREYPLE': 0x99AAB5,
  'DARK_BUT_NOT_BLACK': 0x2C2F33,
  'NOT_QUITE_BLACK': 0x23272A
}

class Embed(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command(
        name = 'embed',
        description = 'Cette commande permet de faire une intégration avec du texte'
    )
    async def embed_command(self,ctx):

        membre = ctx.message.author
        print(f"{membre} used the 'embed' command")

        #Défini une fonction qui valide le message reçu par le bot
        def check(ms):
            #Cherche le message envoyé dans le salon dans lequel a été exécuté la commande
            #ainsi que l'utilisateur qui a exécuté la commande
            return ms.channel == ctx.message.channel and ctx.message.author

        #Demande en premier à l'utilisateur le titre
        await ctx.send(content = "Quel titre veux-tu donner ?")

        #Attendre pour la réponse de l'utilisateur et récupérer le titre
        msg = await self.bot.wait_for('message', check=check)
        title = msg.content

        #Ensuite, demande le contenu
        await ctx.send(content = 'Quelle description veux-tu mettre ?')
        msg = await self.bot.wait_for('message', check=check)
        desc = msg.content

        #Enfin, on fait l'intégration et on l'envoie
        msg = await ctx.send(content = "Génération de l'intégration...")
            
        color_list = [c for c in colors.values()]
        #Convertit les couleurs en une liste pour être capable d'en choisir une aléatoirement

        embed = discord.Embed(
            title=title,
            description=desc,
            color=random.choice(color_list)
        )

        #Paramétrer la miniature pour être la PP du bot
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        #Ajouter aussi le nom de l'auteur et sa PP
        embed.set_author(
            name=ctx.message.author.name,
            icon_url=ctx.message.author.avatar_url
        )

        await msg.edit(
            embed=embed,
            content=None
        )
        #Edite le message
        #Nous devons spécifier le contenu à 'None' puisque l'on ne veux pas que ça reste à 'Génération de l'intégration'
        return

    """
    @commands.command(
        name = 'help',
        description = 'La commande pour avoir la liste des commandes disponibles !',
        aliases = ['commands', 'command', 'cmd'],
        usage = 'cog'
    )
    async def help_command(self, ctx, cog='all'):

        membre = ctx.message.author
        print(f"{membre} used the 'help' command")

        #le troisième paramètre antre en jeu quand seulement un argument est donné par l'utilisateur

        #prépare l'intégration

        color_list = [c for c in colors.values()]
        help_embed = discord.Embed(
            title='Help',
            color=random.choice(color_list)
        )
        help_embed.set_thumbnail(url=self.bot.user.avatar_url)
        help_embed.set_footer(
            text=f"Demandé par {ctx.message.author.name}",
            icon_url=self.bot.user.avatar_url
        )

        #Fait une liste de tous les cogs
        cogs = [c for c in self.bot.cogs.keys()]

        #Si aucun cog n'est spécifié par l'utilisateur, on liste tous les cogs et commandes
        if cog == 'all':
            for cog in cogs:
                #Récupérer une liste de toutes les commandes dans chaque cog

                cog_commands = self.bot.get_cog(cog).get_commands()
                commands_list = ''
                for comm in cog_commands:
                    commands_list += f'**{comm.name}** - *{comm.description}*\n'

                #Ajouter le détail du cog à l'intégration

                textes = "Tu peux avoir plus de détail se les commandes en tapant `$help [nom de la catégorie]`\n Ce bot est complètement inutile, jore, vraiment."

                help_embed.add_field(
                    name=cog,
                    value=commands_list,
                    inline=False
                ).add_field(
                    name='\u200b', value='\u200b', inline=False
                )

                #Ajoute également un espace vide '\u200b' est un charactère d'espace vide
            pass
        else:
            
            #Si le cog est spécifié

            lower_cogs = [c.lower() for c in cogs]

            #Si le cog existe bel est bien
            if cog.lower() in lower_cogs:

                #Récupérer une liste de toutes les commandes dans le cog spécifié
                commands_list = self.bot.get_cog(cogs[ lower_cogs.index(cog.lower()) ]).get_commands()
                help_text = ''

                #Ajouter les détails de chaque commande au texte d'aide
                #Command Name
                #Description
                #[Aliases]
                #
                #Format
                for command in commands_list:
                    help_text += f"```{command.name}```\n" \
                        f"**{command.description}**\n\n"

                    #Ainsi que les aliases, s'il y en a
                    if len(command.aliases) > 0:
                        help_text += f'**Alias :** `{"`,`".join(command.aliases)}`\n\n\n'
                    else:
                        #Ajouter une nouvelle ligne de caractère pour que ça reste joli
                        #ce qui est le but d'une commande help personnalisée
                        help_text += "\n"

                    #Enfin le format
                    if command.usage is None:
                        help_text += f'Format : `${command.name}`\n\n\n\n'
                    else:
                        help_text += f'Format : `${command.name} {command.usage}`\n\n\n\n'
                    
                help_embed.description = help_text
                
            else:
                #Notifie l'utilisateur que le cog est invalide, et termine la commande
                await ctx.send('Commande spécifié invalide.\nUtilise la commande `help` pour lister toutes les commandes.')
                return

        await membre.send(embed=help_embed)
        await ctx.send(f"{membre.name}, la liste des commandes t'a été envoyée, vérifie tes MP !")

        return
    """



def setup(bot):
    bot.add_cog(Embed(bot))
