import discord
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
REQUEST_LINK = os.environ.get("REQUEST_LINK")
GUILD = os.environ.get("GUILD")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

client.run(DISCORD_TOKEN)

print(DISCORD_TOKEN)
print(REQUEST_LINK)
print(GUILD)