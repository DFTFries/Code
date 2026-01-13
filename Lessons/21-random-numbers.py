import random

# print(help(random))

# number = random.randint(1, 6)
low = 1
high = 100
options = ("Rock", "Paper", "Scissor")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# number= random.randint(low, high)
# number = random.random() picks a random float number between 0 and 1
# result = random.choice(options)
random.shuffle(cards) #shuffles the list

print(cards)
