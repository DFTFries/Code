# Write a function which calculates the average of the numbers in a given array.

# Note: Empty arrays should return 0.


#_________my solution_________________

def find_average(numbers):
    return 0 if not numbers else sum(numbers)/len(numbers)

#_________ codewars solution__________

def find_average(array):
    return sum(array) / len(array) if array else 0

#_____________________________________

def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0