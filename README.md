# 🍴 MenuMind AI – Smart Menu Intelligence for Regional Cravings

**MenuMind AI** is a simple AI-powered tool that helps new restaurants or cafés in India design effective menus by recommending popular dishes based on **region** and **craving type**. The system takes inputs from users via dropdowns and suggests dishes from a MongoDB database.

---

## 🔥 Current Features

- ✅ **Dish Recommendations**: Based on region and craving dropdown inputs  
- 📂 **MongoDB Querying**: Matches exact or fuzzy cravings from database  
- 🔍 **Fuzzy Matching**: Allows flexible matching of craving keywords  
- 📊 **Trends Dashboard**: View top cravings and top-rated dishes per region  
- 📦 **User Input Logging**: Stores inputs for future trend analysis  

---

## 🏗️ Project Structure
menumind/
├── backend/
│ ├── init.py
│ ├── nlp_engine.py
│ ├── recommender.py
│ ├── trend_fetcher.py
│ ├── cravings_suggestion.py
├── config/
│ └── settings.py
├── data/
│ ├── craving_dataset.csv
│ ├── sample_menu.csv
├── database/
│ ├── init.py
│ ├── db_ops.py
│ ├── schema.py
│ ├── mongo_clients.py
│ ├── query.py
├── pages/
│ ├── 1_recommendation.py
│ ├── 2_trend_dashboard.py
├── test/
│ ├── init.py
│ ├── test_trend_fetcher.py
│ ├── test_recommender.py
│ ├── test_nlp_engine.py
│ ├── test_db_ops.py
├── .env
├── requirements.txt
├── main.py
├── import_data.py

## 🧠 How It Works

### 🔹 Page 1: Menu Recommender
- User selects `region` and `craving` from dropdowns  
- Backend runs `recommend_dishes(region, craving)`  
- Dish list is fetched from MongoDB and displayed with:
  - Name  
  - Category  
  - Price  
  - Rating  

### 🔹 Page 2: Trends Dashboard
- Displays analytics including:
  - Top 5 cravings from `user_inputs` log  
  - Top 5 rated dishes from `menu_items` collection  
- Region filter is available for focused trend analysis  

---

## 📌 Notes

- No text input or ML model is used in the current version  
- Inputs are stored in the `user_inputs` collection for future use  
- Focus is on simplicity and early-stage restaurant decision support  

---

## 🔮 Future Enhancements

- ✅ Feedback system for recommended dishes  
- ✅ Admin panel to upload dishes easily  
- ✅ Dashboard for regional demand prediction  
- ✅ Integration with Swiggy/Zomato for live trends  
- ✅ Advanced ML/NLP pipeline for recommendation engine  

---

## 👨‍🍳 Ideal For

- **Restaurant & Café Owners** launching in Indian cities  
- **Food Startups** wanting to optimize menus based on customer intent  
- **Analysts** studying regional food trends  

---

## 💻 Tech Stack

| Layer      | Technology       |
|------------|------------------|
| Frontend   | Streamlit        |
| Backend    | Python           |
| Database   | MongoDB          |
| Libraries  | pandas, fuzzywuzzy, python-dotenv |

