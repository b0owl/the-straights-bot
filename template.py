class NewCommand:
    def __init__(self, callback, call):
        self.callback = callback
        self.call = call

    async def check_call(self, message):
        if message.content.startswith(self.call):
            arg = message.content[len(self.call):].strip()
            await self.callback(message, arg)


calls_dict = {}

def add_command(cmd):
    calls_dict[cmd.call] = cmd

async def check_all(message):
    for cmd in calls_dict.values():
        await cmd.check_call(message)
