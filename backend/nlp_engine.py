# backend/nlp_engine.py

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from database.mongo_client import db

def preprocess_text(text):
    """Basic preprocessing: lowercase and strip"""
    return text.lower().strip()

def get_unique_cravings():
    """Fetch distinct craving types from menu_items collection"""
    return db.menu_items.distinct("craving")

def get_menu_items():
    """Fetch all menu items from DB"""
    return list(db.menu_items.find({}, {"_id": 0}))

def recommend_dishes(region, craving, limit=10):
    """
    Recommend dishes based on region and craving.
    Uses fuzzy matching on cravings and region.
    Returns list of menu items.
    """
    region = preprocess_text(region)
    craving = preprocess_text(craving)
    
    # Find menu items matching region (case-insensitive)
    menu_items = list(db.menu_items.find({
        "region": {"$regex": f"^{region}$", "$options": "i"}
    }, {"_id": 0}))

    if not menu_items:
        return []

    # Filter menu items where craving is a substring or fuzzy matches craving input
    filtered_items = []
    for item in menu_items:
        item_craving = item.get("craving", "").lower()
        # Direct substring match
        if craving in item_craving:
            filtered_items.append(item)
        else:
            # Fuzzy match threshold 75 (adjustable)
            score = fuzz.ratio(craving, item_craving)
            if score >= 75:
                filtered_items.append(item)

    # Sort by ratings descending, fallback to price ascending
    filtered_items.sort(key=lambda x: (-x.get("ratings", 0), x.get("price", float('inf'))))

    # Limit results
    return filtered_items[:limit]

def log_user_input(user_id, region, craving):
    """Store user input data for future analysis and learning"""
    db.user_inputs.insert_one({
        "user_id": user_id,
        "region": region,
        "craving": craving,
    })
