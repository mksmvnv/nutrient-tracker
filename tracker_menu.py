from dataclasses import dataclass
from user_goals import user_goals

import numpy as np
import matplotlib.pyplot as plt

user_goals = user_goals()


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
2 - Visualize progress
3 - Quit
Enter number: """)

        match choice:
            case "1":
                print("Adding a new food!")
                name = input("Name: ")
                calories = float(input("Calories: "))
                proteins = float(input("Proteins: "))
                fats = float(input("Fats: "))
                carbs = float(input("Carbs: "))
                food = Food(name, calories, proteins, fats, carbs)
                current_data.append(food)
                print("Successfully added!")
            case "2":
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
                axs[0, 1].bar([0, 1, 2], [proteins_sum, fats_sum, carbs_sum],
                              width=0.4,
                              color=["#379efb", "#ffa438", "#49cc10"])
                axs[0, 1].bar([0.5, 1.5, 2.5], [
                    user_goals["PROTEINS_GOAL"], user_goals["FATS_GOAL"],
                    user_goals["CARBS_GOAL"]
                ],
                              width=0.4,
                              color=["#f44336", "#f44336", "#f44336"])
                axs[0, 1].set_title("Macronutriens Progress")
                axs[0, 1].set_xticks([0.25, 1.25, 2.25])
                axs[0, 1].set_xticklabels(["Proteins", "Fats", "Carbs"])
                axs[1, 0].pie([
                    calories_sum,
                    user_goals["CALORIE_GOAL_LIMIT"] - calories_sum
                ],
                              labels=["Calories", "Remaining"],
                              autopct="%1.1f%%",
                              textprops={'fontsize': 8},
                              colors=["#379efb", "#f44336"])
                axs[1, 0].set_title("Calories Goal Progress")
                data = list(range(len(current_data)))
                calories_eaten = np.cumsum(
                    [food.calories for food in current_data])
                calorie_goal = [user_goals["CALORIE_GOAL_LIMIT"]
                                ] * len(current_data)
                axs[1, 1].plot(data,
                               calories_eaten,
                               color="#93c47d",
                               label="Calories Eaten")
                axs[1, 1].plot(data,
                               calorie_goal,
                               color="#f44336",
                               label="Calorie Goal")
                axs[1, 1].legend()
                axs[1, 1].set_title("Calories Goal Over Time")
                fig.tight_layout()
                plt.show()
            case "3":
                done = True
            case _:
                print("Invalid choice.")
