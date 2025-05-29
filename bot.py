import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from config_loader import load_config, ConfigError
from flight_scraper_fr24 import FlightScraperFR24

# Load environment variables
load_dotenv(override=True)
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    print("[ERROR] DISCORD_TOKEN not found in environment. Please check your .env file.")
    exit(1)

try:
    config = load_config()
except ConfigError as e:
    print(f"[CONFIG ERROR] {e}")
    exit(1)

# No privileged intents needed for slash commands
intents = discord.Intents.none()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"[BOT] Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()  # Global sync only
        print(f"[BOT] Synced {len(synced)} global slash commands")
    except Exception as e:
        print(f"[SYNC ERROR] {e}")

@bot.tree.command(
    name="check",
    description="Manually check for upcoming tracked flights"
)
async def check_flights(interaction: discord.Interaction):
    scraper = FlightScraperFR24(config)
    flights = scraper.fetch_flights()

    if not flights:
        await interaction.response.send_message("No flights found in the configured time window.")
        return

    response = "**Tracked Flights**\n\n"

    for flight in flights:
        fr24_link = f"https://www.flightradar24.com/{flight['flight_number']}"
        response += (
        f"Flight: {flight['flight_number']} ({flight['aircraft_type']})\n"
        f"From {flight['origin']} to {flight['destination']} | ETA: {flight['estimated_time']}\n"
        f"Link: {fr24_link}\n\n"
    )


    await interaction.response.send_message(response)

# Run the bot
bot.run(TOKEN)
