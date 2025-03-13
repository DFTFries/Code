# Exercise 2 Shopping cart program

item = str(input("What item would you like to buy?: "))
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the amount of the item you are buying: "))
bill = quantity * price

print(f"You are buying {quantity}x {item}/s for a total of €{bill:.2f}")