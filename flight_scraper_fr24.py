from datetime import datetime, timedelta
from typing import List, Dict, Any

class FlightScraperFR24:
    def __init__(self, config: Dict[str, Any]):
        self.airport = config["flight_tracking"]["airport"]
        self.airlines = config["flight_tracking"]["airlines"]
        self.start_time_str = config["flight_tracking"]["time_window"]["start"]
        self.end_time_str = config["flight_tracking"]["time_window"]["end"]

        # Validate and parse time window
        self.start_time = self._parse_time(self.start_time_str)
        self.end_time = self._parse_time(self.end_time_str)

    def _parse_time(self, time_str: str) -> datetime.time:
        try:
            return datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            raise ValueError(f"Invalid time format in config: {time_str}. Expected HH:MM.")

    def fetch_flights(self) -> List[Dict[str, Any]]:
        """
        Placeholder method. Later this will:
        - Scrape Flightradar24
        - Filter flights to/from self.airport
        - Include only flights operated by self.airlines
        - Check if scheduled time is within the configured window

        For now, it returns a static example flight.
        """
        example_flight = {
            "flight_number": "5X123",
            "aircraft_type": "B767",
            "origin": "KSDF",
            "destination": self.airport,
            "scheduled_time": "20:15",
            "estimated_time": "20:25",
            "direction": "arrival"
        }

        return [example_flight]  # Replace with real data later
