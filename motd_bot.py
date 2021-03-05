import discord
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
REQUEST_LINK = os.environ.get("REQUEST_LINK")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
client.run(DISCORD_TOKEN)

print(DISCORD_TOKEN)
print(REQUEST_LINK)