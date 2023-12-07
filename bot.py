import discord
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

# Set up Discord intents for the bot
intents = discord.Intents.default()
intents.messages = True  # Enable message events
intents.guilds = True  # Enable guild events
intents.members = True  # Enable member events

# Initialize the Discord client with the specified intents
client = discord.Client(intents=intents)

# Retrieve bot token and channel IDs from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
MEMBER_CHANNEL_ID = int(os.getenv("MEMBER_CHANNEL_ID"))
SUCCESS_CHANNEL_ID = int(os.getenv("SUCCESS_CHANNEL_ID"))


def log_message(user_id, message_content, attachment_url=None):
    """
    Logs a message to a text file with a timestamp, user ID, message content, and optional attachment URL.
    """
    with open("message_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - User {user_id}: {message_content}"
        if attachment_url:
            log_entry += f" [Attachment: {attachment_url}]"
        log_entry += "\n"
        log_file.write(log_entry)


@client.event
async def on_ready():
    """
    Event triggered when the bot is ready.
    """
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    """
    Event triggered when a message is sent in any channel the bot has access to.
    """
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Check if the message is a DM (Direct Message)
    if isinstance(message.channel, discord.DMChannel):
        # Retrieve the guild and specific channels using their IDs
        guild = client.get_guild(GUILD_ID)
        specific_channel = guild.get_channel(MEMBER_CHANNEL_ID)
        another_channel = guild.get_channel(SUCCESS_CHANNEL_ID)

        # Check if the author of the message is a member of the specific channel
        if message.author in specific_channel.members:
            # Create an embed to forward the message content
            embed = discord.Embed(title="Anon Success Posted:", description=message.content, color=0x00ff00)
            attachment_url = None
            if message.attachments:
                # If there's an attachment, add it to the embed
                attachment_url = message.attachments[0].url  # Assuming first attachment is the image
                embed.set_image(url=attachment_url)
            # Send the embed in another channel
            await another_channel.send(embed=embed)
            # Notify the user that their message has been forwarded
            await message.author.send("Your message has been successfully forwarded!")

            # Log the message and any attachment URL
            log_message(message.author.id, message.content, attachment_url)
        else:
            # Inform the user if they are not in the required channel
            await message.author.send("You are not in the required channel to perform this action.")


# Run the client with the bot token
client.run(BOT_TOKEN)
