import discord
import os
import random
from dotenv import load_dotenv

# Load the bot token from .env file
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Intents setup
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content

# Initialize the bot
client = discord.Client(intents=intents)

# Random comments for uploaded images
random_comments = [
    "Wow, that's an amazing photo!",
    "Looks interesting! Did you take it yourself?",
    "Haha, this is great!",
    "What a masterpiece!",
    "I have no words... this is incredible.",
    "Not bad at all!",
    "Is this from another world? Love it!",
    "This totally made my day!",
    "10/10 would frame this picture.",
    "I can feel the energy from this image!"
]

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message contains an attachment
    if message.attachments:
        # Choose a random comment
        comment = random.choice(random_comments)
        await message.channel.send(comment)

# Run the bot
client.run(TOKEN)
