# Standard library
import asyncio
import os
import signal
# Third party
import discord
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

# Local
from template import NewCommand, add_command, check_all
from modules.add_quote import add_quote_cb
from modules.read_quote import read_quotes_cb
from modules.someones_mom import someones_mom_cb
from modules.help import help_cb
from modules.purge import purge_cb
from modules.say import say_cb

# Initialize Discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def register_commands():
    """Register all bot commands"""
    add_command(NewCommand(add_quote_cb, ".addquote"))
    add_command(NewCommand(read_quotes_cb, ".readquotes"))
    add_command(NewCommand(someones_mom_cb, ".mom-of"))
    add_command(NewCommand(help_cb, ".help"))
    add_command(NewCommand(purge_cb, ".purge"))
    add_command(NewCommand(say_cb, ".say"))

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await check_all(message)

async def main():
    """Main async function to run the bot"""
    async with client:
        await client.start(os.getenv('API_KEY'))

# Register commands and run bot
register_commands()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nShutting down...")
