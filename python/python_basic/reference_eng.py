# reference_eng.py

# 1. String Formatting
# 2. Escape Codes
# 3. Ignoring Line Breaks


# [1. String Formatting]

# String Formatting    => Use formatting symbols inside quotes to represent variables in a string.
# Why use string formatting: When printing multiple variables and strings together, using commas can 
# result in unintended spaces. Formatting allows precise placement of variable values within the string.

# Example: To print "Hello CIT"
# a = "Hello"
# b = "CIT"
# print(a, b)                 # Using a comma adds an unwanted space between the variables.
#                             # Using commas also limits the number of variables that can be printed.
# print("%s %s" % (a, b))     # Formatting places variable values exactly where desired, making customization easier.

# Formatting symbols   => Place inside quotes
# String (str)         => %s
# Float (float)        => %f
# Integer (int)        => %d
# Use the formatting symbol that matches the variable type.

# 1. To print a single variable:
# print("%f" % (variable))                  The value of variable is placed where %f is.
# 2. To print multiple variables:
# print("%f %s" % (varA, varB))             The value of varA is placed where %f is, 
                                            # and the value of varB is placed where %s is.

# Example: To print "My name is Park! And my age is 15."
# name = "Park"   # Use %s for string
# print("My name is %s! And my age is 15." % (name))

# i = "My"        # Use %s for string
# print("%s name is %s! And my age is 15." % (i, name))

# age = 15        # Use %d for integer
# print("%s name is %s! And my age is %d." % (i, name, age))

# print("%d %d" % (age, age)) # Formatting allows the same variable to be used multiple times.

# Formatting for decimal places
# Use %f for floats
# By default, %f prints 6 decimal places. Specifically, it rounds at the 7th place and displays up to the 6th place.
# pi = 3.1415
# print("%f" % (pi))  # If the variable has fewer than 6 decimal places, the remaining places are filled with 0s.

# %.numberf       => Print up to 'number' decimal places. Specifically, round at the (number+1) place.
# print("%.3f" % (pi))    # Rounds at the 4th place and prints up to the 3rd place.

# Formatting can also be used to align strings.
# 100000
#  10000
#   1000
# To print the above:
# a = 100000
# b = 10000
# c = 1000
# print("%7d" % a)
# print("%7d" % b)
# print("%7d" % c)

# Insert a number between % and d to specify the width of the space.
# %7d   => Print the value right-aligned within a 7-character space.
# %-7d  => Print the value left-aligned within a 7-character space.
# If the value is wider than 7 characters, it will be printed normally.
# c = 1000
# print('%7d' % c)
# print('%-7dhi' % c)

# This alignment works with %s, %d, and %f.
# Special case for %f:
# To print up to 3 decimal places: %.3f
# Specifically, round at the 4th place and print up to the 3rd place.
# pi = 3.14159265
# print('%5.3f' % pi)      # Prints 3.142 because the 4th place value (5) causes rounding.


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# [2. Escape Codes]
# Special characters used in strings to perform certain actions.
# \n    Inserts a newline.
# \t    Inserts a tab space.
# \\    Prints a backslash (\).
# \'    Prints a single quote (').
# \"    Prints a double quote (").
# print("Hello\nCIT")     # \n used to insert a newline.
# print("Hello\tCIT")     # \t used to insert a tab space.
# print("Hello\\CIT")     # \\ used to print a backslash.
# print("\' \"")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# [3. Ignoring Line Breaks]
# By default, print() adds a newline at the end.
# To avoid this, use print() with ,end=''.
# The exact meaning of ,end='character' is to print the content without adding a newline and then append the character.
# Usually, an empty string is used.
# for i in range(5):
#     print('%d ' % i, end='')    # Prints the results in a single line.
# print()

# for i in range(5):
#     print('%d ' % i)    # Prints the results, each on a new line.
# print()
