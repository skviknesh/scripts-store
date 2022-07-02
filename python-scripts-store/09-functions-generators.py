# FUNCTIONS & GENERATORS:
# SYNTAX 1:
# def function_name(parameters):
#     """docstring"""
#     <body of the function>
#     return expression

# Example for syntax 1:
# def <function_name>([<parameters>]):
#     <statement(s)>

# SYNTAX 2:
# def function_name(parameter: data_type) -> return_type:
#     """Docstring"""
#     <body of the function>
#     return expression

# Simple function 1: ##################################################################################################

def hello():
    print("hello")
    print("hello again")


hello()  # calling the hello() function


# Simple function 2: ##################################################################################################
def f():
    s = '-- Inside f()'
    print(s)


print('Before calling f()')
f()
print('After calling f()')


# Empty function: ####################################################################################################
def f():
    pass


f()


# Positional Arguments: ###############################################################################################
def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')


f(6, 'bananas', 1.74)
f('bananas', 6, 1.74)  # Positions will get changed


# Keyword Arguments: ###############################################################################################
# Using keyword arguments lifts the restriction on argument order, so you can specify them in any order.

def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')


f(qty=6, item='bananas', price=1.74)
f(item='bananas', qty=6, price=1.74)  # Keyword arguments won't get changed
f(price=1.74, qty=6, item='bananas')  # Keyword arguments won't get changed


# Default Parameters: ###############################################################################################
# If a parameter specified in a Python function definition has the form <name>=<value>,
# then <value> becomes a default value for that parameter

def f(qty=6, item='bananas', price=1.74):  # qty=6, item=bananas, price=1.74 will be default values
    print(f'{qty} {item} cost ${price:.2f}')


f(4, 'apples', 2.24)  # Parameter values are overwritten with what we passed.
f(4, 'apples')        # Parameter values are overwritten only for 4 & apples.
f(4)                  # Parameter values are overwritten for 4.
f()                   # Default parameters are taken
f(item='kumquats', qty=9)  # Default parameters are overwritten here for item & qty.
f(price=2.29)              # Default parameters are overwritten only for price.


# Mutable default value parameters: ###################################################################################

def f(my_list=[]):
    my_list.append('###')
    return my_list


f([1, 2, 3, 4, 5])

f()
f()
f()
# Oops! You might have expected each subsequent call to also return the singleton list ['###'],
# just like the first. Instead, the return value keeps growing. What happened?

# In Python, default parameter values are defined only once when the function is defined
# (that is, when the def statement is executed).
# The default value isn’t re-defined each time the function is called.
# Thus, each time you call f() without a parameter, you’re performing .append() on the same list.


# To understand this better, we can check this with object id (address) with id() function: ###########################
def f(my_list=[]):
    print(id(my_list))
    my_list.append('###')
    return my_list


f([1, 2, 3, 4, 5])

f()
f()
f()
# The object identifier displayed confirms that, when my_list is allowed to default,
# the value is the same object with each call.


# Functions 02: Return keyword ########################################################################################
def fun():
    s = 0
    for i in range(10):
        s += i
    return s


print(fun())


# Another way of mentioning datatypes in function calls: ##############################################################
def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3


# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
type(num1), type(num2), type(ans)  # (<class 'int'>, <class 'int'>, <class 'int'>)


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