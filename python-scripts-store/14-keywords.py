# Python code to demonstrate working of iskeyword() ####################################################################
# 1. importing "keyword" for keyword operations
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

# 2. Example: True, False, and None Keyword ############################################################################
print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])
'''None: This is a special constant used to denote a null value or a void. 
It’s important to remember, 0, any empty container(e.g empty list) does not compute to None. 
It is an object of its datatype – NoneType. 
It is not possible to create multiple None objects and can assign them to variables.'''

# 3. Example: and, or, not, is and in keyword ##########################################################################
print(True or False) # Showing logical operation or (returns True)
print(False and True) # showing logical operation and (returns False)
print(not True) # showing logical operation not (returns False)

# using "in" to check
if 's' in 'geeksforgeeks':
    print("s is part of geeksforgeeks")
else:
    print("s is not part of geeksforgeeks")

# using "in" to loop through
for i in 'geeksforgeeks':
    print(i, end=" ")

print("\r")

# using is to check object identity string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print(' ' is ' ')

# using is to check object identity dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({} is {})


