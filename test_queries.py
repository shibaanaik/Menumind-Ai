from database.query import (
    log_user_search,
    get_all_searches,
    log_menu_recommendation,
    get_recent_recommendations,
    log_trend,
    get_recent_trends
)

# 1. Test search logging
print("Logging user search...")
log_user_search("Delhi", "spicy lunch")

# 2. Fetch all searches
print("\nAll Searches:")
searches = get_all_searches()
for search in searches:
    print(search)

# 3. Log a recommendation
print("\nLogging menu recommendation...")
log_menu_recommendation("Delhi", "spicy lunch", ["Paneer Tikka", "Chicken Biryani"])

# 4. Fetch recent recommendations
print("\nRecent Recommendations:")
recommendations = get_recent_recommendations("Delhi")
for rec in recommendations:
    print(rec)

# 5. Log a trend
print("\nLogging trend data...")
log_trend("Delhi", ["spicy lunch", "butter chicken", "chole bhature"])

# 6. Fetch recent trends
print("\nRecent Trends:")
trends = get_recent_trends("Delhi")
for trend in trends:
    print(trend)
