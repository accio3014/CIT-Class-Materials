# for loop

# for variable in range(start, end, step) :
#     code to loop

# range(start, end, step) where start, end, step are numbers [ ex. range(1, 5, 2) ]
# From start to end-1(end not included), put the increased/decreased value by step into a variable and loop.
# Don't necessarily have to enter the start and step.
# If start is not entered, 0
# If step is not entered, 1
# range(5)          => start and step not entered
# range(0, 5)       => step not entered
# range(0, 5, 1)    => standard


# for i in range(0, 5, 1) :   # repeats 5 times with i taking values 0, 1, 2, 3, 4
#     print(i)                # use variable in the repeated code

# for i in range(0, 5, 1) :
#     print('hello')          # do not use variable in the repeated code


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# while loop
# while(condition) :
#       code
# Used in this format
# Similar to if statements, executes if the condition is True

# i = 0
# while(i < 5) :
#     print(i)
#     i += 1      # i = i +1, increment i


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Infinite loop
# while(True) :
#       code
# This creates an infinite loop

# continue and break
# continue and break can be used in both for and while loops

# continue
# when continue is encountered, the loop moves to the next iteration

# for i in range(0, 10, 1) :
#     if(i % 2 == 0) :
#         continue        # skip even numbers
#     print(i)


# break
# when break is encountered, the loop stops
# break is usually used with if

# i = 0
# while(True) :
#     print(i)
#     if(i == 10) :
#         break
#     i += 1


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Sample of using infinite loop, continue, break
# while(True) :
#     print("Please choose a menu option:")
#     print("1. Print hello")
#     print("2. Print hi")
#     print("3. Exit")
#     menu = int(input())

#     if(menu == 1) :
#         print("hello")
#     elif(menu == 2) :
#         print("hi")
#     elif(menu == 3) :
#         print("Exiting the menu program.")
#         break
#     else :
#         print("Invalid input. Please enter a number between 1 and 3.")
#         print()
#         print()
#         continue

#     print()
#     print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Nested loops
# A loop inside another loop
# Two nested loops is called double nested, three nested loops is called triple nested. 
# More than triple nested loops are rarely used.

# for x in range(1, 10, 1) :          # repeats 9 times
#     for y in range(1, 10, 1) :      # repeats 81 times in total
#         print(x, "*", y, "=", x * y)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# while() multiplication table
# x = 1
# while(x < 10) :
#     y = 1
#     while(y < 10) :
#         print(x, "*", y, "=", x * y)
#         y += 1
#     x += 1


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# for x in range(1, 10, 1) :          
#     for y in range(1, x+1, 1) :      # Can use an external variable in range
#         print(x, "*", y, "=", x * y)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Case 1
# for i in range(1, 9, 1) :
#     print(i)
#     for j in range(i + 1, i + 3, 1) :
#         print(j)

# Case 2
# for i in range(1, 9, 1) :
#     for j in range(i, i + 3, 1) :
#         print(j)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# for i in range(1, 6, 1) :
#     print('A')
#     for j in range(0, i, 1) :
#         print('B')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Line breaks
# print() automatically moves to the next line
# To prevent a new line, use end=''

# print("Hi ")
# print("Hello")

# print("Hi ", end='')  # line break
# print("Hello")