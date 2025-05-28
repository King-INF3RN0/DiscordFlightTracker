import json
import os

class ConfigError(Exception):
    pass

def load_config(path="config.json"):
    if not os.path.exists(path):
        raise ConfigError(f"Config file not found: {path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            config = json.load(f)
    except json.JSONDecodeError as e:
        raise ConfigError(f"Failed to parse config.json: {e}")

    required_fields = [
        "general",
        "flight_tracking",
        "discord"
    ]

    for field in required_fields:
        if field not in config:
            raise ConfigError(f"Missing required section: '{field}' in config.json")

    return config
