import discord
from discord.ext import commands
import random
from discord.ext.commands import has_permissions, MissingPermissions

class Admin(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command(
        name = "getrole",
        description = "Cette commande permet de se donner un rôle.",
        usage = "[role]",
        aliases = ['gr']
    )
    @commands.has_permissions(manage_roles=True)
    async def getrole_command(self,ctx, role: discord.Role):
        if role in ctx.author.roles:
            await ctx.author.remove_roles(role)
            await ctx.send(f"Le rôle {role} a été supprimé à {ctx.message.author.mention}")
        else:
            await ctx.author.add_roles(role)
            await ctx.send(f"Le rôle {role} a été ajouté à {ctx.message.author.mention}")
        return


    @commands.command(
        name = "role",
        description = "Cette commande permet de donner un rôle à un utilisateur.",
        usage = "[role] @mention"
    )
    @commands.has_permissions(manage_roles=True)
    async def role_command(self,ctx, role:discord.Role):
        user = ctx.message.mentions[0]
        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f"Le rôle {role.name} a été supprimé à {user.name}")
        else:
            await user.add_roles(role)
            await ctx.send(f"Le rôle {role.name} a été ajouté à {user.name}")
        return


    @commands.command(
        name = "validate",
        description = "Cette commande permet de valider un nouvel arrivant (Nécessite les rôles `@Validé` et `@PasValidé` de présents sur le server.)",
        usage = "@mention"
    )
    @commands.has_permissions(manage_roles=True)
    async def validate_command(self,ctx):
        user = ctx.message.mentions[0]
        unvalidate_role = discord.utils.get(ctx.guild.roles, name='PasValidé')
        validate_role = discord.utils.get(ctx.guild.roles, name='Validé')
        await user.remove_roles(unvalidate_role)
        await user.add_roles(validate_role)
        await ctx.send(f"{user.mention} a été validé !")
        return


    @commands.command(
        name = "unvalidate",
        description = """Cette commande permet de "bloquer" quelqu'un, de lui enlever le rôle "Validé" (Nécessite les rôles `@Validé` et `@PasValidé` de présents sur le server.)""",
        usage = "@mention",
        aliases = ['block']
    )
    @commands.has_permissions(manage_roles=True)
    async def unvalidate_command(self,ctx):
        user = ctx.message.mentions[0]
        unvalidate_role = discord.utils.get(ctx.guild.roles, name='PasValidé')
        validate_role = discord.utils.get(ctx.guild.roles, name='Validé')
        await user.remove_roles(validate_role)
        await user.add_roles(unvalidate_role)
        await ctx.send(f"{user.mention} a été bloqué !")
        return


    @commands.command(
        name = "mute",
        description = "Cette commande permet de mute qeulqu'un (Nécessite le rôle `@Muted` de présent sur le server.)",
        usage = "@mention"
    )
    @commands.has_permissions(manage_messages=True)
    async def mute_command(self,ctx,member : discord.Member):
        writer = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.add_roles(role)
        embed = discord.Embed(title="Utilisateur muté !", description=f"**{member}** a été muté par **{writer}**")
        await ctx.send(embed=embed)
        return


    @commands.command(
        name = "unmute",
        description = "Cette commande permet d'enlever le mute d'un utilisateur (Nécessite le rôle `@Muted` de présent sur le server.)",
        usage = "@mention"
    )
    @commands.has_permissions(manage_messages=True)
    async def unmute_command(self,ctx,member : discord.Member):
        writer = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name = 'Muted')
        await member.remove_roles(role)
        embed = discord.Embed(title="Utilisateur dé-muté !",description=f"**{writer}** a dé-muté **{member}** !")
        await ctx.send(embed=embed)
        return



def setup(bot):
    bot.add_cog(Admin(bot))