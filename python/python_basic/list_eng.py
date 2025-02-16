# list_eng.py

# variable = ["value", value]       => The data type of the value does not matter
# Use in the above form
# List is a collection of multiple data types in order in one variable.
# The order of values starts from 0 => It is called the index number.
# When bringing in list values, refer to them using []

# list1 = [1, 'cit', True]
# print(list1)
# print(list1[0])     # Get list1 index number 0 value.
# print(list1[2])
# print(list1[3])     # Get list1 index number 3 value. There is index number 3, so an error occurs


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# You can use the index number to modify the value at that index number.
# Changing the value can be done as if saving the value in a variable.
# a = [1, 'cit', True]
# print(a)

# a[1] = "hello"  # Change the value of the index number 1 of a.
# print(a)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# list1 = ["abc", "dfg", "hij", 123, 456 ]
# print(list1)
# print()

# print("Q1. Change the 1st element of list1 to 'park'.")
# list1[1] = 'park'
# print(list1)
# print()




# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# for i in range(1, 9, 2):
#     print(i)
# print()

# list1 = [1, 3, 5, 7]
# for i in list1:         # Can insert a list variable instead of range() in for loop.
#     print(i)            # Get the elements of a list one by one
# print()

# list2 = ['a', 'hello', 'cit', 'coding', 'A']
# for j in list2 :
#     print(j)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# score = [92, 96, 98, 100]
# avg = 0
# for i in score :
#     avg = avg + i
# print(avg / 4)


# avg = 0
# for i in range(4) :
#     avg = avg + score[i]
# print(avg / 4)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# List function

# listName.insert(Index number, Value to add)
# insert() add one value to index number. If there is a value that index, the values are pushed back.
# If index number is out of range, the value is insert to the end.

# listName.append(Value to add)
# appened() add one value append to the end.

# del(listName[Index number])
# In the case of del(), the value at the index number of the list deleted, 
# and if there is an index number after it, it is pulled forward.
# If index number is out of range, an error occurs.

# listName.remove(Value to remove)
# In the case of remove(), the value to be deleted is found in the list and deleted.
# If there is an index number after it, it is pulled forward.
# If the value to be deleted is not in the list, an error occurs.

# listName.index(Value to find index)
# In the case of index(), the index number where the value is located is returned.
# If the value to find is not in the list, an error occurs.
# If there are multiple values in the list, the number with the lowest index is returned.

# len(listName)
# In the case of len(), the length of the listName is returned.
# (It is different from the index, the last number of the index is the value -1 of len(listName))

# sum(listName)
# In the case of sum(), it returns after adding all the values in the listName. 
# (Available only when the list data types are numeric.)
# If the data types in the list are mixed with str and numbers, an error occurs

# listName.count(Value to counter)
# In the case of count(), it returns how many values are in the list.
# 0 if the value to be counted is not in list.

# listName.sort()
# Sort the contents of the list in ascending order.

# Functions like insert() that are used with a list variable followed by a dot(.) can only be used with lists.
# Functions like del(), len(), and sum() can be used with other data types as well, not just lists.


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# score = [92, 96, 98, 100]

# avg = sum(score) / len(score)
# print(avg)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# in
# in is used to check if a value exists in a list, returning True or False.
# This result can be applied within conditional statements like 'if'.
# It's used in the following format:
# value_to_find in list_name

# numbers = [1,2,3,4,5]
# print(2 in numbers)
# print(8 in numbers)

# if(3 in numbers) :
#     print("3 inside the list")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Double Lists (2D Lists)
# When there's a list inside another list,
# use double square brackets [][] to reference values.

# list1 = [1, 'cit', True]
# list2 = [3, 2, 'py']
# list3 = [list1, list2]

# print(list1)
# print(list2)
# print(list3)
# print(list3[0][1])
# print(list3[1][1])
# print(list3[0])
# print()

# for i in range(len(list3)) :
#     for j in range(len(list3[0])) : 
#         print(list3[i][j])


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Triple Lists (3D Lists)
# When there's a list inside another list inside another list,
# use triple square brackets([][][]) to reference values.


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Cafe = ['Starlucks', 'Mollys', 'Emiya', 'FomAFams']
# Main = ['Americano', 'Cappuccino', 'Cafelatte', 'Americano']
# Price = [3700, 4600, 3200, 4100]
# Location = ['A Street', 'B Street', 'C Street', 'D Street']
# CafeTable = [Cafe, Main, Price, Location]
# print(CafeTable)
# print()

# Viewing the content of nested lists line by line
# for i in CafeTable:
#     print(i)
# print()

# Printing only the price information
# print(CafeTable[2])
# print()

# Printing only the information for Mollys
# for i in range(len(CafeTable)):
#     print(CafeTable[i][1], end=' ')
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# A = [1, 4, 5]
# B = [2, 3, 6]
# C = []

# Case 1 : using value
# for i in A :
#    for j in B :
#       C.append(i*j)

# for z in C :
#    print(z)
# print()

# C = []
# Case 2 : using index
# for i in range(len(A) ):
#    for j in range(len(B)) :
#         C.append(A[i] * B[j])

# for z in C :
#    print(z)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Combining Lists
# You can combine lists using the + symbol 
# (but for nested lists, they must have the same nesting level).
# a = [1, 2, 3]
# b = [2, 3, 4]
# c = a + b
# print(c)