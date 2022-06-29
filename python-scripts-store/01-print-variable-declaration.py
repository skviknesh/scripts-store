# PRINT, VARIABLE DECLARATIONS & PRINT FORMATTING:
# 1. OUTPUT:
# Python Output functions
# Syntax: print(value(s), sep= ‘ ‘, end = ‘\n’, file = file, flush = flush)

# "print" function ####################################################################################################

print("Hello World")
print("My name is Viknesh")


# "end" parameter - the output with a <space at end by default> #######################################################

print("Welcome to", end=' ')
print("Python", end=' ')

print("Python", end='@')
print("is really awesome")

print("It is great to learn programming in a structured way", end="**")
print("Welcome to learning")


# "sep" parameter - separates the string in commas ####################################################################

print('26', '03', '1992', sep='-')

print('Red', 'Green', 'Blue', sep=',')

print("Hello my name is Viknesh", sep=',')  # has no change
print("Hello", "my", "name", "is", "Viknesh", sep=',')
print("Hello", "my", "name", "is", "Viknesh", sep='-')

print('I', 'am', sep='', end='')
print('Viknesh')

print('I', 'am', 'creating', sep=',', end='@')
print('Python Scripts')


# \n - for new line ###################################################################################################

print("Python is very famous in all aspects")
print("Python \n is very famous in all aspects.")

print('26', '03', '1992', sep='-', end='\n')


# 2. VARIABLE DECLARATIONS: ############################################################################################

myNumber = 3
print(myNumber)

myNumber2 = 4.5
print(myNumber2)

myNumber = "helloworld"
print(myNumber)

num, num2, num7 = 1, 4, 5
print(num, num2, num7)

num = 5; num2 = 4; num7 = 7
print(num, num2, num7)


# \, (), [], {}, ;
# Declared using Continuation Character (\): ##########################################################################

s = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(s)


# Declared using parentheses (): ##################################################################################

n = (1 * 2 * 3 + 7 + 8 + 9)
print(n)


# Declared using square brackets []: ##############################################################################

footballer = ['MESSI',
              'NEYMAR',
              'SUAREZ']
print(footballer)


# Declared using braces {}: #######################################################################################

x = {1 + 2 + 3 + 4 + 5 + 6 +
     7 + 8 + 9}
print(x)


# Declared using semicolons(;): ####################################################################################

flag = 2; ropes = 3; pole = 4
print(flag, ropes, pole)


# Printing objects ##################################################################################################

x = 5
print("x =", x)

b = "Viknesh"
print("Hello", b, "How are you")

a, b = 1, 3  # Declaring two integers
add = a + b  # adding two integers
print(add)  # displaying the output


# 3. PRINT FORMATTING: ################################################################################################

# \" \"

print("I \"love you")
print("I \"love\" you")


# using ".format()" method ###########################################################################################

print("I love {} for your {}!".format('You', 'Kindness'))

# Referring a position of the object
print('{0} and {1}'.format('Love', 'Kindness'))
print('{1} and {0}'.format('Love', 'Kindness'))

print("I love {0} for your \"{1}!\"".format('You', 'Kindness'))

print("I prefer to have {0} with {1}, and {other}.".format('Tea', 'Sugar', other='Biscuits'))

print("Runs :{0:2d}, Run rate :{1:8.2f}".format(12, 00.546))

# "f-Strings", similar to ".format()" #################################################################################

print(f"I love {'you'} for your {'Kindness'}!")

print(f"I love {'you'} for your \"{'Kindness'}!\"")


# STRING FORMATTING ###################################################################################################
# d, i, u - Decimal integer;               x, X - Hexadecimal integer;         o - Octal integer;
# f, F - Floating-point;                   e, E - E notation;                  g, G - Floating-point or E notation;
# c - Single character;                    s, r, a - String;                   % - Single '%' character

print("Hello, my name is %s." % "Viknesh")

print("%d %s cost $%.2f" % (6, "bananas", 1.74))   # Multiple values enclosed in a tuple.

"%d, %i, %u" % (42, 42, 42)

"%5s" % "foo"

"%3d" % 4
