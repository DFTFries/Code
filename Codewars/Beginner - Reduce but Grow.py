# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24


#_________my solution_________________

def grow(arr):
    start = 1
    for num in arr:
        start = start * num
    return start
        

#_________ codewars solution__________

def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product

#______________________________________

