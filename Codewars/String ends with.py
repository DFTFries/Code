# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# Inputs: "abc", "bc"
# Output: true

# Inputs: "abc", "d"
# Output: false

#______my solution_________

def solution(text, ending):
    x = len(ending)
    return ending in text[-x:]

#_______codewars solution__________ string.endswith()

def solution(string, ending):
    return string.endswith(ending)

#_________________________________one liner of my solution

def solution(string, ending):
    return ending in string[-len(ending):]

