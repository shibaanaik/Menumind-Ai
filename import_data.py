import csv
from database.mongo_client import db

def import_menu_items(csv_path):
    menu_collection = db["menu_items"]
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        menu_items = []
        for row in reader:
            item = {
                "name": row["name"],
                "category": row["category"],
                "ingredients": [i.strip() for i in row["ingredients"].split(",")],
                "region": row["region"],
                "spiciness": row["spiciness"],
                "price": float(row["price"]),
                "ratings": float(row["ratings"])
            }
            menu_items.append(item)
        if menu_items:
            menu_collection.insert_many(menu_items)
            print(f"Inserted {len(menu_items)} menu items.")

def import_cravings(csv_path):
    craving_collection = db["cravings"]
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        cravings = []
        for row in reader:
            cravings.append({
                "region": row["region"],
                "craving": row["craving"]
            })
        if cravings:
            craving_collection.insert_many(cravings)
            print(f"Inserted {len(cravings)} craving entries.")

if __name__ == "__main__":
    import_menu_items("data/sample_menu.csv")
    
