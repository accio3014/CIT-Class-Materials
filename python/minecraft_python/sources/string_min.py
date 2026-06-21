# from minecraft import *

# chat()
# chat("문자")의 경우 문자를 마인크래프트에 출력함, 문자가 저장된 변수도 사용 가능
# print()와 다르게 콤마(,)로 여러개를 출력하지 못함

# chat("Hello welcome!")

# say = "nice to meet you!"
# chat(say)   # 문자가 저장된 변수 사용


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 내가 입력한 것을 마인크래프트에 출력
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


# name = input("what is your name? : ")

# say = "your name is " + name
# chat(name)
# chat(say)
# print(say)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# input() 함수를 통해 블록 id를 받아서 마인크래프트에 블록을 설치하는 코드(2종류)
# 1. 입력을 받을 때 부터 숫자로 입력 받음
# x = 200
# y = 100
# z = 200
# block = int(input("input the block id : "))     # 입력을 받자마자 int 자료형으로 변환, 즉 숫자로 변환

# setpos(x, y, z)
# setblock(x, y-1, z, block)


# 2. 해당 변수가 필요한 부분에서만 숫자로 형변환
# x = 200
# y = 100
# z = 200
# block = input("input the block id : ")          # 문자로 입력을 받음

# setpos(x, y, z)
# setblock(x, y-1, z, int(block))                 # 블록을 설치 할 때만 int 자료형으로 변환, 즉 숫자로 변환


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# x = input("x-coordinate : ")
# y = input("z-coordinate : ")
# z = input("y-coordinate : ")
# block = input("block id : ")
# length = input("length : ")
# breadth = input("breadth : ")

# say = "x : " + x + ", y : " + y + ", z : " + z + ", block type : " + block + ", length : " + length + ", breadth : " + breadth + ", not i build them!"
# print(say)
# chat(say)

# setblocks(int(x), int(y), int(z), int(x) + (length - 1), int(y), int(z) + (breadth - 2), block)