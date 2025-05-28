from pymongo import MongoClient
from datetime import datetime
import os

# MongoDB setup
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://menuuser11:Shibaa2003@menumind-cluster.dbupyox.mongodb.net/?retryWrites=true&w=majority"
)  # Replace with your actual URI or load from env
client = MongoClient(MONGO_URI)
db = client["menu_db"]
user_logs_collection = db["user_logs"]

def log_user_input(region: str, craving: str, suggestion: str = None):
    """
    Logs the user's input (region, craving) and optional suggestion into MongoDB.

    Parameters:
    - region (str): The region/city the user enters (e.g., "Bhubaneswar").
    - craving (str): The craving type (e.g., "dessert").
    - suggestion (str, optional): The dish the user wanted or suggested, if AI couldn't find one.

    Returns:
    - result (dict): A dict indicating success or failure.
    """
    try:
        log_entry = {
            "region": region.strip().title(),
            "craving": craving.strip().lower(),
            "user_suggestion": suggestion.strip().title() if suggestion else None,
            "timestamp": datetime.utcnow()
        }
        user_logs_collection.insert_one(log_entry)
        return {"status": "success", "message": "User input logged successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
