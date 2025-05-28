import streamlit as st
from database.mongo_client import db
from datetime import datetime

# --- Constants ---
REGION_OPTIONS = [
    "Bhubaneswar", "Delhi", "Mumbai", "Chennai",
    "Kolkata", "Bangalore", "Hyderabad", "Punjab"
]

CRAVING_OPTIONS = [
     "Chatpata", "Starter", "Main Course",
    "Dessert", "Snacks", "Shake", "Refreshing Drinks"
]

# --- Helper Functions ---

def get_menu_items(region=None, craving=None):
    query = {}
    if region:
        query["region"] = {"$regex": f"^{region}$", "$options": "i"}
    if craving:
        query["category"] = {"$regex": f"^{craving}$", "$options": "i"}
    items = list(db.menu_items.find(query, {"_id": 0}))
    return items

def log_user_input(region, craving):
    db.user_inputs.insert_one({
        "region": region,
        "craving": craving,
        "timestamp": datetime.utcnow()
    })

# --- Streamlit UI ---

st.set_page_config(page_title="🍽️ MenuMind Recommendations", layout="wide")
st.title("🍴 MenuMind AI - Recommendations")

with st.sidebar:
    st.header("Select Your Preferences")
    selected_region = st.selectbox("Select Region:", REGION_OPTIONS)
    selected_craving = st.selectbox("Select Craving:", CRAVING_OPTIONS)
    recommend_btn = st.button("Get Recommendations")

if recommend_btn:
    with st.spinner("Fetching recommendations..."):
        # Log user input if needed
        log_user_input(selected_region, selected_craving)

        dishes = get_menu_items(region=selected_region, craving=selected_craving)

        if not dishes:
            st.warning(f"No {selected_craving} dishes found in {selected_region}.")
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
