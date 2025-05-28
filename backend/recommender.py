import streamlit as st
import pandas as pd
from database.mongo_client import db
from datetime import datetime

# --- Constants ---
CRAVING_OPTIONS = [
    "Sweet", "Spicy", "Chatpata", "Starter", "Main Course",
    "Dessert", "Snacks", "Shakes", "Refreshing Drinks"
]

REGION_OPTIONS = [
    "Bhubaneswar", "Delhi", "Mumbai", "Chennai", 
    "Kolkata", "Bengaluru", "Hyderabad", "Punjab"
]

# --- Helper Functions ---

def get_menu_items(region: str, craving: str):
    """
    Fetch menu items filtered by region and craving (category) from MongoDB.
    Matching is case-insensitive.
    """
    query = {
        "region": {"$regex": f"^{region}$", "$options": "i"},
        "category": {"$regex": f"^{craving}$", "$options": "i"}
    }
    items = list(db.menu_items.find(query, {"_id": 0}))
    return items

def log_user_input(region: str, craving: str):
    """
    Logs user selections of region and craving into 'user_inputs' collection with timestamp.
    """
    log_entry = {
        "region": region,
        "craving": craving,
        "timestamp": datetime.utcnow()
    }
    db.user_inputs.insert_one(log_entry)

def get_craving_logs():
    """
    Retrieve all user input logs from the database.
    """
    return list(db.user_inputs.find({}, {"_id": 0}))

# --- Streamlit UI ---

st.set_page_config(page_title="🍽️ MenuMind Recommendations & Trends", layout="wide")
st.title("🍴 MenuMind AI - Regional Recommendations & Craving Trends")

with st.sidebar:
    st.header("User Preferences")
    selected_region = st.selectbox("Select your region:", REGION_OPTIONS)
    selected_craving = st.selectbox("Select your craving:", CRAVING_OPTIONS)
    recommend_btn = st.button("Get Recommendations")

if recommend_btn:
    with st.spinner("Fetching recommendations..."):
        # Log user input
        log_user_input(selected_region, selected_craving)

        # Fetch menu items matching region & craving
        dishes = get_menu_items(selected_region, selected_craving)

        if not dishes:
            st.warning(f"No dishes found for craving '{selected_craving}' in {selected_region}.")
        else:
            st.header(f"🍽️ Recommended {selected_craving} Dishes in {selected_region}")
            for dish in dishes:
                st.markdown(f"### {dish.get('name', 'Unnamed Dish')}")
                st.markdown(f"**Category:** {dish.get('category', 'N/A')}")
                st.markdown(f"**Price:** ₹{dish.get('price', 'N/A')}")
                st.markdown(f"**Rating:** ⭐ {dish.get('ratings', 'N/A')}")
                ingredients = dish.get('ingredients')
                if ingredients:
                    if isinstance(ingredients, list):
                        ingredients = ', '.join(ingredients)
                    st.markdown(f"**Ingredients:** {ingredients}")
                st.markdown("---")

# --- Craving Trends Dashboard ---

st.header(f"📈 Craving & Dish Trends in {selected_region}")

logs = get_craving_logs()
if not logs:
    st.warning("No craving logs available.")
else:
    df_logs = pd.DataFrame(logs)
    if "region" not in df_logs.columns or "craving" not in df_logs.columns:
        st.error("Craving logs missing required fields: 'region' and/or 'craving'.")
    else:
        # Filter logs for selected region (case-insensitive)
        filtered_logs = df_logs[df_logs["region"].str.lower() == selected_region.lower()]
        if filtered_logs.empty:
            st.info(f"No craving logs found for {selected_region}.")
        else:
            craving_counts = filtered_logs["craving"].value_counts().reset_index()
            craving_counts.columns = ["Craving", "Count"]
            st.subheader("🔥 Top Cravings")
            st.bar_chart(craving_counts.set_index("Craving"))

        # Show top rated dishes for the region (all categories)
        region_dishes = list(db.menu_items.find(
            {"region": {"$regex": f"^{selected_region}$", "$options": "i"}},
            {"_id": 0}
        ))
        if region_dishes:
            df_region = pd.DataFrame(region_dishes)
            if "ratings" in df_region.columns:
                top_dishes = df_region.sort_values(by="ratings", ascending=False).head(5)
                st.subheader("🍲 Trending Top Rated Dishes")
                for item in top_dishes.itertuples():
                    st.markdown(f"### {item.name}")
                    st.markdown(f"**Category:** {item.category}")
                    st.markdown(f"**Price:** ₹{item.price}")
                    st.markdown(f"**Rating:** ⭐ {item.ratings}")
                    st.markdown("---")
            else:
                st.info("No rating data available for dishes.")
        else:
            st.info(f"No menu items found for {selected_region}.")

st.success("✅ Data loaded successfully.")
