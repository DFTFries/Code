# membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tiple, set or dictionary)
#                        1. in
#                        2. not in

#________String___________

# word = "APPLE"
# letter = input("Guess a letter in the secret word: ").upper()

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

#________List, Tuple, Set_____________

# students = {"Spongebob", "Patrick", "Sandy"}

# student = input("Enter the name of a student: ").capitalize()

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")

#_________Dictionary_________________

# grades = {
#     "Sandy": "A", 
#     "Squidward": "B", 
#     "Spongebob": "C", 
#     "Patrick": "D"
# }
# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

# ___________example__________________

email = "testmail@gmail.com"

if "@" in email and "." in email:
    print(f"{email} is vaild")
else:
    print(f"{email} is not valid")