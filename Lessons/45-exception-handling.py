# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2.except, 3.finally

# 1 / 0         ZeroDivisionError
# 1 + '1'       TypeError
# int("pizza")  ValueError

"""
try:
    # Try some code

except Exception:
    # Handle an Exception

finally:
    # Do some clean up
"""

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Enter only numbers, please.")
except Exception:                         # catches all exceptions, but is bad practice.
    print("Something went wrong!")        # You're not informing about the cause. Useful as a last resort
finally:
    print("Do some cleanup here.")        # finally-block always executes, regardless if there is an exception or not
