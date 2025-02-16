# stars.py

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# for i in range(1, 6, 1):
#     for j in range(0, i, 1):
#         print('* ', end='')
#     print()

# row = int(input('Input row count.\n'))
# print()

# for i in range(1, row+1, 1):
#     for j in range(0, i, 1):
#         print('* ', end='')
#     print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# * * * * *
# * * * * 
# * * * 
# * * 
# * 
# for i in range(1, 6, 1):
#     for j in range(0, 6-i, 1):
#         print('* ', end='')
#     print()

# row = int(input('Input row count.\n'))
# print()

# for i in range(0, row, 1):
#     for j in range(0, row-i, 1):
#         print('* ', end='')
#     print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# for i in range(0, 6, 1):
#     for j in range(0, i, 1):  # 공백을 출력 부분
#         print('  ', end='')
#     for x in range(1, 6-i, 1):    # 공백을 출력한 후에 별을 출력한 부분
#         print('* ', end='')
#     print() 



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


#         *
#       * *
#     * * *
#   * * * * 
# * * * * *
# for i in range(1, 6, 1):
#     for j in range(1, 6-i, 1):  # 공백을 출력 부분
#         print('  ', end='')
#     for k in range(0, i, 1):    # 공백을 출력한 후에 별을 출력한 부분
#         print('* ', end='')
#     print()                     # 공백과, 별이 전부 출력된 후에 줄 바꿈

# row = int(input('Input row count.\n'))
# print()

# for i in range(1, row+1, 1):
#     for j in range(0, row-i, 1):
#         print('  ', end='')
#     for k in range(i):
#         print('* ', end='')
#     print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# for i in range(1, 6, 1):
#     for j in range(1, 6-i, 1):  # 공백을 출력 부분
#         print('  ', end='')
#     for x in range(0, i, 1):    # 공백을 출력한 후에 별을 출력한 부분
#         print('* ', end='')

#     if(i >= 2):
#         for y in range(1, i, 1):
#             print('* ', end='')
#     print()                     # 공백과, 별이 전부 출력된 후에 줄 바꿈

# row = int(input('Input row count.\n'))
# print()

# for i in range(1, row+1, 1):
#     for j in range(1, row+1-i, 1):
#         print('  ', end='')
#     for j in range(0, 2*i-1, 1):
#         print('* ', end='')
#     print()

#         1 
#       1 2 3 
#     1 2 3 4 5 
#   1 2 3 4 5 6 7 
# 1 2 3 4 5 6 7 8 9 
# for i in range(1, 6, 1):
#     for j in range(1, 6-i, 1):
#         print('  ', end='')
#     for j in range(0, 2*i-1, 1):
#         print('%d ' % (j+1), end='')
    
#     print()


# row = int(input('Input row count.\n'))
# print()

# for i in range(1, row+1, 1):
#     for j in range(1, row+1-i, 1):
#         print('  ', end='')
#     for j in range(0, 2*i-1, 1):
#         print('%d ' % (j+1), end='')
    
#     print()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


#     * 
#   * * * 
# * * * * * 
#   * * * 
#     * 
# line = int(5/2) + 1

# for i in range(1, 2*line, 1):
#     if(i<=line):
#         for j in range(0, line-i, 1):
#             print('  ', end='')
#         for j in range(0, 2*i-1, 1):
#             print('* ', end='')
#         print()
#     else:
#         for j in range(0, i-line, 1):
#             print('  ', end='')
#         for j in range(0, (2*line-i)*2-1, 1):
#             print('* ', end='')
#         print()



# while(True):

#     row = int(input('Input row count.\n'))
#     x = int(row/2) + 1
#     print()
#     if(row == 0):
#         print('The number of rows cannot be zero\n\n')
#     elif(row%2 == 0):
#         print('The number of rows cannot be even\n\n')
#         continue
#     else:
#         for i in range(1, 2*x):
#             if(i<=x):
#                 for j in range(x-i):
#                     print('  ', end='')
#                 for j in range(2 * i - 1):
#                     print('* ', end='')
#                 print()
#             else:
#                 for j in range(i-x):
#                     print('  ', end='')
#                 for j in range((2*x-i)*2-1):
#                     print('* ', end='')
#                 print()
        
#         break
