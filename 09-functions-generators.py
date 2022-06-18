# Functions 01: ######################################################################################################
def hello():
    print("hello")
    print("hello again")

# calling function
hello()

# Functions 02: Return keyword ########################################################################################
def fun():
    s = 0
    for i in range(10):
        s += i
    return s
print(fun())

# Generators - Yield Keyword ###########################################################################################
# Example 1:
def numberGenerator(n):
    number = 0
    while number < n:
        yield number
        number += 1

myGenerator = numberGenerator(3) # sets n = 3
print(next(myGenerator)) # iteration 1: n = 3, number = 0 | So yields number 0 & increments number to 1
print(next(myGenerator)) # iteration 2: n = 3, number = 1 | So yields number 1 & increments number to 2
print(next(myGenerator)) # iteration 2: n = 3, number = 2 | So yields number 2 & increments number to 3

# Example 2:
def numberGenerator(n):
    number = 0
    while number < n:
        yield number
        number += 1

g = numberGenerator(10) # For 10 times yields number.

counter = 0
while counter < 10:
    print(next(g)) # For 0-9 times calls numberGenerator()
    counter += 1