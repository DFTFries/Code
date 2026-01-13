# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.


#_________my solution_________________

def get_count(sentence):
    letters = []
    for letter in sentence:
        letters.append(letter)
    vowels = letters.count("a") + letters.count("e") + letters.count("i") + letters.count("o") + letters.count("u")
    return vowels

#_________ codewars solution__________

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

#_____________________________________

def getCount(s):
    return sum(c in 'aeiou' for c in s)