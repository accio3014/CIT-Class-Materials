# reference.py

# 1. 문자 포매팅
# 2. 이스케이프 코드
# 3. 줄바꿈 무시


# [1. 문자 포맷팅]

# 문자 포맷팅     => 문자를 표현하는 따음표안에 포맷팅 기호를 적어야 함
# 문자 포맷팅을 사용하는 이유 : 여러개의 변수와 문자를 같이 출력하는 경우 콤마(,)를 사용 시 의도하지 않은
# 띄어쓰기가 발생하기 때문. 포맷팅을 이용하면 내가 원하는 위치에 변수의 값이 들어감

# Hello CIT     <= 이렇게 출력하고 싶음
# a = "Hello"
# b = "CIT"
# print(a, b)                 # 콤마를 사용할 경우 자동으로 띄어쓰기가 되어 출력시 띄어쓰기를 계산을 해야함
#                             # 그리고 콤마의 경우 사용할 수 있는 수량이 정해져 있어 많은 변수의 값을 출력 불가
# print("%s %s" % (a, b))     # 포맷팅을 사용할 경우 내가 원하는 위치에 변수 값이 들어가므로 커스텀이 용이


# 포맷팅 기호   => 따음표 안에 적어야 함
# 문자(str)     => %s
# 실수(float)   => %f
# 정수(int)     => %d
# 위 포맷팅 기호는 변수의 자료형에 맞게 사용

# 1. 1개의 변수를 출력할 때
# print("%f" % (변수명))                변수명의 값이 %f위치에 들어감
# 2. 2개 이상의 변수를 출력할 때
# print("%f %s" % (A변수명, B변수명))    A변수명의 값이 %f위치에 들어가고 B변수명의 값이 %s 위치에 들어감


# My name is Park! And my age is 15. <= 이렇게 출력하고 싶음
# name = "Park"   # 문자이기 때문에 %s
# print("My name is %s! And my age is 15." % (name))

# i = "My"        # 문자이기 때문에 %s
# print("%s name is %s! And my age is 15." % (i, name))

# age = 15        # 정수이기 때문에 %d
# print("%s name is %s! And my age is %d." % (i, name, age))

# print("%d %d" % (age, age)) # 포맷팅을 사용할 때 같은 변수를 여러번 가능


# 포맷팅의 소수점 표시
# 실수의 경우 %f를 사용
# %f 사용시 기본 값은 소수점 6번째 자리 수 까지 출력. 정확히는 7번째 자리에서 반올림한 후 6자리 까지 출력
# pi = 3.1415
# print("%f" % (pi))  # 만약 변수 값이 6자리 보다 작으면 나머지 소수점 자리의 숫자는 0으로 출력

# %.숫자f       => 소수점 숫자 번째 까지 출력. 정확히는 숫자 + 1 자리수에서 반올림한 후 숫자 번째 자리수까지 출력
# print("%.3f" % (pi))    # 소수점 4번째 자리에서 반올림 한 후 소수점 3째 자리까지 출력



# 포매팅을 이용해서 문자열을 정렬할 수 있다.
# 100000
#  10000
#   1000
# 위 와 같이 출력하고 싶을 경우
# a = 100000
# b = 10000
# c = 1000
# print("%7d" % a)
# print("%7d" % b)
# print("%7d" % c)

# 포매팅 기호 사이에 숫자를 넣을 수 있음
# %7d   =>  7칸의 공간에서 출력할 값을 오른쪽에 붙여 출력
# %-7d  =>  7칸의 공간에서 출력할 값을 왼쪽에 붙여 출력
# 만약 출력할 내용이 7칸보다 클경우 왼쪽에 붙여 출력
# c = 1000
# print('%7d' % c)
# print('%-7dhi' % c)

# 위와 같이 정렬에 대한 것은 %s, %d, %f 전부 가능

# pi = 3.14159265
# print('%-6.3fhi' % pi)      # 3.142가 출력된 이유는 4번째 자리의 값이 5이므로 반올림, .도 한자리로 포함


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# [2. 이스케이프 코드]
# 특별한 문자로 문자 출력시에 사용한다  => 따음표 기호('') 안에 있음
# \n    문자열 안에서 줄을 바꿀 때 사용
# \t    문자열 사이에 탭 간격을 줄 때 사용
# \\    문자 \를 그대로 표현할 때 사용
# \'    ' 를 출력
# \"    " 를 출력

# print("Hello\nCIT")     # \n 사용
# print("Hello\tCIT")     # \t 사용
# print("Hello\\CIT")     # \\ 사용
# print("\' \"")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# [3. 줄바꿈 무시]
# print()를 사용하게 되면 자동으로 줄을 바꾼다
# 이것을 무시하기 위해서는 print() 안에 ,end=''을 사용한다.
# 정확한 ,end='문자'의 뜻은 어떤 내용을 출력하고 뒤에 줄 바꿈을 하지 않는 후 문자를 추가이다. 보통 빈칸으로 많이 사용
# for i in range(0, 5, 1):
#     print('cit ', end='')   # 한줄에 반복한 결과 출력
# print()                     # , end=''을 사용한 후 print()를 사용하여 한칸 띄운다

# for i in range(0, 5, 1):
#     print('cit', end='@')
# print()