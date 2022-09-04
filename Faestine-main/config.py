import discord
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_TOKEN = os.getenv('TOKEN')
CLIENT_PREFIX = '&'
GIPHY_TOKEN = os.getenv("GIPHY_TOKEN")
TENOR_TOKEN = os.getenv('TENOR_TOKEN')
