# Created by @mksmvnv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from dataclasses import dataclass
from core.user_limits import user_limits

user_limits = user_limits()


@dataclass
class Food:
    name: str
    calories: float
    proteins: float
    fats: float
    carbs: float


def tracker_menu():
    current_data = []
    done = False

    while not done:

        choice = input("""
Menu:
1 - Add a new food
2 - Food list
3 - Visualize progress
4 - Quit
Enter number: """)

        match choice:
            case "1":
                print("Adding a new food!")
                try:
                    name = input("Name: ")
                    calories = float(input("Calories: "))
                    proteins = float(input("Proteins: "))
                    fats = float(input("Fats: "))
                    carbs = float(input("Carbs: "))
                    food = Food(name, calories, proteins, fats, carbs)
                    current_data.append(food)
                    print("Successfully added!")
                except ValueError:
                    print(
                        "Invalid input. Please enter valid numbers for calories, proteins, fats, and carbs."
                    )

            case "2":
                food_list = pd.DataFrame(
                    current_data, index=range(1, len(current_data)+1))
                print(food_list)

            case "3":
                try:
                    default_size = plt.rcParams["figure.figsize"]
                    window_size = (1000, 600)
                    dpi = window_size[0] / default_size[0]
                    plt.style.use("./custom.mplstyle")
                    calories_sum = sum(food.calories for food in current_data)
                    proteins_sum = sum(food.proteins for food in current_data)
                    fats_sum = sum(food.fats for food in current_data)
                    carbs_sum = sum(food.carbs for food in current_data)
                    fig, axs = plt.subplots(2,
                                            2,
                                            figsize=(window_size[0] / dpi,
                                                     window_size[1] / dpi),
                                            dpi=dpi)
                    axs[0, 0].pie([proteins_sum, fats_sum, carbs_sum],
                                  labels=["Proteins", "Fats", "Carbs"],
                                  autopct="%1.1f%%",
                                  textprops={'fontsize': 8},
                                  colors=["#379efb", "#ffa438", "#49cc10"])
                    axs[0, 0].set_title("Macronutriens Distribution")
                    axs[0, 1].bar([0, 1, 2],
                                  [proteins_sum, fats_sum, carbs_sum],
                                  width=0.4,
                                  color=["#379efb", "#ffa438", "#49cc10"])
                    axs[0, 1].bar([0.5, 1.5, 2.5], [
                        user_limits["PROTEINS_LIMIT"], user_limits["FATS_LIMIT"],
                        user_limits["CARBS_LIMIT"]
                    ],
                        width=0.4,
                        color=["#f44336", "#f44336", "#f44336"])
                    axs[0, 1].set_title("Macronutriens Progress")
                    axs[0, 1].set_xticks([0.25, 1.25, 2.25])
                    axs[0, 1].set_xticklabels(["Proteins", "Fats", "Carbs"])
                    axs[1, 0].pie([
                        calories_sum,
                        user_limits["CALORIE_LIMIT"] - calories_sum
                    ],
                        labels=["Calories", "Remaining"],
                        autopct="%1.1f%%",
                        textprops={'fontsize': 8},
                        colors=["#379efb", "#f44336"])
                    axs[1, 0].set_title("Calories Goal Progress")
                    data = list(range(len(current_data)))
                    calories_eaten = np.cumsum(
                        [food.calories for food in current_data])
                    calorie_goal = [user_limits["CALORIE_LIMIT"]
                                    ] * len(current_data)
                    axs[1, 1].plot(data,
                                   calories_eaten,
                                   color="#379efb",
                                   label="Calories Eaten")
                    axs[1, 1].plot(data,
                                   calorie_goal,
                                   color="#f44336",
                                   label="Calorie Goal")
                    axs[1, 1].legend()
                    axs[1, 1].set_title("Calories Goal Over Time")
                    fig.tight_layout()
                    plt.show()
                except ValueError:
                    print("Incorrect data. Data visualization has stopped.")
                    exit()

            case "4":
                done = True

            case _:
                print("Invalid choice.")
