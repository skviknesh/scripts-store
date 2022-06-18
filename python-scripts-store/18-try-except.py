# initializing number
a, b = 4, 0
try:
    k = a//b # raises divide by zero exception.
    print(k)
except ZeroDivisionError: # handles zero division exception
    print("Can't divide by zero")
finally:
    print('This is always executed') # this block is always executed regardless of exception generation.

