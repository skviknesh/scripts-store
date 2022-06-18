"""Scope of a variable/ object:
Scope refers to the coding region from which a particular Python object is accessible.
Hence, one cannot access any particular object from anywhere from the code,
the accessing has to be allowed by the scope of the object.
Let’s take an example to have a detailed understanding of the same: """

# Scope of a variable: Example 1 ######################################################################################
var1 = 5                # var1 is in the global namespace
def some_func():
    var2 = 6               #var2 is in the local namespace
    def some_inner_func():      # var3 is in the nested local namespace
        var3 = 7

# Python program processing global variable ###########################################################################
count = 5
def some_method1():
    global count
    count = count + 1
    print(count)
some_method1()

# Python program showing a scope of object: ###########################################################################
def some_func2():
    print("Inside some_func")
    def some_inner_func2():
        var = 10
        print("Inside inner function, value of var:", var)
    some_inner_func2()

    print("Try printing var from outer function: ", var) # This will create error as this var is defined inside.
some_func2()
