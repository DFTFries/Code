
unit = input("Please enter the current unit (C/F): ")
temperature = float(input("Please enter the Temperature you want to convert: "))

if unit.lower() == "c":
    result = temperature * 1.8 + 32
    print(f"The temperature is {round(result, 1)}°F")
elif unit.lower() == "f":
    result = (temperature - 32) / 1.8
    print(f"The temperatre is {round(result, 1)}°C")
else:
    print(f"{unit} is not a valid unit.")