import discord
import asyncio
from discord.ext import commands


class Owner(commands.Cog, name='Owner Commands'):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description='Load a cog')
    @commands.is_owner()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def load(self, ctx: discord.ApplicationContext, *, extension):
        self.client.load_extension(f'cogs.{extension}')
        embed = discord.Embed(description=f'\✅ The {extension} cog has been successfully loaded.', color=discord.Color.green())
        await ctx.respond(embed=embed)

    @commands.slash_command(description='Unload a cog')
    @commands.is_owner()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def unload(self, ctx: discord.ApplicationContext, *, extension):
        self.client.unload_extension(f'cogs.{extension}')
        embed = discord.Embed(description=f'\✅ The {extension} cog has been successfully unloaded.', color=discord.Color.green())
        await ctx.respond(embed=embed)

    @commands.slash_command(description='Reload a cog')
    @commands.is_owner()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def reload(self, ctx: discord.ApplicationContext, *, extension):
        self.client.reload_extension(f'cogs.{extension}')
        embed = discord.Embed(description=f'\✅ The {extension} cog has been successfully reloaded.', color=discord.Color.green())
        await ctx.respond(embed=embed)


def setup(client):
    client.add_cog(Owner(client))
