
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []
# You can assume that all values are integers. Do not mutate the input array.

#________my solution__________

def invert(lst):
    c = 0
    new_lst=[n for n in lst]
    for n in new_lst:
        if n > 0:
            new_lst[c] = n - n - n
        elif n < 0:
            new_lst[c] = n + n * -2
        c += 1
        
    return new_lst

#_______codewars solutions_____________

def invert(lst):
    return [-x for x in lst]

