import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# MongoDB URI from environment
MONGO_URI = os.getenv("MONGO_URI")

# Database name
DB_NAME = "menumind"

# Collection names (you can update these later)
SEARCH_LOG_COLLECTION = "search_logs"
RECOMMENDATION_COLLECTION = "menu_recommendations"
TREND_COLLECTION = "trend_data"