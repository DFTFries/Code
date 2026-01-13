# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

#______my solution_______________

def reverse_words(text):
    new_text = text.split(" ")
    reversed_text = [word[::-1] for word in new_text]
    return " ".join(reversed_text)



#________codewars solution________

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

# For those wondering why this solution works event with multiple spaces, I add to read the doc carefully (I used a regex to solve it but this solution is simpler)

# If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2'])

# If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator

# For example:

# print('The     quick  brown fox jumps over the lazy dog.'.split())
# -> ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']

# print('The     quick  brown fox jumps over the lazy dog.'.split(' '))
# -> ['The', '', '', '', '', 'quick', '', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']

print((reverse_words('  double  spaced  words  ')))