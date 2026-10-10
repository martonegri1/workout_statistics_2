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

def count_calories(avg_heartbeat, weight, age, duration, sex):
    if duration < 0:
        raise ValueError("Az edzés időtatrama nem lehet nulla vagy negatív szám.")

    if sex == "M":
        calories = ((-55.0969 + (0.6309 * avg_heartbeat) + (0.1988 * weight) + (0.2017 * age)) / 4.184) * duration
        return calories

    elif sex == "F":
        calories = ((-20.4022 + (0.4472 * avg_heartbeat) - (0.1263 * weight) + (0.0740 * age)) / 4.184) * duration
        return calories

    else:
        raise ValueError("Az érték csak 'M' vagy 'F' lehet!")

return calories