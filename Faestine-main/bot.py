import discord
import os
import chalk
from discord.ext import commands
from dotenv import load_dotenv

from config import CLIENT_PREFIX

activity = discord.Game('IM DA BEST!')
intents = discord.Intents.default()

client = commands.Bot(command_prefix=f'{CLIENT_PREFIX}',
                      activity=activity,
                      intents=intents)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(chalk.cyan(f'>>| Loaded cogs.{filename[:-3]}'))
    else:
        print(chalk.red(f'Could not load cogs.{filename[:-3]}'))
else:
    print(chalk.blue('\nAll cogs loaded\n'))


@client.event
async def on_ready():
    print(chalk.cyan('\nThe bot is ready'))
    print(chalk.cyan('logged in as {0.user}'.format(client)))


load_dotenv()
CLIENT_TOKEN = CLIENT_TOKEN = os.getenv('CLIENT_TOKEN')
client.run(CLIENT_TOKEN)
