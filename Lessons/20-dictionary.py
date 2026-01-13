# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.", 
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")
# capitals.update({"Germany": "Berlin"})
# capitals.pop("China")
# capitals.popitem()   removes tha latest key:value pair that was inserted
# capitals.clear()

# keys = capitals.keys()         use .keys() to get the keys
# for key in capitals.keys():     use it in for loop to iterate through the keys
#     print(key)

# values = capitals.values()
# for value in capitals.values():   # .value() in for loop to iterate through all values
#     print(value)

# items = capitals.items() # .items() returns a dictionary object, that resembles a 2D list of tuples
for key, value in capitals.items():
    print(f"{key}: {value}")
