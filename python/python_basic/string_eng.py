# string = "cit academy"

# You can retrieve a single value of the string using its index number.
# print(string[3])
# print(string[6])

# You can retrieve a part of the string using slicing.
# print(string[1:4])  # Retrieves values from index 1 to 4 (excluding 4) of the string variable.
# print(string[5:9])  # Retrieves values from index 5 to 9 (excluding 9) of the string variable.

# You can omit numbers in slicing.
# If omitted, it retrieves from the beginning or until the end.
# print(string[:3])   # Retrieves values from the beginning to index 3 (excluding 3) of the string variable.
# print(string[8:])   # Retrieves values from index 8 to the end of the string.
# print(string[:])    # Retrieves values from the beginning to the end, same as print(string)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# string0 = 'cit academy'
# print(string0)
# print()

# split(string)
# Divides the string into substrings and returns a list.
# If no character to split, it generates a list with the whole string.
# print("split('a') :", string0.split('a'))
# print()

# count(string)
# Returns the number of occurrences of a specific substring.
# The length of the substring to count does not matter.
# If the substring is not found, it returns 0.
# print("count('a') :", string0.count('a'))
# print()

# upper()   => Converts all characters to uppercase.
# lower()   => Converts all characters to lowercase.
# print('upper() :', string0.upper())
# print('lower() :', string0.lower())
# print()

# replace(string1, string2)
# Replaces string1 with string2.
# If the string to replace doesn't exist, it remains unchanged.
# print("replace('a', 'A') :",string0.replace('a', 'A'))
# print(string0)
# string0 = string0.replace('a', 'A')   # Reassign the variable to change its value.
# print(string0)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# bookname = 'hello java'
# number = '20NB1A'
# print(bookname)
# print(number)
# print()

# print('Q1. Replace “java” with “python” in bookname.')
# bookname = bookname.replace('java', 'python')
# print(bookname)
# print()

# print('Q2. Print the number of characters in bookname.')
# print(len(bookname))
# print()

# print('Q3. Convert bookname to uppercase.')
# bookname = bookname.upper()
# print(bookname)
# print()

# print('Q4. Print the total count of “A” in both variables.')
# sum = bookname.count('A') + number.count('A')
# print(sum)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# name = ["bell", "sona", "rick", "tony", "jade"]
# score = [52, 96, 32, 73, 85]
# print(name)
# print(score)
# print()

# print('Q1. Replace "sona" with "kona" in name using replace() function.')
# if("sona" in name):
#     idx = name.index("sona")
#     name[idx] = name[idx].replace("sona", "kona")
# else:
#     print("sona not found")
# print(name)
# print()

# print("Q2. Replace all 'o' in name with \"ecoto\" using replace() function.")
# for i in name:
#     if('o' in i):
#         idx = name.index(i)
#         name[idx] = i.replace('o', "ecoto")
# print(name)
# print()

# print("Q3. Print all elements of name.")
# print(name)
# print()

# print("Q4. If 'co' exists in name, split it and append to the end of name list.")
# for i in name:
#     if("co" in i):
#         idx = name.index(i)
#         sp = i.split("co")
#         del(name[idx])
#         for k in sp:
#             name.append(k)
# print(name)
# print()

# print('Q5. Print all elements of name.')
# print(name)
# print()

# print('Q6. Calculate and print the average of score.')
# sum = sum(score) / len(score)
# print(sum)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# Concatenating strings
# You can concatenate strings using the + symbol.
# a = "hi"
# b = " hello"
# c = a + b
# print(c)

# Operations between strings and numbers
# Only multiplication (*) is possible between strings and numbers.
# print("hello " * 5)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# print('Q1. Create a string variable A1 with the value "abc".')
# A1 = 'abc'
# print(A1)
# print()

# print('Q2. Create a string variable A2 with the value "ABC".')
# A2 = 'ABC'
# print(A2)
# print()

# print('Q3. Concatenate A1 and A2 to create a string variable B1 with the value "abcABC".')
# B1 = A1 + A2
# print(B1)
# print()

# print('Q4. Create a string variable C1 with the value of concatenating the 2nd to 4th characters from B1 and "LE".')
# C1 = B1[2:5] + 'LE'
# print(C1)
# print()

# print('Q5. Convert the characters of C1 to uppercase.')
# C1 = C1.upper()
# print(C1)
# print()

# print('Q6. Concatenate C1 and "CAR" and print the result.')
# print(C1+'CAR')
# print()

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# num = []
# for i in range(10):
#     num.append(str(i))
#     value = "%s" % i
#     num.append(value)
# print(nums)

# anything = input("Enter anything => ")

# idx = 0
# num_cnt = 0
# change = ""

# while(idx < len(anything)):

#     if(anything[idx].isupper()):
#         change += anything[idx].lower()
#     elif(anything[idx].islower()):
#         change += anything[idx].upper()
#     elif(anything[idx] in nums):
#         num_cnt += 1
#         change += anything[idx]
    
#     idx += 1

# print('Change string : ' + change)
# print('\nNumber of numbers :', num_cnt)
# print()