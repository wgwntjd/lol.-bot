import discord

token = NzM3OTc3NTE0MzI0MDAwODU4.XyFNHg.eB1xqwxvrUx0dcWOvx_g7n7qgPs

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswitch('$hello'):
        await message.channel.send('Hello')

client.run(token)