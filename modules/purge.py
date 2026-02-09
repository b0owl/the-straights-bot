import discord, asyncio

async def purge_cb(message, arg):
    if not message.author.guild_permissions.manage_messages:
        await message.channel.send("You don't have permission to purge messages.")
        return

    try:
        count = int(arg)
    except (ValueError, TypeError):
        await message.channel.send("Please provide a valid number of messages to purge.")
        return

    deleted = await message.channel.purge(limit=count)
    await message.channel.send(f"Purged {len(deleted)} messages.", delete_after=5)
