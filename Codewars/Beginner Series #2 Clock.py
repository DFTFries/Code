# Clock shows h hours, m minutes and s seconds after midnight.

# Your task is to write a function which returns the time since midnight in milliseconds.

# Example:
# h = 0
# m = 1
# s = 1

# result = 61000
# Input constraints:

# 0 <= h <= 23
# 0 <= m <= 59
# 0 <= s <= 59


#_________my solution_________________

def past(h, m, s):
    hour = h * 3600000
    minute = m * 60000
    seconds = s * 1000
    return hour + minute + seconds

#_________ codewars solution__________

def past(h, m, s):
    return (3600*h + 60*m + s) * 1000

#_____________________________________

def past(h, m, s):
    if 0 <= h <= 23 or 0 <= m <= 59 or 0 <= s <= 59:
        x = h * 3600000
        y = m * 60000
        z = s * 1000
        total = x + y + z
        return(total)
    else:
        return("Please input an hour between 0 and 23 and a minute or second inbetween 0 and 59.")