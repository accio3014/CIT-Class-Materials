# if_eng.py

# Comparison operators
# The result of the comparison operation is always True or False.
# ==    : True if the same, False if different.
# !=    : True if different, False if the same
# <
# >
# <=
# >=

# print(5 != 2)
# print(5 < 2)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# if(condition) :
#   Run if the above condition is True.
# elif(condition) :
#   Run elif the above condition is True.
# else :
#   Run if all condition are False.

# if    : always use 1
# elif  : use range 0 ~ infinity
# else  : use 0 or 1
# if can be used by nesting within if.


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 100 ~ 90  : A
# 89 ~ 70   : B
# 69 ~ 60   : C
# 59 ~      : D

# score = int(input())

# if(100 >= score >= 90) :
#     print('A')
# elif(89 >= score >= 70):
#     print('B')
# elif(69 >= score >= 60):
#     print('C')
# elif(59 >= score >= 0):
#     print('D')

# print("End")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# age = int(input("Enter your age : "))

# if(age >= 12) :
#     print("Good, Have fun watching.")
# else :
#     print("Sorry, Only over 12 years watch the movie.")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("Enter number.")
# num = int(input())

# if(num % 2 == 0) :
#     print("Even.")
# else :
#     print("Odd")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# not   : If True, the result is reversed to False. If it is False, the result is reversed to True.
# and   : True if both sides are True, False if even one side is False
# or    : False if both sides are False, True if at least one side is True
# The execution order is executed in the order of not, and, or.
# print(not(1 == 1))
# print((1 != 5) and (10 <= 15))
# print((6 != 6) or (5 == 3))


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Nested if 
# if can be nested

# age = int(input("Enter your age: "))
# is_member = input("Are you a member? (yes or no): ")

# if(age >= 18) :
#     if(is_member == "yes") :
#         print("Welcome, adult member!")
#     else :
#         print("Adult non-member, please sign up.")
# else :
#     if(is_member == "yes") :
#         print("Welcome, young member!")
#     else :
#         print("Young non-member, please sign up.")



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #





# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# An year is said to be leap year if it divisible by 4 and not divisible by 100, 
# with an exception that it is divisible by 400.

# year = int(input('Enter year : '))
 
# if(((year%4 == 0) and (year%100 != 0)) or (year%400 == 0)) :
#     print(year, "is a leap year.")
# else :
#     print(year, "is not a leap year.")