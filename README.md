#🍴 MenuMind AI – Smart Menu Intelligence for Regional Cravings
MenuMind AI is a simple AI-powered tool that helps new restaurants or cafés in India design effective menus by recommending popular dishes based on region and craving type. The system takes inputs from users via dropdowns and suggests dishes from a MongoDB database.

🔥 Current Features
✅ Dish Recommendations: Based on region and craving dropdown inputs
📂 MongoDB Querying: Matches exact or fuzzy cravings from database
🔍 Fuzzy Matching: Allows flexible matching of craving keywords
📊 Trends Dashboard: View top cravings and top-rated dishes per region
📦 User Input Logging: Stores inputs for future trend analysis

Project structure :
menumind/
├── backend/
│   ├── __init__.py
│   ├── nlp_engine.py
│   ├── recommender.py
│   ├── trend_fetcher.py
│   ├── cravings_suggestion.py
├── config/
│   └── settings.py
├── data/
│   ├── craving_dataset.csv
│   ├── sample_menu.csv
├── database/
│   ├── __init__.py
│   ├── db_ops.py
│   ├── schema.py
│   ├── mongo_clients.py
│   ├── query.py
├── pages/
│   ├── 1_recommendation.py
│   ├── 2_trend_dashboard.py
├── test/
│   ├── __init__.py
│   ├── test_trend_fetcher.py
│   ├── test_recommender.py
│   ├── test_nlp_engine.py
│   ├── test_db_ops.py
├── .env
├── requirements.txt
├── main.py
├── import_data.py



🧠 How It Works
Page 1: Menu Recommender
User selects region and craving from dropdowns

Backend runs recommend_dishes(region, craving)

Dish list is fetched and shown with name, category, rating, and price

Page 2: Trends Dashboard
Shows:

Top 5 cravings from user_inputs log

Top 5 rated dishes from menu_items

Region filter is available


📌 Notes
Currently no text input or learning model is used – just dropdown inputs + direct DB match

Inputs are still logged in the user_inputs collection for future training or analysis


🔮 Future Enhancements
✅ Feedback system for recommended dishes

✅ Admin panel to upload dishes easily

✅ Dashboard for regional demand prediction

✅ Integration with Swiggy/Zomato for live trends

✅ Advanced ML/NLP pipeline for recommendation engine


👨‍🍳 Ideal For
Restaurant & Café Owners launching in Indian cities

Food startups wanting to optimize menus based on customer intent

Analysts studying regional food trends
