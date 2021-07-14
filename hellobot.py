import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run('ODY0OTg0Mjc4ODUyODI5MjU1.YO9ZYg.ZD9k8k4fYe0Cr8aFQ3akD3F7V-Y')