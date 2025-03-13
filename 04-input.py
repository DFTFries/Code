# input() = A function that prompts the user ti enter data
#           Returns the entered data as a string

name = input("What is yor name?: ")
age = int(input("How old are you?: "))

age = age + 1


print(f"Hello {name}")
print("HAPPY BIRTHDAY!")
print(f"Your are {age} years old.")