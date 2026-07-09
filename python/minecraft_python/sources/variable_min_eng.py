from minecraft import *

# setpos(x, y, z)
# Use numbers or variables that store numbers for x, y, and z.
# Move to the position you want.

# setpos(100, 100, 100)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# x = 200
# y = 200
# z = 200
# setpos(x, y, z)     # Using variables


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# getpos()
# You can use getpos() to get your current position.
# But if you only use getpos(), you can get the current position but cannot see it.
# So use it together with print().

# getpos()            # Gets the current position, but you cannot see it
# print(getpos())     # Gets the current position and prints it


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# setblock(x, y, z, b)
# Creates one block at the x, y, z position.
# The block ID is b.
# x, y, z, and b must all be numbers or variables that store numbers.

# setpos(100, 100, 100)
# setblock(100, 100, 100, 2)  # Creates a block with block ID 2 at position 100, 100, 100


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# setblocks(x1, y1, z1, x2, y2, z2, b)
# Creates many blocks from x1 to x2, y1 to y2, and z1 to z2.
# x1, y1, z1, x2, y2, z2, and b must all be numbers or variables that store numbers.
# x1, y1, z1    => starting position
# x2, y2, z2    => ending position
# It creates blocks of type b.
# The starting position is included, and the ending position is also included.

# setpos(100, 100, 100)
# setblocks(100, 100, 100, 101, 101, 101, 2)