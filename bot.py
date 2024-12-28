import discord
import random
import os

from flask import Flask
from threading import Thread

# Flask Web Server
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Start the web server in a separate thread
Thread(target=run).start()

# Get the bot token directly from the environment
TOKEN = os.getenv("BOT_TOKEN")

# Configure intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize client
client = discord.Client(intents=intents)

# Random comments
random_comments = [
    "Wow, that's an amazing photo!",
    "Looks interesting! Did you take it yourself?",
    "Haha, this is great!",
    "What a masterpiece!",
    "10/10 would frame this picture!"
]

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    print("Bot is now running and will not shut down!")

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message contains an image
    if message.attachments and any(
        attachment.filename.endswith(('.png', '.jpg', '.jpeg', '.gif')) for attachment in message.attachments
    ):
        # Respond with a random comment
        random_comment = random.choice(random_comments)
        await message.channel.send(random_comment)
        print("Processed an image.")

# Run the bot
client.run(TOKEN)