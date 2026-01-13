# Beginner - Lost Without a Map

# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

#________my solution_________

def maps(a):
    a = [c*2 for c in a]
    return a

#________codewars one liner________

def maps(a):
    return [2 * x for x in a]