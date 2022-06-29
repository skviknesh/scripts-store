# Iterator - Loops:

# SYNTAX:
# for <variable> in <iterable>:
#     <statements>

# Sample
for step in range(5):
    print(step)


# Iterating over a list ###############################################################################################

print("List Iteration")
l = ["Viknesh", "is", "funny"]
for i in l:
    print(i)


# Iterating over a tuple (immutable) ##################################################################################

print("\nTuple Iteration")
t = ("viknesh", "is", "funny")
for i in t:
    print(i)


# Iterating over a String #############################################################################################

print("\nString Iteration")
s = "Viknesh"
for i in s:
    print(i)


# Iterating over dictionary ###########################################################################################

print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" %(i, d[i]))


# Continue in Loops - 1. Print: all letters except 'k' and 's' ########################################################

for letter in 'Viknesh':
    if letter == 'k' or letter == 's':
        continue

    print('Current Letter :', letter)


# Continue in Loops - 2 ###############################################################################################

i = 0
while i < 10:
    # If i  equals to 6, continue to next iteration without printing
    if i == 6:
        i += 1
        continue
    else:
        # otherwise print the value of i
        print(i, end=" ")
    i += 1


# Break in Loops: 1 ###################################################################################################

for letter in 'Viknesh':
    # break the loop as soon it sees 'k' or 's'
    if letter == 'k' or letter == 's':
        break

print('Current Letter :', letter)


# Break in Loops: 2 ###################################################################################################

for i in range(10):
    print(i, end=" ")
    # break the loop as soon it sees 6
    if i == 6:
        break


# Pass keyword/statement in Loops: An empty loop ######################################################################

for letter in 'viknesh':
    pass
print('Last Letter :', letter)


# Python Program to show range() basics printing a number #############################################################

x = range(0, 10)  # x is created as an object, to view it, enclose it in tuple/list.
print(tuple(x))
print(list(x))

for i in range(10):
    print(i, end=" ")


# using range for iteration ###########################################################################################

l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end=" ")


# performing sum of first 10 numbers ##################################################################################

add = 0
for i in range(1, 10):
    add = add + i
print("Sum of first 10 numbers :", add)


# Python program to demonstrate for-else loop #########################################################################

for i in range(1, 4):
    print(i)
else: # Executed because no break in for
    print("No Break\n")


for i in range(1, 4):
    print(i)
    break
else: # Not executed as there is a break in for loop.
    print("No Break")


# LOOPS: Multiple Variables ###########################################################################################
# https://www.delftstack.com/howto/python/python-for-loop-multiple-variables/

# 1. Use the for Loop for Multiple Assignments in a Dictionary in Python ##############################################

dict1 = {1: "Bitcoin", 2: "Ethereum"}
for key, value in dict1.items():
    print(f"Key {key} has value {value}")
    # dict1_items() has values dict_items([(1, 'Bitcoin'), (2, 'Ethereum')])
    # It comes in pairs (key, value) for each (one) iteration
print(dict1.items())


# 2. Use enumerate() Function for Multiple Assignments in a List in Python ############################################

coins = ["Bitcoin", "Ethereum", "Cardano"]
prices = [48000, 2585, 2]
for i, coin in enumerate(coins):
    price = prices[i]
    print(f"${price} for 1 {coin}")
    # enumerate(coins) creates values ((0, 'Bitcoin'), (1, 'Ethereum'), (2, 'Cardano'))
    # It comes in pairs (index, value) for each (one) iteration


# 3. Use the zip() Function for Multiple Assignments in a Tuple or a List in Python ###################################
coins = ["Bitcoin", "Ethereum", "Cardano"]
prices = [48000, 2585, 2]
for coin, price in zip(coins, prices):
    print(f"${price} for 1 {coin}")
    # zip(coins, prices) create values (('Bitcoin', 48000), ('Ethereum', 2585), ('Cardano', 2))
    # It comes in pairs (value-list1, value-list2) for each (one) iteration.

# Next refer this website: https://www.dataquest.io/blog/tutorial-advanced-for-loops-python-pandas/
