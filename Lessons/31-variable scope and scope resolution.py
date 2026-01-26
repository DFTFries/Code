# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# def func1(): #variable a and b are local and cannot be accessed by the other function
#     a = 1
#     print(a)

# def func2():
#     b = 2
#     print(b)

# func1()
# func2()

# def func1():
#     x = 1
#     def func2():    #since func2() is enclosed in func1() it can access the variable x
#         print(x)
#     func2()

# func1()

# x = 1               # in this case the variable x is global and can be accessed by every function
#                     # if there is no local or enclosed variable it will access the global 
# def func1():
#     x = 3           # local variables have a higher priority than global variables
#     print(x)

# def func2():
#     print(x)

# func1()
# func2()

from math import e

def func1():
    print(e)

e = 3          #global variables have a higher priority tham built-in

func1()



