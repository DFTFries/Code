# module = a file containing code you want to include in your program
#          use "import" to include a module (built-in or you own)
#          useful to break a large program into reusable seperate files

# print(help("modules"))

# import math 
# print(math.pi)

# import math as m
# print(m.pi)

# from math import pi
# print(pi)

from math import e            #importing specific variables can cause conflicts in your code
a, b, c, d, e = 1, 2, 3, 4, 5 #since we're reassigning a value to e, the import becomes obsolete
print(e ** a)
print(e ** b)
print(e ** c)
print(e ** d)
print(e ** e) 

#____________________________________

import math           
a, b, c, d, e = 1, 2, 3, 4, 5 
print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e) 



