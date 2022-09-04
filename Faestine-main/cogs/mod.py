import discord
import asyncio
from discord.ext import commands


class Mod(commands.Cog, name='Moderator Commands'):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description='Kick a member from the guild')
    @commands.has_permissions(kick_members=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def kick(self, ctx: discord.ApplicationContext, member, reason=None):
        if member is None or member == ctx.author:
            await ctx.respond("\⛔ You cannot ban yourself")
            return
        if reason is None:
            reason = "No reason provided"
        await member.kick(reason=reason)
        embed = discord.Embed(description='A member has been kicked', color=discord.Color.dark_red())
        embed.add_field(name='Member', value=member, inline=False)
        embed.add_field(name='Reason', value=reason, inline=False)
        await ctx.respond(embed=embed)


def setup(client):
    client.add_cog(Mod(client))
