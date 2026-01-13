# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters.
# Examples:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"

#_________my solution_________________

def get_middle(s):
    num = len(s)
    c = [c for c in s]

    return c[int(num / 2)] if num % 2 == 1 else f"{c[int(num / 2)-1]}{c[int(num / 2)]}"   

#_________ codewars solution__________

def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]

#_____________________________________

def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s