import discord
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_TOKEN = os.getenv('CLIENT_TOKEN')
CLIENT_PREFIX = os.getenv('CLIENT_PREFIX')
GIPHY_TOKEN = os.getenv("GIPHY_TOKEN")
TENOR_TOKEN = os.getenv('TENOR_TOKEN')