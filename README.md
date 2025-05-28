# UPS Flight Tracker Bot

A Discord bot that posts real-time UPS flight arrival/departure information into your server based on scraped data from Flightradar24 and FlightAware. Ideal for student pilots, A&P students, and ramp workers tracking cargo flights at night.

---

## ✈ Features

- Daily automated flight brief at a configurable time (e.g., 5:45 PM).
- Monitors UPS flights to/from KTPA (or any airport) from 6:00 PM to 12:59 AM.
- Role-based pings based on day of week (Weekday/Saturday/Sunday).
- Real-time ETA updates and 10-minute warning alerts.
- Smart fallback system: Flightradar24 first, FlightAware as backup.
- Debug notices are sent to a dedicated debug channel if issues arise.

---

## 🚀 Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/UPSFlightBot.git
cd UPSFlightBot
