# Created by @mksmvnv

def user_limits():
    print("\nWelcome to Nutrient Tracker!")
    try:
        user_gender = input("""
Choose your gender:
1 - Male
2 - Female
3 - Other
Enter number: """)

        user_age = int(input("Age: "))
        user_height = float(input("Height: "))
        user_weight = float(input("Weight: "))

        user_active_level = input("""
Choose your activity level:
1 - Sedentary lifestyle
2 - Moderate activity
3 - Active lifestyle
4 - Very active lifestyle
Enter number: """)
    except ValueError:
        print("Incorrect data entered, please be careful. Try again.")
        exit()
    try:
        match user_gender:
            case "1":
                BMR = 66 + (13.75 * user_weight) + (5 * user_height) - (
                    6.75 * user_age)
            case "2":
                BMR = 655 + (9.56 * user_weight) + (1.85 * user_height) - (
                    4.68 * user_age)
            case "3":
                print("Sorry. On planet Earth we only have 2 genders.\n")
                exit()
            case _:
                print("Invalid choice.")
                exit()
    except ValueError:
        print("Incorrect data entered, please be careful. Try again.")
        exit()
    try:
        match user_active_level:
            case "1":
                CALORIE_LIMIT = BMR * 1.2
            case "2":
                CALORIE_LIMIT = BMR * 1.375
            case "3":
                CALORIE_LIMIT = BMR * 1.55
            case "4":
                CALORIE_LIMIT = BMR * 1.725
            case _:
                print("Invalid choice.")
                exit()
    except ValueError:
        print("Incorrect data entered, please be careful. Try again.")
        exit()
    PROTEINS_LIMIT = (CALORIE_LIMIT * 0.3) / 4
    FATS_LIMIT = (CALORIE_LIMIT * 0.3) / 9
    CARBS_LIMIT = (CALORIE_LIMIT * 0.4) / 4
    user_limits_data = {
        "CALORIE_LIMIT": CALORIE_LIMIT,
        "PROTEINS_LIMIT": PROTEINS_LIMIT,
        "FATS_LIMIT": FATS_LIMIT,
        "CARBS_LIMIT": CARBS_LIMIT
    }
    return user_limits_data
