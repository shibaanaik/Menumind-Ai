# database/db_ops.py

from .mongo_client import db  #updated import
import datetime

# 1. Insert Menu Item
def insert_menu_item(name, category, ingredients, region, spiciness, price, ratings):
    """
    Insert a new menu item into the 'menu_items' collection.
    """
    menu_collection = db["menu_items"]
    menu_item = {
        "name": name,
        "category": category,
        "ingredients": ingredients,
        "region": region,
        "spiciness": spiciness,
        "price": price,
        "ratings": ratings,
        "timestamp": datetime.datetime.utcnow(),
    }
    result = menu_collection.insert_one(menu_item)
    return result.inserted_id

# 2. Log User Search
def log_user_search(region, craving):
    """
    Log a user's search with region and craving into the 'searches' collection.
    """
    searches_collection = db["searches"]
    search_data = {
        "region": region,
        "craving": craving,
        "timestamp": datetime.datetime.utcnow(),
    }
    result = searches_collection.insert_one(search_data)
    return result.inserted_id

# 3. Insert Recommendations
def insert_recommendations(user_id, region, craving, menu_items):
    """
    Insert recommendations for a user based on region and craving.
    """
    recommendations_collection = db["recommendations"]
    recommendation_data = {
        "user_id": user_id,
        "region": region,
        "craving": craving,
        "menu_items": menu_items,
        "timestamp": datetime.datetime.utcnow(),
    }
    result = recommendations_collection.insert_one(recommendation_data)
    return result.inserted_id

# 4. Fetch Menu Items
def get_menu_items(region=None, category=None):
    """
    Retrieve menu items from the 'menu_items' collection based on region and/or category.
    """
    menu_collection = db["menu_items"]
    query = {}
    if region:
        query["region"] = region
    if category:
        query["category"] = category
    return list(menu_collection.find(query))

# 5. Fetch All User Searches
def get_all_searches():
    """
    Retrieve all user searches from the 'searches' collection.
    """
    searches_collection = db["searches"]
    return list(searches_collection.find({}))

# 6. Fetch Recommendations for a User or Region
def get_recommendations(user_id=None, region=None):
    """
    Retrieve recommendations from the 'recommendations' collection for a given user or region.
    """
    recommendations_collection = db["recommendations"]
    query = {}
    if user_id:
        query["user_id"] = user_id
    if region:
        query["region"] = region
    return list(recommendations_collection.find(query))

# 7. Fetch Menu Items by Craving
def get_menu_items_by_craving(craving, region=None):
    """
    Get a list of menu items that match a specific craving and optionally a region.
    """
    menu_items = get_menu_items(region=region)
    matched_items = []
    for item in menu_items:
        if craving.lower() in item["name"].lower() or craving.lower() in item.get("description", "").lower():
            matched_items.append(item)
    return matched_items

# 8. Insert Trend Data
def insert_trend_data(food_item, region, trend_score):
    """
    Insert food trend data into the 'trends' collection.
    """
    trends_collection = db["trends"]
    trend_data = {
        "food_item": food_item,
        "region": region,
        "trend_score": trend_score,
        "timestamp": datetime.datetime.utcnow(),
    }
    result = trends_collection.insert_one(trend_data)
    return result.inserted_id

# 9. Fetch Trend Data
def get_trend_data(food_item=None, region=None):
    """
    Retrieve trend data from the 'trends' collection based on food item and/or region.
    """
    trends_collection = db["trends"]
    query = {}
    if food_item:
        query["food_item"] = food_item
    if region:
        query["region"] = region
    return list(trends_collection.find(query))
