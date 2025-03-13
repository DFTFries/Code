# Variable = A container for a value (string,  integer, float, boolean)
#            A Variable behave as if it was the value it contains


# string
# everything between "" is a string

first_name = "Jan"
food = "pizza"
email = "jan@pizza.com"

print(f"Hello, {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers
# be sure numbers are not inside ""

age = 34
quantity = 3
num_of_students = 30

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {num_of_students} students.")

# float
 
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} km.")

# boolean

is_student = True
for_sale = False
is_online = True

if is_student:
    print("Your are a student")
else:
    print("You are NOT a student!")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available.")
if is_online:
    print("You are online.")
else:
    print("You are offline.")
