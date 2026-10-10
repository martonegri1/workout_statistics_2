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



