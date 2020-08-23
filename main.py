# on importe le module discord.py
import discord

from discord.utils import get

#ajouter un composant de discord.py
from discord.ext import commands

import random

import jeton

# une commande
# !regles =regles #regles

# créer le bot
bot = commands.Bot(
    command_prefix='$',
    description = 'Un bot qui sert à rien, vraiment',
    owner_id = 373731794635456512,
    case_insensitive = True
    )

cogs = ['cogs.basic', 'cogs.embed', 'cogs.fun', 'cogs.divers', 'cogs.admin']

# détecter quand le bot est prêt ("allumé")
@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user.name} - {bot.user.id}")
    bot.remove_command('help')
    #Enlève la commande help
    for cog in cogs:
        bot.load_extension(cog)
        print(cog)
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game("Aussi inutile que mon créateur ($help)"))


# détecter quand quelqu'un ajoute un emoji sur un message
@bot.event
async def on_raw_reaction_add(payload):

    emoji = payload.emoji.name # récupère l'emoji
    canal = payload.channel_id # récupère le numéro du canal
    message = payload.message_id # récupère le numéro du message

    python_role = get(bot.get_guild(payload.guild_id).roles, name="python")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    print(membre)

    # vérifier si l'émoji ajouté est "python"
    if canal == 711559616160595980 and message == 711559953130848326 and emoji == "python":
        print("Grade ajouté !")
        await membre.add_roles(python_role)
        await membre.send("Tu obtiens le grade Python !")


# détecter quand quelqu'un supprime un emoji sur un message
@bot.event
async def on_raw_reaction_remove(payload):

    emoji = payload.emoji.name # récupère l'emoji
    canal = payload.channel_id # récupère le numéro du canal
    message = payload.message_id # récupère le numéro du message

    python_role = get(bot.get_guild(payload.guild_id).roles, name="python")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    # vérifier si l'émoji ajouté est "python"
    if canal == 711559616160595980 and message == 711559953130848326 and emoji == "python":
        print("Grade supprimé !")
        await membre.remove_roles(python_role)
        await membre.send("Tu perds le grade Python !")

        
@bot.command()
async def mention(ctx,destinator : discord.Member):
    writer = ctx.message.author.mention
    pseudo = destinator.mention
    robot = bot.user.name + "#" + bot.user.discriminator
    await ctx.send(f"Le pingé est {pseudo}, celui qui as pingé est {writer}")
    await ctx.send(f"{destinator} a été pingé - Signé {robot}")
    if destinator == None:
        await ctx.send("A qui essayes-tu de faire un câlin ? Réessaye en le mentionnant !")
    elif destinator.user.idLong == ctx.author.idLong:
        await ctx.send("Auto-ping")
    elif destinator.user.idLong == ctx.jda.selfUser.idLong:
        await ctx.send("Bot-ping :smirk:")
    else:
        await ctx.send("Ping classique")
    return


# donner le token pour qu'il se connecte
token = jeton.code

# phrase
print("Lancement du bot...")

# connecter au serveur
bot.run(token, bot = True, reconnect = True)