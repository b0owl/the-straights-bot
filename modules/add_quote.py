import discord, asyncio

async def add_quote_cb(message, arg):
    if not arg:
        await message.channel.send("You forgot the quote.")
        return

    with open('quotes.txt', "a") as f:
        f.write(arg + "\n")
        f.write("-" * 30)
        f.write("\n")

    await message.channel.send(f"Added quote:\n> {arg}")
