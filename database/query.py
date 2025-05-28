import datetime
from mongo_client import db

def log_user_search(region, craving):
    return db["searches"].insert_one({
        "region": region,
        "craving": craving,
        "timestamp": datetime.datetime.utcnow()
    }).inserted_id

def get_all_searches():
    return list(db["searches"].find({}))

def log_menu_recommendation(region, craving, recommended_items):
    return db["menu_recommendations"].insert_one({
        "region": region,
        "craving": craving,
        "recommended_items": recommended_items,
        "timestamp": datetime.datetime.utcnow()
    }).inserted_id

def get_recent_recommendations(region, limit=5):
    return list(
        db["menu_recommendations"]
        .find({"region": region})
        .sort("timestamp", -1)
        .limit(limit)
    )

def log_trend(region, trending_cravings):
    return db["trend_data"].insert_one({
        "region": region,
        "trending_cravings": trending_cravings,
        "timestamp": datetime.datetime.utcnow()
    }).inserted_id

def get_recent_trends(region, limit=5):
    return list(
        db["trend_data"]
        .find({"region": region})
        .sort("timestamp", -1)
        .limit(limit)
    )

def get_menu_data_for_region(region):
    return list(db["menu_items"].find({"region": {"$regex": f"^{region}$", "$options": "i"}}))
