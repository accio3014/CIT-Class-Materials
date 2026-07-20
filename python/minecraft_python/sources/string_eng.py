import time     # Import time tools


# time.sleep(number)
# Stops the program for the given number of seconds.
# It is not used very often in real programs.

# print('1')
# time.sleep(1)   # Print 1, then wait for 1 second.
# print('2')
# time.sleep(2)   # Print 2, then wait for 2 seconds.
# print('3')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Strings
# A string is one type of data.
# A data type tells us what kind of value it is.
# Text inside quotation marks is always a string.
# You can use double quotes " " or single quotes ' '.

# name = "jack"
# where = "cit"
# a = '5'         # This is the string "5", not the number 5.

# print(name)
# print(where)
# print(name, where, a)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# input('text' or variable)
# It shows text and waits for the user to type something and press Enter.
# The text or variable can be left out.
# variable = input('text')
# This is the most common way to use input().
# If you use only input(), the entered value is not saved.
# input() always saves the value as a str type.

# name = input()
# print(name)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Adding strings
# You can join strings using the + operator.

# first = "cit"
# second = "academy"

# name1 = "cit" + " " + "academy"
# print(name1)

# name2 = "cit" + " " + second
# print(name2)

# name3 = first + " " + second
# print(name3)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Type casting
# str(variable or value)     -> Changes it to a string.
# float(variable or value)   -> Changes it to a float.
# int(variable or value)     -> Changes it to an integer.
# If you use type casting only in a calculation,
# the original variable does not change.
# To change the original variable's data type,
# save the changed value back into the variable.
# Example: a = int(a)

# one = "1"
# two = "2"
# three = int(one) + int(two)     # The strings in one and two are changed to integers.
# print(three)

# four = 4
# zero = 0
# forty = str(four) + str(zero)   # The numbers in four and zero are changed to strings.
# print(forty)