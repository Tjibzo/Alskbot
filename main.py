# on importe le module discord.py
import discord

from discord.utils import get

#ajouter un composant de discord.py
from discord.ext import commands

import random

import jeton

import asyncio

# une commande
# !regles =regles #regles

# créer le bot
bot = commands.Bot(
    command_prefix='$',
    description = 'Un bot qui sert à rien, vraiment',
    owner_id = 373731794635456512,
    case_insensitive = True
    )

cogs = ['cogs.basic', 'cogs.embed', 'cogs.fun', 'cogs.divers', 'cogs.admin','cogs.casino']

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
                              activity=discord.Activity(type=discord.ActivityType.watching, name = "l'humanité périr ($help)"))

"""
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
"""

@bot.event
async def on_member_join(member):
    unvalidate_role = discord.utils.get(member.guild.roles, name='PasValidé')
    await member.add_roles(unvalidate_role)
    channel = bot.get_channel(743478642385879154)
    await channel.send(f"Bienvenue {member.mention} sur le server ! N'hésite pas à faire la commande `regles` !")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(743478642385879154)
    await channel.send(f"{member} nous a quitté pour suivre une autre voie de la Force....")
        
@bot.command()
async def mention(ctx,destinator : discord.Member):
    writer = ctx.message.author.mention
    pseudo = destinator.mention
    print(destinator)
    print(ctx.author)
    print(pseudo)
    robot = bot.user.name + "#" + bot.user.discriminator
    await ctx.send(f"Le pingé est {pseudo}, celui qui as pingé est {writer}")
    await ctx.send(f"{destinator} a été pingé - Signé {robot}")
    if destinator == None:
        await ctx.send("Manque la mention")
    elif destinator == ctx.author:
        await ctx.send("Auto-ping")
    elif pseudo == '<@714478143632703510>':
        await ctx.send("Bot-ping :smirk:")
    else:
        await ctx.send("Ping classique")
    return


@bot.command()
async def mwahahaha(ctx):
    await ctx.message.delete()
    await ctx.send("https://tenor.com/view/evil-laugh-laughing-dark-side-muahaha-gif-8949456")


@bot.command()
async def fs(ctx):
    counter = 5
    await ctx.send("Je vais faire un décompte et envoyer 'Coucou' dans 5 secondes")
    while counter>0:
        await ctx.send(counter)
        counter -= 1
        await asyncio.sleep(1)
    await ctx.send("Coucou")


# donner le token pour qu'il se connecte
token = jeton.code

# phrase
print("Lancement du bot...")

# connecter au serveur
bot.run(token, bot = True, reconnect = True)