import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        print(message.type)
        if message.author == client.user:
            return
        if message.content == 'Test':
            await message.channel.send('Test')
        if message.content.startswith('Hallo'): #DETECT FIRST WORD
            await message.channel.send('Hallo Bos')
        if message.content.startswith('giveme'):
            await message.channel.send('Hello', file=discord.File('/home/veril/Downloads/aku.jpg', 'diriku.jpg')) #SEND FILE
        if message.content == 'Info':
            await message.channel.send('''
https://telegra.ph/Proktor-Puspo-11-21
''')
        
with open('token') as f:
    token=f.read()
token=token.split('\n')          
client = MyClient()
client.run(token[2]) #[0] dan [1] untuk skolidbot dan testbot