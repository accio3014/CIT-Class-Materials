# func_eng.py

# Functions
# A function performs a specific task. There are built-in functions and user-defined functions.

# def function_name(parameter):
#       codes...
#       return value[variable]

# You can define a function in the above format and execute it as follows:
# function_name(argument)

# parameter : A variable used within the function
# return    : Ends the function and optionally returns a value to the caller
# argument  : The value passed to the function when calling it
#           parameter, return, and argument are optional
# The number of parameters in the definition and arguments in the call must match

# Examples of function definitions and calls:
# def a():                # No parameters, no return
#     print("Hello")

# def b(name):            # No return
#     print(name, "Hi")

# def c(a):
#     return a + 10

# a()
# b("Jeong")
# c(10)
# var = c(5)
# print(var)
# b(var)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Function definition with a return value
# def bmi_return(weight, height):
#     BMI = weight / height / height
#     return BMI

# Function definition without a return value
# def bmi_no_return(weight, height):
#     BMI = weight / height / height
#     print(BMI)

# Function calls
# print(bmi_return(67, 1.78))
# bmi_no_return(67, 1.78)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# The return statement is often used to share values between functions

# def check_score(score) :        # Returns a list of scores 50 and above
#     over = []
#     for i in score :
#         if(i >= 50) :
#             over.append(i)
#     return over

# def average(score)  :           # Calculates the average
#     print(sum(score) / len(score))

# score = [51, 99, 78, 34, 75, 22, 12]
# over_50 = check_score(score)    # Store scores 50 and above in over_50
# print(over_50)
# average(over_50)                # Calculate the average of scores 50 and above


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Variables can be either local or global
# local variable    : Defined inside a function and used only within that function
# global variable   : Defined outside a function and can be used both inside and outside functions
# Variable names and their scope (local or global) are not related; by default, variables are global

# a = 10          # global variable

# def test():
#     a = 5       # local variable
#     b = 20      # local variable

# print(a)
# test()
# print(a)        # The value of 'a' remains unchanged after calling test()
# print(b)        # Variable 'b' is not accessible outside test() and will cause an error


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Modifying a global variable within a function
# Use the global keyword
# Without global, you can read the variable but not modify it

# bmi = 0                                   # global variable

# def BMI(height, weight):
#     global bmi                            # Use global to modify the value
#     # global bmi = 0                    # Cannot assign a value while declaring global (error)
    
#     height = height / 100
#     bmi = weight / (height * height)

#     return bmi

# print(bmi)
# print(BMI(178, 80))                     # Print the value returned by the BMI function
# print(bmi)                              # The value of 'bmi' is modified by the BMI function


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def star(n):
#     blank = ' '
#     print("*%s*%s*" % (blank*n, blank*(5-n)))

# for i in range(0, 6, 1):
#     star(i)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Recursion functions
# A function that calls itself within its definition
# def function() :
#     print('Hello')
#     input()
#     function()        # Calls itself

# function()


# Fibonacci sequence
# def fibonacci(a, b):
#     c = a + b
#     if(a < 100) :
#         print(a, end='  ')
#         return fibonacci(b, c)      # Return None repeatedly until all calls are resolved
#     else :
#         return                      # Returns None since no value or variable is specified

# fibonacci(1, 1)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def star(n):
#     sum = n + n
#     if n <= 16:
#         print('*' * n, end=' ')
#         return star(sum)
#     else:
#         return

# star(1)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def at(a, b):
#     c = b
#     d = a * b
#     if a <= 4:
#         print('@'*a, end='')
#         print(' ', end='')
#         print('^'*b, end='')
#         print(' ', end='')
#         return at(c, d)
#     else:
#         return

# at(1, 2)
# print()


# def p(a, b):
#     a += 10
#     b += 5
#     return a, b

# x = p(10, 20)
# print(x)
