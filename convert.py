
# Temperature conversion formula
# https://www.rapidtables.com/convert/temperature/celsius-to-fahrenheit.html
# celsius to fahrenheit formula
# T(°F) = (°C) × 9/5 + 32
# fahrenheit to celsius formula
# T(°C) = (°F) - 32) × 5/9

def celsius_to_fahrenheit(celsius):

    fahrenheit = celsius * (9 / 5) + 32
    return round(float(fahrenheit), 2)


def fahrenheit_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5 / 9
    return round(float(celsius), 2)
