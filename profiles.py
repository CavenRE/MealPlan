import os

profiles_dir = 'profiles'

def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == 'female':
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        return None

def get_calorie_goals(bmr):
    maintenance = bmr * 1.55
    moderate_deficit = maintenance - 500
    aggressive_deficit = maintenance - 1000
    very_aggressive_deficit = maintenance - 1500
    return maintenance, moderate_deficit, aggressive_deficit, very_aggressive_deficit

def save_profile_to_markdown(profile_name, details, bmr, goals):
    profile_name = profile_name.lower()
    if not os.path.exists(profiles_dir):
        os.makedirs(profiles_dir)

    content = f"""
# Profile: {profile_name.capitalize()}

- **Weight:** {details['weight']} kg
- **Height:** {details['height']} cm
- **Age:** {details['age']}
- **Gender:** {details['gender']}
- **BMR:** {bmr:.2f} calories/day

## Calorie Goals

- **Maintenance Calories:** {goals['maintenance']:.2f} calories/day
- **Moderate Deficit (0.5 kg/week):** {goals['moderate_deficit']:.2f} calories/day
- **Aggressive Deficit (1 kg/week):** {goals['aggressive_deficit']:.2f} calories/day
- **Very Aggressive Deficit (1.5 kg/week):** {goals['very_aggressive_deficit']:.2f} calories/day
"""

    with open(os.path.join(profiles_dir, f"{profile_name}.md"), 'w') as file:
        file.write(content)
    print(f"Profile '{profile_name}' saved successfully.")

def load_profiles():
    profiles = {}
    if os.path.exists(profiles_dir):
        for filename in os.listdir(profiles_dir):
            if filename.endswith('.md'):
                profile_name = filename[:-3]
                profiles[profile_name] = os.path.join(profiles_dir, filename)
    return profiles

def display_profiles(profiles):
    if not profiles:
        print("No profiles found.")
        return

    for profile_name, file_path in profiles.items():
        with open(file_path, 'r') as file:
            print(file.read())

def display_profile_details(profile_name, details, bmr, goals):
    print(f"\nProfile: {profile_name.capitalize()}")
    print(f"  Weight: {details['weight']} kg")
    print(f"  Height: {details['height']} cm")
    print(f"  Age: {details['age']}")
    print(f"  Gender: {details['gender']}")
    print(f"  BMR: {bmr:.2f} calories/day")
    print(f"  Maintenance Calories: {goals['maintenance']:.2f} calories/day")
    print(f"  Moderate Deficit (0.5 kg/week): {goals['moderate_deficit']:.2f} calories/day")
    print(f"  Aggressive Deficit (1 kg/week): {goals['aggressive_deficit']:.2f} calories/day")
    print(f"  Very Aggressive Deficit (1.5 kg/week): {goals['very_aggressive_deficit']:.2f} calories/day")

def edit_profile(details):
    while True:
        print("\nEdit Profile")
        print("1] Edit Weight")
        print("2] Edit Height")
        print("3] Edit Age")
        print("4] Edit Gender")
        print("5] Confirm Profile")
        print("6] Cancel")

        choice = input("Enter your choice: ")

        if choice == '1':
            details['weight'] = float(input("Enter weight (kg): ").replace('kg', '').strip())
        elif choice == '2':
            details['height'] = float(input("Enter height (cm): ").replace('cm', '').strip())
        elif choice == '3':
            details['age'] = int(input("Enter age: ").strip())
        elif choice == '4':
            details['gender'] = input("Enter gender (male/female): ").strip().lower()
        elif choice == '5':
            return True
        elif choice == '6':
            return False
        else:
            print("Invalid choice. Please try again.")

def manage_profiles():
    profiles = load_profiles()

    while True:
        print("\nProfile Management")
        print("1] View Profiles")
        print("2] Add Profile")
        print("3] Back")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_profiles(profiles)
        elif choice == '2':
            profile_name = input("Enter profile name: ")
            weight = float(input("Enter weight (kg): ").replace('kg', '').strip())
            height = float(input("Enter height (cm): ").replace('cm', '').strip())
            age = int(input("Enter age: ").strip())
            gender = input("Enter gender (male/female): ").strip().lower()

            profile_details = {
                'weight': weight,
                'height': height,
                'age': age,
                'gender': gender
            }

            while True:
                bmr = calculate_bmr(profile_details['weight'], profile_details['height'], profile_details['age'], profile_details['gender'])
                maintenance, moderate_deficit, aggressive_deficit, very_aggressive_deficit = get_calorie_goals(bmr)

                goals = {
                    'maintenance': maintenance,
                    'moderate_deficit': moderate_deficit,
                    'aggressive_deficit': aggressive_deficit,
                    'very_aggressive_deficit': very_aggressive_deficit
                }

                display_profile_details(profile_name, profile_details, bmr, goals)

                confirm = input("Is this information correct? (Y/n): ").strip().lower()
                if confirm == 'y':
                    save_profile_to_markdown(profile_name, profile_details, bmr, goals)
                    profiles[profile_name] = os.path.join(profiles_dir, f"{profile_name}.md")
                    break
                else:
                    if edit_profile(profile_details):
                        continue
                    else:
                        print("Profile creation canceled.")
                        break
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
