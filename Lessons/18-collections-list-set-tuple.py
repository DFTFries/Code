# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates // immutable = unveränderlich
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut"]  # list []
# fruits = {"apple", "orange", "banana", "coconut"}  # set {}
fruits = ("apple", "orange", "banana", "coconut")  # tuple ()

######## common methods ########

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))        # shows the amount of values in the collection
# print("apple" in fruits)  # returns a boolean

# print(fruits[0])          # use [start:end:step] after variable to access specific values // remember -1 in step reverses the order

# for fruit in fruits:      # common to use singular version of the word as counter in for loop - helps with understanding
#     print(fruit)

######## list methods ########
# lists are ordered - meaning the values have a specific order - so you can access them by index

# fruits.append("pineapple")     # adds value to the end of the list
# fruits.remove("apple")         # removes specific value from the list
# fruits.insert(0, "pineapple")  # adds value at specific index
# fruits.sort()                  # sorts the list alphabetically or numerically
# fruits.reverse()               # reverses the order of the list
# fruits.clear()                 # removes all values from the list
# print(fruits.index("apple"))   # returns the index of the specific value

# fruits.append("banana")
# print(fruits.count("banana"))   # returns the index of the first occurrence of the specific value

######## set methods ######## 
# sets are unordered - meaning the values do not have a specific order - so you cannot access them by index

# fruits.add("pineapple")        # adds value to the set
# fruits.remove("apple")         # removes specific value from the set
# fruits.pop()                       # removes a random value from the set
# fruits.clear()                 # removes all values from the set

######## tuple methods ########
# # tuples are immutable - meaning you cannot add or remove values after creation - faster than lists and sets - order is fixed
# print(fruits.index("apple"))     # returns the index of the specific value
# print(fruits.count("coconut"))     # returns the number of occurrences of the specific value

for fruit in fruits:
    print(fruit)



