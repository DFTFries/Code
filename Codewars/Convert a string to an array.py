# Write a function to split a string and convert it into an array of words.

# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]

# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

#_________my solution_________________

def string_to_array(s):
    return [''] if not s else s.split()

#_________ codewars solution__________

def string_to_array(string):
    return string.split(" ")