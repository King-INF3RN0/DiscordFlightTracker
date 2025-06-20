import os
import requests
from datetime import datetime, time, date
from typing import List, Dict, Any
import pytz
import json

class FlightScraperAPI:
    def __init__(self, config: Dict[str, Any]):
        self.api_url = "http://api.aviationstack.com/v1/flights"
        self.api_key = os.getenv("AVIATIONSTACK_API_KEY")
        self.airport = config["flight_tracking"]["airport"].upper()
        self.airlines = [airline.upper() for airline in config["flight_tracking"]["airlines"]]
        self.start_time_str = config["flight_tracking"]["time_window"]["start"]
        self.end_time_str = config["flight_tracking"]["time_window"]["end"]
        self.timezone = config["general"].get("timezone", "UTC")

        self.start_time = self._parse_time(self.start_time_str)
        self.end_time = self._parse_time(self.end_time_str)

    def _parse_time(self, time_str: str) -> time:
        return datetime.strptime(time_str, "%H:%M").time()

    def _within_time_window(self, flight_time_str: str) -> bool:
        try:
            local_tz = pytz.timezone(self.timezone)
            flight_dt = datetime.fromisoformat(flight_time_str.replace("Z", "+00:00"))
            local_dt = flight_dt.astimezone(local_tz)
            local_time = local_dt.time()
            today = date.today()
            if local_dt.date() < today:
                return False
            if self.start_time <= self.end_time:
                return self.start_time <= local_time <= self.end_time
            else:
                return local_time >= self.start_time or local_time <= self.end_time
        except Exception as e:
            print(f"[DEBUG] Time parsing error: {e}")
            return False

    def _update_api_call_counter(self):
        counter_file = "api_call_counter.txt"
        count = 100
        if os.path.exists(counter_file):
            with open(counter_file, "r") as f:
                try:
                    count = int(f.read().strip())
                except ValueError:
                    count = 100
        count = max(count - 1, 0)
        with open(counter_file, "w") as f:
            f.write(str(count))
        print(f"[DEBUG] API calls remaining: {count}")

    def fetch_flights(self) -> List[Dict[str, Any]]:
        if not self.api_key:
            print("[ERROR] Missing AviationStack API key. Set AVIATIONSTACK_API_KEY in your .env file.")
            return []

        all_flights = []

        for direction in ["arr_iata", "dep_iata"]:
            params = {
                "access_key": self.api_key,
                direction: self.airport,
                "limit": 100
            }

            try:
                print(f"[DEBUG] Sending API request to {self.api_url} with params: {params}")
                response = requests.get(self.api_url, params=params)
                response.raise_for_status()
                self._update_api_call_counter()
                data = response.json()

                with open(f"aviationstack_raw_dump_{direction}.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2)

                if "data" in data:
                    all_flights.extend(data["data"])
                else:
                    print(f"[API ERROR] Unexpected format in response for {direction}")
            except requests.RequestException as e:
                print(f"[API ERROR] {e}")

        filtered = []
        print("[DEBUG] Examining flights...")
        for flight in all_flights:
            flight_info = flight.get("flight") or {}
            airline_info = flight.get("airline") or {}
            departure_info = flight.get("departure") or {}
            arrival_info = flight.get("arrival") or {}
            aircraft_info = flight.get("aircraft") or {}

            flight_number = flight_info.get("iata") or ""
            airline_code = airline_info.get("iata") or ""
            icao_code = airline_info.get("icao") or ""
            dep_iata = departure_info.get("iata") or ""
            arr_iata = arrival_info.get("iata") or ""
            scheduled_arrival = arrival_info.get("scheduled") or ""
            estimated_arrival = arrival_info.get("estimated") or ""
            scheduled_departure = departure_info.get("scheduled") or ""
            estimated_departure = departure_info.get("estimated") or ""
            aircraft_type = aircraft_info.get("icao24") or ""

            direction = None
            scheduled_time = ""
            estimated_time = ""
            origin = ""
            destination = ""

            if arr_iata.upper() == self.airport:
                direction = "arrival"
                scheduled_time = scheduled_arrival
                estimated_time = estimated_arrival
                origin = dep_iata
                destination = arr_iata
            elif dep_iata.upper() == self.airport:
                direction = "departure"
                scheduled_time = scheduled_departure
                estimated_time = estimated_departure
                origin = arr_iata
                destination = dep_iata
            else:
                continue

            print(f"[DEBUG] Flight {flight_number} | Airline: {airline_code}/{icao_code} | Scheduled: {scheduled_time} | Direction: {direction}")

            if not all([flight_number, airline_code, origin, destination, scheduled_time, estimated_time]):
                print("[DEBUG] Skipping: missing data")
                continue

            if not any(code in self.airlines for code in [airline_code.upper(), icao_code.upper()]):
                print(f"[DEBUG] Skipping: airline {airline_code}/{icao_code} not in tracked list {self.airlines}")
                continue

            if not self._within_time_window(scheduled_time):
                print(f"[DEBUG] Skipping: scheduled time {scheduled_time} outside of window")
                continue

            filtered.append({
                "flight_number": flight_number,
                "aircraft_type": aircraft_type,
                "origin": origin,
                "destination": destination,
                "scheduled_time": scheduled_time,
                "estimated_time": estimated_time,
                "direction": direction
            })

        filtered.sort(key=lambda f: f["scheduled_time"])

        print(f"[DEBUG] Total flights returned by API: {len(all_flights)} | Tracked: {len(filtered)}")
        return filtered
