import discord

client = discord.Client()


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('Sup, 86 :thinking:')

client.run('ENTER TOKEN HERE')
