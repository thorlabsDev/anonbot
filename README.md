# AnonBot

AnonBot is a Discord bot designed to facilitate anonymous message forwarding and logging in a Discord server. It enables users to send messages and attachments directly to specific channels anonymously.

## Features

- **Anonymous Messaging**: Users can send direct messages (DMs) to the bot, which will then anonymously forward these messages to a designated channel.
- **Message Logging**: Every message received and forwarded by the bot is logged with a timestamp, user ID, and content.
- **Attachment Support**: The bot supports forwarding attachments sent in messages.
- **Member Verification**: Only members of a specific channel are allowed to use the bot's DM feature.

## Requirements

- Docker and Docker Compose.
- A Discord Bot Token.
- 

## Setup

## Setup with Docker

1. **Clone the Repository**:
   Clone this repository to your local machine or server.

2. **Prepare the `.env` File**:
   Create a `.env` file in the root directory of the project as given in `example.env`:

3. **Building the Docker Image**:
Run `docker-compose build` to build the Docker image for your bot.

4. **Running the Bot**:
Execute `docker-compose up` to start the bot.

## Usage

- **Direct Message to Bot**: Users can send a direct message to AnonBot. If they are members of the designated channel, their message will be anonymously forwarded to another specified channel.
- **Attachments**: Attachments sent in direct messages are also forwarded.
- **Logging**: All messages are logged in `message_log.txt` with relevant details.

## Contributions

Contributions to AnonBot are welcome. Please ensure you follow the project's code style and contribute to its overall quality.

## License

This project is licensed under [MIT LICENSE](https://opensource.org/license/mit/). Please see the LICENSE file for more details.

## Contact

For support or queries, contact [DISCORD](https://discord.gg/thorlabs).
