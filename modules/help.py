import discord, asyncio

async def help_cb(message, arg):
    embed = discord.Embed(
        title="Bot Commands Menu",
        description="List of commands:",
        color=discord.Color.purple()
    )

    embed.add_field(name=".mom-of [name]", value="Shows `[name] mom`", inline=False)
    embed.add_field(name=".addquote [quote]", value="Adds a quote to the list", inline=False)
    embed.add_field(name=".readquotes", value="Reads all quotes", inline=False)
    embed.add_field(name=".purge [number]", value="Deletes last [number] messages (requires manage messages permission)", inline=False)
    embed.add_field(name=".help", value="Shows this menu", inline=False)

    await message.channel.send(embed=embed)
