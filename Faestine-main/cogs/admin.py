import discord
import asyncio
from discord.ext import commands


class Admin(commands.Cog, name='Administrator Commands'):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description='Delete messages from the channel')
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def purge(self, ctx: discord.ApplicationContext, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            description=f'\✅ Successfully deleted {len(deleted)} messages.',
            color=discord.Color.blue()
        )
        await ctx.respond(embed=embed)

    @commands.slash_command(description='Ban a member from the guild')
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ban(self, ctx: discord.ApplicationContext, member, reason=None):
        if member is None or member == ctx.author:
            await ctx.respond("\⛔ You cannot ban yourself")
            return
        if reason is None:
            reason = "No reason provided"
        await member.ban(reason=reason)
        embed = discord.Embed(description='A member has been banned', color=discord.Color.dark_red())
        embed.add_field(name='Member', value=member, inline=False)
        embed.add_field(name='Reason', value=reason, inline=False)
        await ctx.respond(embed=embed)


def setup(client):
    client.add_cog(Admin(client))
