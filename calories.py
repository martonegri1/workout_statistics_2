'''
male_calories = (
(-55.0969 +
(0.6309 * avg_heartbeat) +
(0.1988 * weight) +
(0.2017 * age))
/ 4.184
) * duration


female_calories = (
(-20.4022 +
(0.4472 * avg_heartbeat) -
(0.1263 * weight) +
(0.0740 * age))
/ 4.184
) * duration
'''

import matplotlib.pyplot as plt
import pandas as pd


class Athlete:
    def __init__(self, name, weight, sex, age=18):
        self.name = name
        self.age = age
        self.weight = weight
        self.sex = sex


def count_calories(avg_heartbeat, weight, age, duration, sex):
    if duration < 0:
         raise ValueError("Az edzés időtatrama nem lehet negatív szám.")

    if sex == "M":
        calories = ((-55.0969 + (0.6309 * avg_heartbeat) + (0.1988 * weight) + (0.2017 * age)) / 4.184) * duration
        return calories

    elif sex == "F":
        calories = ((-20.4022 + (0.4472 * avg_heartbeat) - (0.1263 * weight) + (0.0740 * age)) / 4.184) * duration
        return calories

    else:
        raise ValueError("Az érték csak 'M' vagy 'F' lehet!")


def show_stats(df):
    df.plot(x="Nap", y="Kalória")

    plt.xlabel("Nap")
    plt.ylabel("Kalória")
    plt.title("Kalóriaégetés")

    plt.show()

def main():
    name = input("Add meg a neved: ")
    age = int(input("Add meg az életkorodat: "))
    weight = int(input("Add meg a testsúlyodat (kg): "))
    sex = input("Add meg a nemed (M/F): ")

    new_athlete = Athlete(name, weight, sex, age)

    workout_df = pd.read_excel("Workout_Data.xlsx")

    workout_df["Kalória"] = workout_df.apply(lambda row: count_calories(
        row["Szívverés(bpm)"],
        new_athlete.weight,
        new_athlete.age,
        row["Edzéshossz(perc)"],
        new_athlete.sex),
        axis=1)

    show_stats(workout_df)

if __name__ == "__main__":
    main()



