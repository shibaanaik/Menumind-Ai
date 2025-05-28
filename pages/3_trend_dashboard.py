import streamlit as st
import pandas as pd
from database.mongo_client import db  # MongoDB connection

st.set_page_config(page_title="📈 Regional Dish Trends", layout="wide")
st.title("📊 Trending Dishes Across Indian Regions")

@st.cache_data(ttl=300)
def load_menu_items():
    try:
        menu_items = list(db["menu_items"].find({}, {"_id": 0}))
        return menu_items
    except Exception as e:
        st.error(f"Error loading menu items from database: {e}")
        return []

# Load data
with st.spinner("Loading regional dish data..."):
    menu_items = load_menu_items()

if not menu_items:
    st.warning("No menu items found in the database.")
else:
    menu_df = pd.DataFrame(menu_items)

    # Drop missing regions
    menu_df = menu_df.dropna(subset=["region"])

    # --- REGION SELECTOR ---
    regions = sorted(menu_df["region"].str.title().unique())
    selected_region = st.selectbox("📍 Select a Region:", regions)

    # Filter by region
    region_menu = menu_df[menu_df["region"].str.lower() == selected_region.lower()]

    if region_menu.empty:
        st.info(f"No dishes found for {selected_region}.")
    else:
        # --- CATEGORY FILTER ---
        categories = sorted(region_menu["category"].dropna().unique())
        selected_category = st.selectbox("🍽️ Filter by Category:", ["All"] + categories)

        if selected_category != "All":
            filtered_menu = region_menu[region_menu["category"] == selected_category]
        else:
            filtered_menu = region_menu

        # --- CATEGORY DISTRIBUTION CHART ---
        st.subheader(f"📊 Dish Distribution by Category in {selected_region}")
        category_counts = region_menu["category"].value_counts().reset_index()
        category_counts.columns = ["Category", "Count"]
        st.bar_chart(category_counts.set_index("Category"))

        # --- TOP DISHES DISPLAY ---
        st.subheader(f"🔥 Top Rated Dishes in {selected_region} ({selected_category})")

        if filtered_menu.empty:
            st.info(f"No dishes found for category '{selected_category}' in {selected_region}.")
        else:
            top_dishes = filtered_menu.sort_values(by="ratings", ascending=False).head(5)

            for item in top_dishes.itertuples():
                with st.container():
                    cols = st.columns([2, 1, 1])
                    with cols[0]:
                        st.markdown(f"### {item.name}")
                        ingredients = ', '.join(item.ingredients) if isinstance(item.ingredients, list) else item.ingredients or "N/A"
                        st.markdown(f"**Ingredients:** {ingredients}")
                        st.markdown(f"**Category:** {item.category}")
                    with cols[1]:
                        st.markdown(f"**Price:** ₹{item.price}")
                    with cols[2]:
                        st.markdown(f"**Rating:** ⭐ {item.ratings}")
                    st.markdown("---")

        st.success("✅ Regional dish trends loaded successfully.")
