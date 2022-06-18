# Break in loops ######################################################################################################
for i in range(10):
    print(i, end=" ")
    # break the loop as soon it sees 6
    if i == 6:
        break
print()

# Continue in loops ####################################################################################################
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
