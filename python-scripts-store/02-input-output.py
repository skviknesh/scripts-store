# Input & Output

# INPUT
# Getting inputs from user: input() function
val = input("Enter your value: ")
print(val)

input1 = input()
print(input1)


# String as input:
name = input('What is your name?\n')	 # \n ---> newline ---> It causes a line break
print(name)


# Program to check input type in Python:
num = input("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)

print ("type of number", type(num))
print ("type of name", type(name1))


# Typecasting: Receive two inputs, convert to int & add:
num1 = int(input())
num2 = int(input())

print(num1 + num2)


# Typecasting: Receive two inputs, convert to float & add:
num1 = float(input())
num2 = float(input())

print(num1 + num2)

# Typecasting: Enter an integer, convert to string:
string = str(input())
print(string, type(string))


# Receiving input twice using split() function:
x, y = input(), input()
print("x=", x, "y=", y)


x, y = input().split()
print("x=", x, "y=", y)
# Output:
# >>>10 20 (Give space to split as default)
# x= 10 y= 20
""" Note that we don’t have to explicitly specify split(‘ ‘) because split() uses whitespace characters as a delimiter 
as default. 
One thing to note in the above Python code is, that both x and y would be of string. 
We can convert them to int using another line."""


# Read two numbers from input and typecasts them to int using list comprehension
x, y = [int(x) for x in input().split()]
print(x, type(x), y, type(y))  # Error

# Read two numbers from input and typecasts them to int using map function
x, y = map(int, input().split())
print(x, type(x), y, type(y))
# Output
# 21 21
# 21 <class 'int'> 21 <class 'int'>


# Python program showing how to multiple input using split
# Taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)


# Taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)


# Taking two inputs at a time
a, b = input("Enter two numbers: ").split()
print("First number is {} and second number is {}".format(a, b))
print(f"First number is {a} and second number is {b}")


# Taking multiple inputs at a time and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
# Output
# Enter multiple values: >? 12 21 12 21 12 21
# List of students:  [12, 21, 12, 21, 12, 21]


# Python program showing how to take multiple input using List comprehension taking two input at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)

# taking three input at a time
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print("Third Number is: ", z)

# taking two inputs at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))

# taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x)


# taking multiple inputs at a time separated by comma
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x)





# Print 3>>2>>1>>Start:
import time
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>')
        time.sleep(1)
    else:
        print('Start')


import time
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end='>>>', flush = True)
        time.sleep(1)
    else:
        print('Start')


# IO:
import io
dummy_file = io.StringIO()
print('Hello Geeks!!', file=dummy_file)
dummy_file.getvalue()


# array
a = [1, 2, 3, 4]

# printing a element in same
# line
for i in range(4):
	print(a[i], end =" ")

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

# 7. Indentation: (# 4 spaces are mandatory which acts like braces)
site = 'gfg'

if site == 'gfg':
    print('Logging on to geeksforgeeks...') # 4 spaces is mandatory
else:
    print('retype the URL.')
print('All set !')