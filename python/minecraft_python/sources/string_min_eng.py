from minecraft import *

# chat()
# chat("text") shows text in Minecraft.
# You can also use a variable with chat().
# Unlike print(), chat() cannot show many things with commas(,).

# chat("Hello! Welcome!")

# message = "Nice to meet you!"
# chat(message)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Show what you type in Minecraft.
# say = input()
# chat(say)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# say1 = input()
# chat(say1)

# say2 = input()
# chat(say2)

# say = say1 + say2
# chat(say)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# say = "Hello, welcome!"
# chat(say)

# say = input()
# chat(say)

# say = input("say again in python : ")
# chat(say)

# saycon = input("we concatenate text : ")
# chat(say + " " + saycon)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# name = input("What is your name? ")

# message = "Your name is " + name
# chat(name)
# chat(message)
# print(message)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Use input() to get a block ID and place a block in Minecraft.
# Method 1: Change the input to a number right away.

# x = 200
# y = 100
# z = 200
# block = int(input("Block ID: "))

# setpos(x, y, z)
# setblock(x, y - 1, z, block)


# Method 2: Keep it as text first.
# Change it to a number only when you need it.

# x = 200
# y = 100
# z = 200
# block = input("Block ID: ")

# setpos(x, y, z)
# setblock(x, y - 1, z, int(block))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# x = input("X: ")
# y = input("Y: ")
# z = input("Z: ")
# block = input("Block ID: ")
# length = input("Length: ")
# width = input("Width: ")

# message = (
#     "X: " + x +
#     ", Y: " + y +
#     ", Z: " + z +
#     ", Block: " + block +
#     ", Length: " + length +
#     ", Width: " + width
# )

# print(message)
# chat(message)

# setblocks(
#     int(x), int(y), int(z),
#     int(x) + (int(length) - 1),
#     int(y),
#     int(z) + (int(width) - 1),
#     int(block)
# )