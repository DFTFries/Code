# Python weight converter

weight = float(input("Enter the weight you want to convert: "))
unit = input("Enter the type you want to convert to (kg / lb): ")

if unit.lower() == "kg":
    result = weight / 2.205
    print(f"The weight is {round(result, 2)}kg")
elif unit.lower() == "lb":
    result = weight * 2.205
    print(f"the weight is {round(result, 2)}lb")
else:
    print(f"{unit} is not a valid unit.")