# dictionary_eng.py

# Dictionary is a collection of key:value pairs.
# Unlike lists, dictionaries do not have the concept of indices. Instead, values are referenced using keys.

# dicti = {'brand':'CIT', 'classnumber':4}    # Unlike lists, dictionaries are enclosed in {} and keys and values are separated by :.
# print(dicti)

# dicti['classnumber']
# print(dicti['classnumber'])     # When accessing values in a dictionary, they are referenced using keys.

# dicti['classnumber'] = 10       # Values can be modified using keys.
# print(dicti['classnumber'])


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Inserting and Deleting Values in a Dictionary

# test = {'a':213}
# print(test)
# print()

# Insertion
# dictionary_name[key] = value
# Values are added using this format.
# test['class'] = 1
# print(test)
# print()

# Deletion
# dictionary_name.pop(key)
# Both the key and the value are deleted using the pop function.
# test.pop('class')
# print(test)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("1. Create a dictionary with brands as keys and prices as values. Use 'Americano' as the variable name.")
# Americano = {'Starlucks':3700, 'Mollys':4100, 'Emiya':2800, 'FomAFams':4100}
# print('1 :',Americano)
# print()

# print('2. Add the following data to the dictionary created above.')
# Americano['Anzelinus'] = 4900
# Americano['Coffeejean'] = 4800
# print('2 :',Americano)
# print()

# print('3. Delete the Emiya and FomAFams brands from the dictionary created above.')
# Americano.pop('Emiya')
# Americano.pop('FomAFams')
# print('3 :',Americano)
# print()

# print('4. Check if the output of print(Americano) matches the following.')
# print('4 :',Americano)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Americano = {'Starlucks': 3700, 'Mollys': 4100, 'Anzelinus': 4900, 'Coffeejean': 4800}
# print(Americano)
# print('='*20)

# Characteristics of Dictionary for Loops
# Printing only keys
# for i in Americano:
#     print(i)
# print('='*20)

# Printing only values
# for i in Americano.values():
#     print(i)
# print('='*20)

# for x in Americano :
# 	print(Americano[x])     # using key
# print('='*20)

# Printing both keys and values
# for x, y in Americano.items() :
# 	print(x, y)
# print('='*20)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Americano = {'Starlucks' : 3700, 'Mollys' : 4100, 'Anzelinus' : 4900, 'Coffeejean' : 4800}
# print('1. Print all brands.')
# print('1 : ', end='')
# for i in Americano:
#     print(i, end=' ')
# print()
# print()

# print('2. Calculate the total price of Americano.')
# sum = 0 
# for i in Americano.values():
#     sum += i        # sum = sum + i This code has the same meaning
# print('2 :', sum)
# print()

# print('3. Calculate the average price of Americano.')
# avg = sum / len(Americano)
# print('3 :', avg)
# print()

# print('4. Use the items() function to print as follows.')
# for x, y in Americano.items() :
# 	print('brand: %-12s price: %d' % (x, y))
