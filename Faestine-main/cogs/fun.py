import discord
import os
import asyncio
import random
from discord.ext import commands
import config


class Fun(commands.Cog, name='Fun Commands'):
    def __init__(self, client):
        self.client = client

    # Reserved for future code


def setup(client):
    client.add_cog(Fun(client))
