import discord
import asyncio
import random
import os

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

# Shutdown timer
shutdown_timer = None


# Function to handle shutdown after 15 minutes of idle time
async def idle_shutdown():
    global shutdown_timer
    if shutdown_timer:
        shutdown_timer.cancel()

    # Wait for 15 minutes (900 seconds)
    shutdown_timer = asyncio.create_task(asyncio.sleep(900))
    try:
        await shutdown_timer
        print("No activity for 15 minutes. Shutting down.")
        await client.close()
    except asyncio.CancelledError:
        pass


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await idle_shutdown()  # Start idle timer


@client.event
async def on_message(message):
    global shutdown_timer

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
        print("Processed an image. Resetting idle timer.")

    # Reset the shutdown timer
    await idle_shutdown()


# Run the bot
client.run(TOKEN)
