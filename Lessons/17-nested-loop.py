# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# examples

# while loop in while loop

# while x > 0:
#     while y > 0:
#         print("do something")

# for loop in for loop

# for x in range(3):
#     for y in range(9):
#         print("do something")

# for loop in while loop

# while x > 0:
#     for y in range(9):
#         print("do something")

# while loop in for loop

# for x in range(3):
#     while y > 0:
#         print("do something")



#for x in range(3):          #range(start, end) remember end is exclusive: e.g. 10 ends at 9
#    for y in range(1, 10):
#        print(y, end="")            #use end="" to print everything in one line user symbols or space in "" to seperate between te printed stuff
#    print()                         #empty print will print an empty line, hence inner loop isn't all on the same line


rows = int(input("How many rows shall the rectangle have: "))
columns = int(input("How many columns shall the rectangle have: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()