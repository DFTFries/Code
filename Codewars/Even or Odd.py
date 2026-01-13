# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


#_________my solution_________________

def even_or_odd(number):
    solution = number % 2
    if solution == 0:
        return "Even"
    else:
        return "Odd"

#_________ codewars solution__________

def even_or_odd(number):
	return 'Odd' if number % 2 else 'Even'