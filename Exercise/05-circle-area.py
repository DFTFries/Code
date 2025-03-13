import math

radius = float(input("Enter the radius of the circle in cm: "))
result = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(result, 2)}cm²")