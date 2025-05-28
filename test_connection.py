from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch Mongo URI from environment
mongo_uri = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(mongo_uri)

# List databases to confirm connection
try:
    print("✅ Databases in your cluster:")
    print(client.list_database_names())
except Exception as e:
    print("❌ Error connecting to MongoDB:", e)
