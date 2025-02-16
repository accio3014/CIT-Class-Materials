# variable
# variable = value
# Save the value in variable in the format above.
# = Unlike the meaning of the symbol, the value is simply stored in a variable.
# Variable can be whatever you want as long as you follow the rules below.
# 1. Impossible to start with a number
# 2. Special characters are not possible except the symbol “_”
# 3. No spacing
# 4. Reserved words not possible

# my_name = "Jeong"


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Data types
# str   -> String       => made up of quotes " "  ' '
# float -> Float        => no quotes and has a decimal point
# int   -> Integer      => no quotes and no decimal point
# Everyday words (English, Chinese, Korean, etc.) without quotes => error

# a = 10      # saves the integer 10 in the variable a
# b = 'cit'   # saves the string 'cit' in the variable b

# name = 'Python'
# age = 20
# height = 178

# print(name)

# name = 'Pong'
# print(name)

# name = 'Go!'
# print(name)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print('text' or variable or number)
# The print() function prints the 'text', number, or value of 
# the variable inside the bracket and then adds a newline.
# To print multiple items, use a comma (,)
# If you use print() with nothing inside, it prints an empty line

# name = 'Python'
# age = 28
# height = 188
# print(name)
# print()         # prints an empty line
# print(age)
# print(height)
# print('hi')
# print()
# print(5)
# print(5*10)
# print(name, age, height, "hello")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# How to check the data type
# type() => gets the data type of the variable or value inside the parentheses
# type(variable)        <= this works, but you can't see the data type
# print(type(variable))
# Usually used inside print() to see the data type

# int0 = 1                # saves the integer 1 in the variable int0
# float0 = 3.14
# str0 = 'test'
# type(int0)              # this works, but you can't see the data type
# print(type(int0))       # prints the data type of int0 using type()
# print(type(float0))
# print(type(str0))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Type casting
# str(variable or value)     => converts variable or value to str data type
# float(variable or value)   => converts variable or value to float data type
# int(variable or value)     => converts variable or value to int data type
# Just using them in calculations doesn't change the original variable's data type
# To change the original variable's data type, save it back into the variable [ ex. a = int(a) ]

# var1 = 2
# var2 = '31'
# result = var1 + int(var2)   # saves var1 + var2 converted to int in result
# print(result)
# print(type(var2))           # prints the data type of var2, which is still str
# var2 = int(var2)            # converts var2 to int and saves it back in var2
# print(type(var2))           # prints the new data type of var2


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# input('text' or value or variable)
# Displays 'text' or the value of the variable, then waits for keyboard input until Enter is pressed
# 'text' or variable can be left out
# variable = input('text' or variable)
# Usually used in this format, without variable it the input value is not saved
# input() always saves the value as a str data type

# var1 = 2
# var2 = input("Insert anything: ")
# print(var2)
# print(type(var2))

# var2 = int(var2)
# print(type(var2))

# sum = var1 + var2
# print(sum)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("Hello. Enter your name.")
# name = input()

# print("Welcome.", name, ", Enter your age.")
# age = input()
# age = int(age)
# year = 2025 - age

# print("You were born in", year, "! Enter your height.")
# height = int(input())

# two_m = 200 - height
# print("There are", two_m, "cm left until 2m.")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# +     add
# -     subtract
# *     multiply
# /     divide (result is a float)
# //    integer division (result is an int)
# %     modulus (remainder)
# **    exponent (power)

# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)