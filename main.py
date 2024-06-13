import sys
import items
import meals
import create
import profiles

def display_menu():
    print("Select an option:")
    print("1] Meals")
    print("2] Create")
    print("3] Items")
    print("4] Update")
    print("5] Profiles")
    print("6] Exit")

def display_items_menu():
    print("Select a category:")
    for i, category in enumerate(items.categories.keys(), 1):
        print(f"{i}] {category.capitalize()}")
    print("9] Back")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            meals.show_meals()
        elif choice == '2':
            create.create_meal()
        elif choice == '3':
            while True:
                display_items_menu()
                sub_choice = input("Enter your choice: ")

                if sub_choice == '9':
                    break
                elif sub_choice.isdigit() and 1 <= int(sub_choice) <= len(items.categories):
                    category = list(items.categories.keys())[int(sub_choice) - 1]
                    print(f"Items in category: {category.capitalize()}")
                    for item in items.categories[category]:
                        print(f"- {item}")
                else:
                    print("Invalid choice. Please try again.")
        elif choice == '4':
            items.update_nutrition_data()
        elif choice == '5':
            profiles.manage_profiles()
        elif choice == '6':
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
