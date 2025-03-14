# for loops = execute a blok of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc

# for x in reversed(range(1, 11)):    #second number is exclusive, if you want to count to 10 use 11 // range(start, end, step)
#     print(x)

# print("HAPPY NEW YEAR!")


# --------------------

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# ---------------------

for x in range(1, 21):
    if x == 13:
        continue   # continue can be used to skip an iteration
    else:
        print(x)