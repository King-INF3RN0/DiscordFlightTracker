# Discord Flight Tracker

A clean and configurable Discord bot that posts real-time aircraft arrival and departure information into your server based on scraped data from public sources like Flightradar24 and FlightAware.

Ideal for student pilots, A&P students, ramp agents, and aviation enthusiasts who want timely flight updates during specific time windows.

---

## Features

- Daily automated flight brief at a configurable time (e.g., 5:45 PM)
- Monitors specified airline flights (e.g., UPS or Delta) to/from any airport (e.g., KTPA or KSLC) in a given time window
- Role-based pings based on day of week (Weekday, Saturday, Sunday)
- Real-time ETA tracking and 10-minute alert pings before arrival/departure
- Built-in fallback between Flightradar24 and FlightAware
- Debug logging to a separate Discord channel with user mentions for failed data sources
- Slash command support (`/check`) for manual flight checks

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

- Copy the template file to `.env`:

```bash
copy env.template .env
```

- Open `.env` and add your Discord bot token:

```
DISCORD_TOKEN=your_token_here
```

> Never share or commit your `.env` file.

---

## Configuration

Edit `config.json` to control:

- Time windows
- Tracked airport and airline codes
- Discord channel and role IDs
- User to @mention in case of fallback or scrape failure

---

## Creating and Connecting Your Discord Bot

Follow these steps to create a Discord bot, add it to your server, and connect it with this project:

### 1. Create a Bot in the Discord Developer Portal

- Go to [https://discord.com/developers/applications](https://discord.com/developers/applications)
- Click **"New Application"**
- Name your bot and click **"Create"**
- In the left sidebar, click **"Bot"**
- Click **"Add Bot"** → **"Yes, do it!"**

### 2. Copy the Bot Token

- In the **Bot** tab, click **"Reset Token"** if needed
- Copy the token and paste it into `.env`:

```
DISCORD_TOKEN=your_token_here
```

---

## Invite the Bot to Your Server

### OAuth2 → URL Generator:

#### Scopes:
- [x] `bot`
- [x] `applications.commands`

#### Bot Permissions:
- [x] Send Messages
- [x] Read Message History
- [x] View Channels
- [x] Mention Everyone
- [x] Embed Links
- [x] Attach Files

Copy the generated URL, open it in your browser, and invite the bot to your server.

---

## Safe Testing

- Use a private test channel and role.
- Temporarily assign the role only to yourself.
- Adjust `config.json` to avoid pinging anyone else while testing.

---

## Manual Commands

After inviting and running your bot, type:

```
/check
```

This will trigger a manual fetch of all flights in the configured time window and return them in Discord.

---

## Version

See the [VERSION](./VERSION) file for the current release.

---

## License

MIT License. Contributions are welcome via pull request.
