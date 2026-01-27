# Hangman in Python

import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

# dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\"
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")
}

def display_man(wrong_guesses):
    print("******")
    print()
    for line in hangman_art[wrong_guesses]:
        print(line)
    print()
    print("******")

def guessed_letters(guess):
    guessed_letters = []
    guessed_letters.append(guess)
    return guessed_letters

def display_hints(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_" for letter in answer]
    wrong_guesses = 0
    is_running = True

    while is_running:
        guesses = []
        display_man(wrong_guesses)
        display_hints(hint)
        if len(guesses) > 0:
            print(guesses)
        else:
            pass
        guess = input("Enter a letter: ").lower()
        print(guesses)
        

        if len(guess) != 1:
            print("Invalid input")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            print(f"Wrong guesses: {wrong_guesses}")
            wrong_guesses += 1


        if wrong_guesses == 6:
            display_man(wrong_guesses)
            print("You have lost")
            print(f"The word was {answer}")
            play_again = input("Do you want to keep playing? (y/n)").lower()
            if play_again == "y":
                main()
            else:
                break
        
        if not "_" in hint:
            print(f"You won. The word was {answer}")
            print(f"You made {wrong_guesses} mistakes")
            display_man(wrong_guesses)
            play_again = input("Do you want to keep playing? (y/n)").lower()
            if play_again == "y":
                main()
            else:
                break
        
    
if __name__ == '__main__':
    main()