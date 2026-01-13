# Description:
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F

#_________my solution_________________

def abbrev_name(name):
    name = name.split()
    first = [letter[0] for letter in name[0]]
    last = [letter[0] for letter in name[-1]]
    return f"{first[0].upper()}.{last[0].upper()}"

#_________ codewars solution__________

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

#_____________________________________

def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]