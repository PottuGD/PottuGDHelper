import discord
import os
import chalk
from discord.ext import commands

from config import CLIENT_TOKEN, CLIENT_PREFIX

activity = discord.Game('with slash commands!')

client = commands.Bot(command_prefix=f'{CLIENT_PREFIX}', activity=activity)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(chalk.cyan(f'>>| Loaded cogs.{filename[:-3]}'))
    else:
        print(chalk.yellow(f'>>| Unable to load cogs.{filename[:-3]}'))

client.run(f'{CLIENT_TOKEN}')
