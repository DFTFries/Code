# Python compound interest calculator

principle = 0
rate = 0 
time = 0

# final = balance * pow((1 + rate / math.n), period)

# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle can't be less than zero")

# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate can't be less zero")

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("Time can't be less zero")

# Either do a condition 
# while principle <= 0:
# or
# while True:   // <--- infinite loop until explicitly breaking out of the loop using break

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less zero")
    else:
        break

total = principle * pow((1 + rate / 100 ), time)
print(f"Balance after {time} year/s: €{total:.2f}")