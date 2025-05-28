# backend/trend_fetcher.py

from database.mongo_client import db
import pandas as pd

def fetch_craving_logs(region=None):
    """
    Fetch user craving logs.
    If region is provided, filter logs by that region (case-insensitive).
    Returns a pandas DataFrame.
    """
    query = {}
    if region:
        query["region"] = {"$regex": f"^{region}$", "$options": "i"}
    
    logs = list(db.user_inputs.find(query, {"_id": 0}))
    if not logs:
        return pd.DataFrame()
    return pd.DataFrame(logs)

def fetch_menu_items(region=None):
    """
    Fetch menu items from DB.
    If region is provided, filter menu items by that region (case-insensitive).
    Returns a pandas DataFrame.
    """
    query = {}
    if region:
        query["region"] = {"$regex": f"^{region}$", "$options": "i"}
    
    items = list(db.menu_items.find(query, {"_id": 0}))
    if not items:
        return pd.DataFrame()
    return pd.DataFrame(items)

def get_top_cravings(region=None, top_n=5):
    """
    Returns the top N cravings by count for a given region.
    If no region specified, returns top cravings overall.
    """
    logs_df = fetch_craving_logs(region)
    if logs_df.empty or "craving" not in logs_df.columns:
        return pd.DataFrame(columns=["Craving", "Count"])
    
    craving_counts = logs_df["craving"].str.lower().value_counts().reset_index()
    craving_counts.columns = ["Craving", "Count"]
    return craving_counts.head(top_n)

def get_top_dishes(region=None, top_n=5):
    """
    Returns the top N dishes sorted by ratings for a given region.
    If no region specified, returns top dishes overall.
    """
    menu_df = fetch_menu_items(region)
    if menu_df.empty or "ratings" not in menu_df.columns:
        return pd.DataFrame(columns=["name", "category", "price", "ratings"])
    
    top_dishes = menu_df.sort_values(by="ratings", ascending=False).head(top_n)
    return top_dishes[["name", "category", "price", "ratings"]]
