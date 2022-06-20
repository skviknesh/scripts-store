# STATEMENTS, PRINT, INDENTATION, COMMENTS & VARIABLE DECLARATIONS:
# \, (), [], {}, ;
# 1. Declared using Continuation Character (\):
s = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(s)


# 2. Declared using parentheses () :
n = (1 * 2 * 3 + 7 + 8 + 9)
print(n)


# 3. Declared using square brackets [] :
footballer = ['MESSI',
              'NEYMAR',
              'SUAREZ']
print(footballer)


# 4. Declared using braces {} :
x = {1 + 2 + 3 + 4 + 5 + 6 +
     7 + 8 + 9}
print(x)


# 5. Declared using semicolons(;) :
flag = 2; ropes = 3; pole = 4
print(flag, ropes, pole)


# 6. Printing Hello world
print("Hello World")


# 7. Indentation: (# 4 spaces are mandatory which acts like braces)
site = 'gfg'

if site == 'gfg':
    print('Logging on to geeksforgeeks...') # 4 spaces is mandatory
else:
    print('retype the URL.')
print('All set !')


# 8. Comments
# This is a comment Print “GeeksforGeeks !” to console
print("GeeksforGeeks")

a, b = 1, 3 # Declaring two integers
sum = a + b # adding two integers
print(sum) # displaying the output


# 9. Multi line string as comments:
"""
This would be a multiline comment in Python that spans several lines and describes geeksforgeeks.
A Computer Science portal for geeks. It contains well written, well thought
and well-explained computer science and programming articles, quizzes and more.
"""
print("GeeksForGeeks")

'''This article on geeksforgeeks gives you a perfect example of
multi-line comments'''
print("GeeksForGeeks")


# 10. Usage of doc strings:
def helloWorld():
    """ This program prints out hello world """ #This is a docstring comment
    print("Hello World")

helloWorld()

# 11. Variable declaration:
myNumber = 3
print(myNumber)

myNumber2 = 4.5
print(myNumber2)

myNumber ="helloworld"
print(myNumber)

num, num2, num7 = 1, 4, 5
print(num, num2, num7)
num = 5; num2 = 4; num7 = 7
print(num, num2, num7)