import discord, asyncio, os

async def read_quotes_cb(message, arg):
    if not os.path.exists('quotes.txt'):
        await message.channel.send("No quotes yet.")
        return

    with open('quotes.txt', "r") as f:
        contents = f.read()

    await message.channel.send(contents or "Empty file.")
