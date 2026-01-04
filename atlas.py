import json
import os

def get_mongo_uri():
    """Reads MongoDB URI from environment variable, with fallback to config.json"""
    # Try to get MongoDB URI from environment variable first
    mongo_uri = os.environ.get("MONGO_URI")
    if mongo_uri:
        return mongo_uri
    
    # Fallback to config.json if environment variable is not set
    try:
        with open("config.json") as f:
            config = json.load(f)
        return config["MONGO_URI"]
    except FileNotFoundError:
        raise Exception("MONGO_URI environment variable not set and config.json not found")
