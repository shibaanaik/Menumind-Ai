# database/mongo_client.py
from pymongo import MongoClient

# Your MongoDB connection URI (hardcoded here, but ideally use environment variables for security)
MONGO_URI = "mongodb+srv://menuuser11:Shibaa2003@menumind-cluster.dbupyox.mongodb.net/?retryWrites=true&w=majority"

# Create a MongoDB client
client = MongoClient(MONGO_URI)

# Connect to your specific database
db = client["menumind_db"]
