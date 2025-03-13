import math

a = float(input("Enter side A in cm: "))
b = float(input("Enter side B in cm: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C is: {round(c, 2)}cm")