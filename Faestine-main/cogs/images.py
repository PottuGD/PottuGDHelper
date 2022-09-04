import discord
import aiohttp
import TenGiphPy
from discord.ext import commands
import config

TOKENS = {'TENOR_TOKEN': config.TENOR_TOKEN}
TENOR = TenGiphPy.Tenor(token=TOKENS['TENOR_TOKEN'])


class Images(commands.Cog, name='Image Commands'):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.client.loop.create_task(self.session.close())

    # Reserved for future code


def setup(client):
    client.add_cog(Images(client))
