time = int(input("Enter the amount of hours worked total: "))
tip_received = float(input("Enter the amount of tip: "))

tip = tip_received / time

print(f"Everybody receives a tip of {tip:.2f}€ per hour.")
 