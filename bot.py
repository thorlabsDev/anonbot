import discord
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

BOT_TOKEN = os.getenv("BOT_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
MEMBER_CHANNEL_ID = int(os.getenv("MEMBER_CHANNEL_ID"))
SUCCESS_CHANNEL_ID = int(os.getenv("SUCCESS_CHANNEL_ID"))

def log_message(user_id, message_content, attachment_url=None):
    with open("message_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - User {user_id}: {message_content}"
        if attachment_url:
            log_entry += f" [Attachment: {attachment_url}]"
        log_entry += "\n"
        log_file.write(log_entry)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        guild = client.get_guild(GUILD_ID)
        specific_channel = guild.get_channel(MEMBER_CHANNEL_ID)
        another_channel = guild.get_channel(SUCCESS_CHANNEL_ID)

        if message.author in specific_channel.members:
            embed = discord.Embed(title="Anon Success Posted:", description=message.content, color=0x00ff00)
            attachment_url = None
            if message.attachments:
                attachment_url = message.attachments[0].url  # Assuming first attachment is the image
                embed.set_image(url=attachment_url)
            await another_channel.send(embed=embed)
            await message.author.send("Your message has been successfully forwarded!")

            # Log the message and attachment URL
            log_message(message.author.id, message.content, attachment_url)

        else:
            await message.author.send("You are not in the required channel to perform this action.")

client.run(BOT_TOKEN)
