import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        # Replace 'YOUR_GUILD_ID' with your server's ID
        guild = client.get_guild(YOUR_GUILD_ID)
        # Replace 'SPECIFIC_CHANNEL_ID' with the ID of the channel you want to check
        specific_channel = guild.get_channel(SPECIFIC_CHANNEL_ID)
        # Replace 'ANOTHER_CHANNEL_ID' with the ID of the channel where you want to send the message
        another_channel = guild.get_channel(ANOTHER_CHANNEL_ID)

        # Check if the user is in the specific channel
        if message.author in specific_channel.members:
            await another_channel.send(f'{message.author.name} sent: {message.content}')
            # If the message has attachments (images), send them as well
            for attachment in message.attachments:
                await another_channel.send(attachment.url)

client.run('YOUR_BOT_TOKEN')
