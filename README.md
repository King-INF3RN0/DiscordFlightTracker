# Discord Flight Tracker

A clean and configurable Discord bot that posts aircraft arrival and departure information into your server using the [AviationStack API](https://aviationstack.com/).

Ideal for student pilots, A&P students, ramp agents, and aviation enthusiasts who want timely flight updates during specific time windows.

---

## ✈️ Version

**Current Version:** `0.2.0`  
Released: June 7, 2025

---

## 🆕 What's New in v0.2.0

- ✅ **Switched from web scraping to AviationStack API**
- 📥 **Uses IATA codes** (e.g., `TPA` not `KTPA`) to match AviationStack formatting
- 💾 **Saves raw flight data** to `aviationstack_raw_dump.json` for easy testing/debugging
- 📊 **Tracks API usage** using `api_call_counter.txt` to prevent exceeding monthly limits
- 🐛 **More granular debug messages** to trace logic, filtered flights, and skips
- 📦 **Improved error handling** if flight data or API keys are missing

---

## Features

- ✅ Daily automated flight brief at a configurable time (e.g., 5:45 PM)
- ✅ Monitors specified airline flights (e.g., UPS or Delta) to/from any airport (e.g., TPA or ATL)
- ✅ Role-based pings based on day of week (Weekday, Saturday, Sunday)
- ✅ Real-time ETA tracking and 10-minute alert pings before arrival/departure (coming soon)
- ✅ Slash command support (`/check`) for manual flight checks
- ✅ Debug logging to a file and console
- ✅ Local API call counter to help free users stay under the limit

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/DiscordFlightTracker.git
cd DiscordFlightTracker
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

- Create a `.env` file with:

```
DISCORD_TOKEN=your_discord_bot_token
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
```

> ⚠️ Never share or commit your `.env` file.

---

## Configuration

Edit `config.json` to control:

```json
{
  "general": {
    "timezone": "US/Eastern",
    "daily_post_time": "17:45",
    "watch_interval_minutes": 10
  },
  "flight_tracking": {
    "time_window": {
      "start": "18:00",
      "end": "00:59"
    },
    "airlines": ["5X"],
    "airport": "TPA"
  },
  "discord": {
    "main_channel_id": "YOUR_CHANNEL_ID"
  }
}
```

- `airlines`: Accepts IATA codes (e.g., "5X" for UPS, "DL" for Delta)
- `airport`: Also IATA format (e.g., "TPA")

---

## Creating and Connecting Your Discord Bot

### 1. Create a Bot in the Discord Developer Portal

- Go to [https://discord.com/developers/applications](https://discord.com/developers/applications)
- Click **"New Application"**
- Name your bot and click **"Create"**
- In the left sidebar, click **"Bot"**
- Click **"Add Bot"** → **"Yes, do it!"**

### 2. Copy the Bot Token

- In the **Bot** tab, click **"Reset Token"** if needed
- Copy the token and paste it into `.env`

---

## Invite the Bot to Your Server

### OAuth2 → URL Generator:

#### Scopes:
- ✅ `bot`
- ✅ `applications.commands`

#### Bot Permissions:
- ✅ Send Messages
- ✅ Read Message History
- ✅ View Channels
- ✅ Mention Everyone
- ✅ Embed Links
- ✅ Attach Files

---

## Safe Testing

- Use a private test channel and role.
- Temporarily assign the role only to yourself.
- Adjust `config.json` to avoid pinging anyone else while testing.

---

## Manual Commands

### `/check`

Manually fetches flights in the configured time window and posts them to Discord.

---

## Debugging Tools

- ✅ Raw API responses saved to `aviationstack_raw_dump.json`
- ✅ Remaining API calls saved to `api_call_counter.txt`
- ✅ Full debug logs printed to the terminal

---

## Version Info

See the [VERSION](./VERSION) file.

---

## License

MIT License. Contributions welcome!
