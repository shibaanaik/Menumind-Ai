import pytest
import sys
import os
# Add the parent directory to the sys.path to allow imports from the root of the project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.recommender import recommend_menu_items

# Mock test data
mock_region = "Bengaluru"
mock_craving = "Spicy"
mock_trend_data = [{"food_item": "Spicy chicken wings", "trend_score": 8}]
mock_menu_items = [
    {"name": "Spicy chicken wings", "category": "Appetizer", "ingredients": "Chicken, Spices, Sauce", "price": 10},
    {"name": "Grilled chicken", "category": "Main Course", "ingredients": "Chicken, Grill, Herbs", "price": 12},
]

# Mock function to replace actual trend fetcher call
def mock_get_trends(region, food_keywords):
    return mock_trend_data

# Mock function to replace actual database call
def mock_get_menu_items(region):
    return mock_menu_items

def test_recommend_menu_items():
    # Use the mock functions to override actual ones
    recommend_menu_items.__globals__['get_trends'] = mock_get_trends
    recommend_menu_items.__globals__['get_menu_items'] = mock_get_menu_items

    # Call the function with the test inputs
    result = recommend_menu_items(mock_region, mock_craving)

    assert len(result) > 0  # Should return some items
    assert result[0]['name'] == "Spicy chicken wings"  # Should match the "Spicy chicken wings" item
    assert result[0]['trend_score'] == 8  # Trend score should match
