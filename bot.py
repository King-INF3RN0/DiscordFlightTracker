import os
import discord
from dotenv import load_dotenv
from config_loader import load_config, ConfigError

# Load .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Load config
try:
    config = load_config()
except ConfigError as e:
    print(f"[CONFIG ERROR] {e}")
    exit(1)

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"[BOT] Logged in as {client.user}")

# Start bot
client.run(TOKEN)
