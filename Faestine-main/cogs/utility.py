import discord
import asyncio
from discord.ext import commands
import config


class Utility(commands.Cog, name='Utility Commands'):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description='Display the bot\'s current ping')
    @commands.has_guild_permissions(send_messages=True)
    async def ping(self, ctx: discord.ApplicationContext):
        client = self.client
        if round(client.latency * 1000) <= 50:
            embed = discord.Embed(
                description='Here is my current ping!',
                color=discord.Color.green()
            )
            embed.add_field(name='Latency', value=f'```css\n{round(client.latency *1000)}\n```')
            embed.set_thumbnail(url='https://raw.githubusercontent.com/NimbiDev/Faestine/main/assets/logo.png')
        elif round(client.latency * 1000) <= 100:
            embed = discord.Embed(
                description='Here is my current ping!',
                color=discord.Color.gold()
            )
            embed.add_field(name='Latency', value=f'```css\n{round(client.latency * 1000)}\n```')
            embed.set_thumbnail(url='https://raw.githubusercontent.com/NimbiDev/Faestine/main/assets/logo.png')
        elif round(client.latency * 1000) <= 200:
            embed = discord.Embed(
                description='Here is my current ping!',
                color=discord.Color.red()
            )
            embed.add_field(name='Latency', value=f'```css\n{round(client.latency * 1000)}\n```')
            embed.set_thumbnail(url='https://raw.githubusercontent.com/NimbiDev/Faestine/main/assets/logo.png')
        else:
            embed = discord.Embed(
                description='Here is my current ping!',
                color=discord.Color.blue()
            )
            embed.add_field(name='Latency', value=f'```css\n{round(client.latency * 1000)}\n```')
            embed.set_thumbnail(url='https://raw.githubusercontent.com/NimbiDev/Faestine/main/assets/logo.png')
        await ctx.respond(embed=embed)

    @commands.slash_command(description='Display a guild member\'s avatar')
    @commands.has_guild_permissions(send_messages=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def avatar(self, ctx: discord.ApplicationContext, *, member: discord.Member = None):
        if not member:
            member = ctx.author
        embed = discord.Embed(title=str(member), color=discord.Color.blue())
        embed.set_image(url=member.avatar.url)
        await ctx.respond(embed=embed)


def setup(client):
    client.add_cog(Utility(client))
