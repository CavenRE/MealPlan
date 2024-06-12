import os
import requests
from tabulate import tabulate
import config # Dont forget to make this file with your API key else it will break

api_key = config.API_KEY
headers = {'X-Api-Key': api_key}

# Categories of food items and yeah, add in as you need, the API will get the info for you
categories = {
    'protein': [
        'Chicken breast skinless',
        'Chicken breast boneless',
        'Chicken thigh skinless',
        'Chicken thigh boneless',
        'Chicken drumstick',
        'Chicken wing',
        'Whole chicken',
        'Beef steak sirloin',
        'Beef steak ribeye',
        'Ground beef lean',
        'Ground beef regular',
        'Beef ribs',
        'Beef brisket',
        'Pork chops bone-in',
        'Pork chops boneless',
        'Pork loin',
        'Ground pork',
        'Pork ribs',
        'Hake fillet',
        'Haddock fillet',
        'Salmon fillet',
        'Tuna steak',
        'Eggs',
        'Tofu',
        'Lamb chops',
        'Lamb leg',
        'Turkey breast',
        'Turkey thigh'
    ],
    'carbs': [
        'White rice',
        'Brown rice',
        'Jasmine rice',
        'Basmati rice',
        'Wild rice',
        'White potatoes',
        'Sweet potatoes',
        'Red potatoes',
        'Yukon Gold potatoes',
        'Quinoa',
        'Oats',
        'Barley (contains gluten)',
        'Couscous (contains gluten)',
        'Bulgur (contains gluten)',
        'Spaghetti (contains gluten)',
        'Penne (contains gluten)',
        'Fusilli (contains gluten)',
        'Macaroni (contains gluten)',
        'Fettuccine (contains gluten)',
        'White bread (contains gluten)',
        'Whole wheat bread (contains gluten)',
        'Sourdough bread (contains gluten)',
        'Rye bread (contains gluten)',
        'Corn',
        'Lentils',
        'Chickpeas',
        'Black beans'
    ],
    'fruits': [
        'Blueberries',
        'Strawberries',
        'Raspberries',
        'Blackberries',
        'Oranges',
        'Lemons',
        'Limes',
        'Grapefruits',
        'Pineapple',
        'Mango',
        'Papaya',
        'Guava',
        'Watermelon',
        'Cantaloupe',
        'Honeydew',
        'Peaches',
        'Plums',
        'Cherries',
        'Apricots',
        'Apples',
        'Pears',
        'Bananas',
        'Grapes',
        'Kiwifruit',
        'Pomegranates'
    ],
    'vegetables': [
        'Lettuce Iceberg',
        'Lettuce Romaine',
        'Spinach',
        'Kale',
        'Swiss Chard',
        'Cabbage Green',
        'Cabbage Red',
        'Broccoli',
        'Cauliflower',
        'Brussels Sprouts',
        'Carrots',
        'Beets',
        'Radishes',
        'Turnips',
        'Onions Yellow',
        'Onions Red',
        'Onions White',
        'Garlic',
        'Leeks',
        'Shallots',
        'Spring Onions',
        'Bell Peppers Green',
        'Bell Peppers Red',
        'Bell Peppers Yellow',
        'Bell Peppers Orange',
        'Chili Peppers',
        'Jalapenos',
        'Zucchini',
        'Butternut Squash',
        'Acorn Squash',
        'Spaghetti Squash',
        'Tomatoes',
        'Cucumbers',
        'Celery',
        'Eggplant',
        'Green Beans',
        'Peas'
    ],
    'spices': [
        'Black Pepper',
        'White Pepper',
        'Salt',
        'Garlic Salt',
        'Celery Salt',
        'Paprika',
        'Cayenne Pepper',
        'Chili Powder',
        'Cumin',
        'Coriander',
        'Basil (Dried)',
        'Oregano (Dried)',
        'Thyme (Dried)',
        'Rosemary (Dried)',
        'Sage (Dried)',
        'Parsley (Dried)',
        'Dill (Dried)',
        'Turmeric',
        'Ginger (Ground)',
        'Nutmeg',
        'Cinnamon',
        'Cloves',
        'Allspice',
        'Bay Leaves'
    ],
    'oils_and_fats': [
        'Olive Oil',
        'Avocado Oil',
        'Coconut Oil',
        'Canola Oil',
        'Sesame Oil',
        'Peanut Oil',
        'Sunflower Oil',
        'Grapeseed Oil',
        'Ghee (Clarified Butter)',
        'Butter (Unsalted)',
        'Butter (Salted)',
        'Lard',
        'Shortening',
        'Margarine'
    ],
    'sauces': [
        'Soy Sauce',
        'Mayonnaise',
        'Tomato Sauce (Ketchup)',
        'Pepper Sauce',
        'Cheese Sauce',
        'Barbecue Sauce',
        'Hot Sauce',
        'Worcestershire Sauce',
        'Mustard',
        'Tartar Sauce',
        'Ranch Dressing',
        'Pesto Sauce',
        'Alfredo Sauce',
        'Teriyaki Sauce',
        'Hollandaise Sauce'
    ],
    'dairy': [
        'Whole Milk (Full Cream)',
        'Skim Milk (Low Fat)',
        '2% Milk',
        'Lactose-Free Milk',
        'Almond Milk',
        'Soy Milk',
        'Heavy Cream',
        'Whipping Cream',
        'Half and Half',
        'Sour Cream',
        'Cheddar Cheese',
        'Gouda Cheese',
        'Mozzarella Cheese',
        'Parmesan Cheese',
        'Blue Cheese',
        'Swiss Cheese',
        'Feta Cheese',
        'Cottage Cheese',
        'Yogurt (Plain)',
        'Yogurt (Greek)',
        'Butter (Unsalted)',
        'Butter (Salted)',
        'Buttermilk'
    ]
}

# Function to ensure the nutrition folder exists
def ensure_nutrition_folder_exists():
    if not os.path.exists('nutrition'):
        os.makedirs('nutrition')
        print("Created 'nutrition' folder.")

# Function to fetch nutrition data for a given item
def fetch_nutrition(item):
    url = f'https://api.calorieninjas.com/v1/nutrition?query={item}'
    print(f"Fetching nutrition data for: {item}")
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Received data for {item}")
        return response.json()['items']
    else:
        print(f"Failed to fetch data for {item}, status code: {response.status_code}")
        return []

# Function to save nutritional data to a Markdown file
def save_to_markdown(category, items):
    ensure_nutrition_folder_exists()
    markdown_content = f"# {category.capitalize()}\n\n"
    table_data = []
    headers = ["Name", "Calories", "Serving Size (g)", "Protein (g)", "Fat Total (g)", "Fat Saturated (g)", "Carbohydrates (g)", "Fiber (g)", "Sugar (g)", "Sodium (mg)"]

    for item in items:
        nutrition_data = fetch_nutrition(item)
        if nutrition_data:
            data = nutrition_data[0]
            table_data.append([
                data.get("name", ""),
                data.get("calories", 0),
                data.get("serving_size_g", 0),
                data.get("protein_g", 0),
                data.get("fat_total_g", 0),
                data.get("fat_saturated_g", 0),
                data.get("carbohydrates_total_g", 0),
                data.get("fiber_g", 0),
                data.get("sugar_g", 0),
                data.get("sodium_mg", 0)
            ])
            print(f"Added data for {item} to the table.")
    
    if table_data:
        markdown_content += tabulate(table_data, headers=headers, tablefmt="pipe")

    with open(f'nutrition/{category}.md', 'w') as file:
        file.write(markdown_content)
        print(f"Saved Markdown file for category: {category}")

# Function to update nutritional data for all categories
def update_nutrition_data():
    for category, items in categories.items():
        print(f"Processing category: {category}")
        save_to_markdown(category, items)
    print("Nutritional information fetched and saved.")