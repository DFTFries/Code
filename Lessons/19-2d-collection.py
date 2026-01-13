# fruits =     ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats =      ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]
# groceries = [["apple", "orange", "banana", "coconut"],
            #  ["celery", "carrots", "potatoes"],
            #  ["chicken", "fish", "turkey"]]     #works the same as using varuabke to store lists

# print(groceries[0]) #index prints the corresponding list f.e.: [0] = fruits list - use 2nd index to select specific value in selected list // used like coordinates - row 0, column 0

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7 ,8 ,9),
           ("*", 0, "#"))

for row in num_pad:
    for pad in row:
        print(pad, end=" ")
    print()