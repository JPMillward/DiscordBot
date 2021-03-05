import discord
import asyncio
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
REQUEST_LINK = os.environ.get("REQUEST_LINK")

print(DISCORD_TOKEN)
print(REQUEST_LINK)