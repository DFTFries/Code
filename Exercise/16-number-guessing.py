# import random

# low = int(input("Please insert the lowest number: "))
# high = int(input("Please insert the highest number: "))



# # while True:
# #     number = random.randint(low, high)
# #     guess = int(input("Pick a number between 1 and 10: (0 to quit)"))
# #     if guess == "0":
# #         break
# #     elif guess == number:
# #         print("You picked the correct number!")
# #     else:
# #         print("Wrong number.")
# #         print(f"The number was: {number}")
      
# number = random.randint(low, high)
# guesses = 0

# while True:
#     guess = int(input(f"Pick a number between {low} and {high}: (0 to quit)"))
#     guesses += 1

#     if guess == 0:
#         break
#     if guess < low or guess > high:
#         print("That number is out of range")
#         print(f"Pick a number between {low} and {high}")
#     elif guess < number:
#         print("Too low. Try again.")
#     elif guess > number:
#         print("Too high, Try again.")
#     else:
#         print(f"Correct! The answer was: {number}")
#         print(f"Number of guesses: {guesses}")
#         continue


import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low. Try again.")
        elif guess > answer:
            print("Too high, Try again.")
        else:
            print(f"Correct! The answer was: {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    elif guess == "q":
        break
    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")
