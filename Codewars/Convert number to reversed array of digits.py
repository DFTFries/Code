# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example (Input => Output):
# 35231 => [1,3,2,5,3]
# 0     => [0]


#_________my solution_________________

def digitize(n):
    n = str(n)
    result = []
    for num in n:
        result.append(int(num))
    return list(reversed(result))

#_________ codewars solution__________

def digitize(n):
    return [int(x) for x in str(n)[::-1]]