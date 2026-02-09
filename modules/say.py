import discord

async def say_cb(message, arg):
    parts = arg.split(None, 1)
    
    if len(parts) < 2:
        await message.channel.send("Usage: `.say <channel_id> <message>`")
        return
    
    try:
        channel_id = int(parts[0])
        text = parts[1]
    except ValueError:
        await message.channel.send("Invalid channel ID. Must be a number.")
        return
    
    channel = message.guild.get_channel(channel_id)
    
    if channel is None:
        await message.channel.send(f"Channel with ID {channel_id} not found.")
        return
    
    try:
        await channel.send(text)
        await message.channel.send(f"Message sent to <#{channel_id}>")
    except discord.Forbidden:
        await message.channel.send(f"I don't have permission to send messages in <#{channel_id}>")
    except Exception as e:
        await message.channel.send(f"Error: {e}")
