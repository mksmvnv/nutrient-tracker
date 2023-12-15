from dataclasses import dataclass

import numpy as np
import matplotlib.pyplot as plt

from user_goals import user_goals

today = []

user_goals = user_goals()


@dataclass
class Food:
    name: str
    calories: int
    proteins: int
    fats: int
    carbs: int


done = False

while not done:

    choice = input("""
Menu:
1 - Add a new food
2 - Visualize progress
3 - Quit
Enter number: """)

    match choice:
        case "1":
            print("Adding a new food!")
            name = input("Name: ")
            calories = int(input("Calories: "))
            proteins = int(input("Proteins: "))
            fats = int(input("Fats: "))
            carbs = int(input("Carbs: "))
            food = Food(name, calories, proteins, fats, carbs)
            today.append(food)
            print("Successfully added!")
        case "2":
            calories_sum = sum(food.calories for food in today)
            proteins_sum = sum(food.proteins for food in today)
            fats_sum = sum(food.fats for food in today)
            carbs_sum = sum(food.carbs for food in today)
            fig, axs = plt.subplots(2, 2)
            axs[0, 0].pie([proteins_sum, fats_sum, carbs_sum],
                          labels=["Proteins", "Fats", "Carbs"],
                          autopct="%1.1f%%")
            axs[0, 0].set_title("Macronutriens Distribution")
            axs[0, 1].bar([0, 1, 2], [proteins_sum, fats_sum, carbs_sum],
                          width=0.4)
            axs[0, 1].bar([0.5, 1.5, 2.5], [
                user_goals["PROTEINS_GOAL"], user_goals["FATS_GOAL"],
                user_goals["CARBS_GOAL"]
            ],
                          width=0.4)
            axs[0, 1].set_title("Macronutriens Progress")
            axs[0, 1].set_xticks([0.25, 1.25, 2.25])
            axs[0, 1].set_xticklabels(["Proteins", "Fats", "Carbs"])
            axs[1, 0].pie([
                calories_sum, user_goals["CALORIE_GOAL_LIMIT"] - calories_sum
            ],
                          labels=["Calories", "Remaining"],
                          autopct="%1.1f%%")
            axs[1, 0].set_title("Calories Goal Progress")
            axs[1, 1].plot(list(range(len(today))),
                           np.cumsum([food.calories for food in today]),
                           label="Calories Eaten")
            axs[1, 1].plot(list(range(len(today))),
                           [user_goals["CALORIE_GOAL_LIMIT"]] * len(today),
                           label="Calorie Goal")
            axs[1, 1].legend()
            axs[1, 1].set_title("Calories Goal Over Time")
            fig.tight_layout()
            plt.show()
        case "3":
            done = True
        case _:
            print("Invalid choice.")
