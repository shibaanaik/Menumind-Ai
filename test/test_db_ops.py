import pytest
import sys
import os
# Add the parent directory to the sys.path to allow imports from the root of the project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_ops import insert_menu_item, log_user_search, insert_recommendations, get_menu_items, get_all_searches, get_recommendations

# Test insert menu item
def test_insert_menu_item():
    menu_item_id = insert_menu_item("Spicy Chicken Curry", "Main Course", ["Chicken", "Spices", "Rice"], "mumbai", "Spicy", 250, 4.5)
    assert menu_item_id is not None
    print(f"Inserted menu item with ID: {menu_item_id}")

# Test log user search
def test_log_user_search():
    search_id = log_user_search("mumbai", "spicy lunch")
    assert search_id is not None
    print(f"Logged user search with ID: {search_id}")

# Test insert recommendation
def test_insert_recommendation():
    recommendation_id = insert_recommendations(1, "mumbai", "spicy lunch", ["Spicy Chicken Curry", "Paneer Tikka", "Chili Chicken"])
    assert recommendation_id is not None
    print(f"Inserted recommendation with ID: {recommendation_id}")

# Test fetching menu items
def test_get_menu_items():
    menu_items = get_menu_items(region="mumbai", category="Main Course")
    assert len(menu_items) > 0  # Check that we got some results
    print(f"Menu Items in Mumbai (Main Course): {menu_items}")

# Test fetching all user searches
def test_get_all_searches():
    searches = get_all_searches()
    assert len(searches) > 0  # Assuming there are searches in the database
    print(f"All User Searches: {searches}")

# Test fetching recommendations for a user
def test_get_recommendations():
    recommendations = get_recommendations(user_id=1)
    assert len(recommendations) > 0  # Check if recommendations are fetched
    print(f"Recommendations for User 1: {recommendations}")
