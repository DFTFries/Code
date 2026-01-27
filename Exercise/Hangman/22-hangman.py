# Hangman in Python

from wordslist import words
import random

# words = ("apple", "orange", "banana", "coconut", "pineapple")

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
                   "/|\\",
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

def display_hints(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_" for letter in answer]
    guessed_letters = []
    wrong_guesses = 0
    is_running = True

    while is_running:
        
        display_man(wrong_guesses)
        display_hints(hint)
        print()
        print("*********")
        print("Guessed letters: " + ", ".join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print("**********************************")
            print(f"You already tried the letter {guess}")
            print("**********************************")
            continue

        guessed_letters.append(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"Wrong guesses: {wrong_guesses}")


        if wrong_guesses >= 6:
            display_man(wrong_guesses)
            print("You have lost")
            print(f"The word was {answer}")
            play_again = input("Do you want to keep playing? (y/n)").lower()
            if play_again == "y":
                main()
            else:
                break
        
        if "_" not in hint:
            print(f"You won. The word was {answer}")
            print(f"You made {wrong_guesses} mistakes")
            display_man(wrong_guesses)
            play_again = input("Do you want to keep playing? (y/n)").lower()
            if play_again == "y":
                main()
            else:
                break
    guessed_letters.clear()
    
if __name__ == '__main__':
    main()