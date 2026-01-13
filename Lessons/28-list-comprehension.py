# list comprehension = a Concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = []

# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)
#______________________________

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1,11)]
# squares = [z * z for z in range(1, 11)]

# print(squares)
#_____________________________

# fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]] #works as well but less readable than the solution below

# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]

# print(fruits)

#________________________________

# fruits = ["apple", "orange", "banana", "coconut"]
# fruits_chars = [fruit[0] for fruit in fruits]

# print(fruits_chars)

# numbers = [0, 1, -2, 3, -4, 5, -6, -7, 8]
# positive_nums = [num for num in numbers if not num < 0] 
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num %2 == 1]

# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)

#_________________________________

# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_grades = [grade for grade in grades if grade >= 60]

# print(passing_grades)

# students = {
#     "Simon": 85,
#     "Karl": 75,
#     "Pascal": 97,
#     "Tina": 74,
#     "Nico": 35
#     }

# passed = {student for student in students if students.get(student) >= 60}

# print(passed)