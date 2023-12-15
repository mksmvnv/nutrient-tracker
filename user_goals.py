def user_goals():
    print("Welcome to your Calorie Tracker!")
    GENDER = input("""
Choose your gender:
1 - Male
2 - Female
3 - Other
Enter number: """)
    AGE = int(input("Age: "))
    HEIGHT = float(input("Height: "))
    WEIGHT = float(input("Weight: "))
    ACTIVE_LEVEL = input("""
Choose your activity level:
1 - Sedentary lifestyle
2 - Moderate activity
3 - Active lifestyle
4 - Very active lifestyle
Enter number: """)

    match GENDER:
        case "1":
            BMR = 66 + (13.75 * WEIGHT) + (5 * HEIGHT) - (6.75 * AGE)
        case "2":
            BMR = 655 + (9.56 * WEIGHT) + (1.85 * HEIGHT) - (4.68 * AGE)
        case "3":
            print("Sorry. On planet Earth we only have 2 genders.\n")
            exit()
        case _:
            print("Invalid choice.")
            exit()

    match ACTIVE_LEVEL:
        case "1":
            CALORIE_GOAL_LIMIT = BMR * 1.2
        case "2":
            CALORIE_GOAL_LIMIT = BMR * 1.375
        case "3":
            CALORIE_GOAL_LIMIT = BMR * 1.55
        case "4":
            CALORIE_GOAL_LIMIT = BMR * 1.725
        case _:
            print("Invalid choice.")
            exit()

    PROTEINS_GOAL = (CALORIE_GOAL_LIMIT * 0.3) / 4
    FATS_GOAL = (CALORIE_GOAL_LIMIT * 0.3) / 9
    CARBS_GOAL = (CALORIE_GOAL_LIMIT * 0.4) / 4

    goals_data = {
        "CALORIE_GOAL_LIMIT": CALORIE_GOAL_LIMIT,
        "PROTEINS_GOAL": PROTEINS_GOAL,
        "FATS_GOAL": FATS_GOAL,
        "CARBS_GOAL": CARBS_GOAL
    }

    return goals_data
