# variable_.py

# 변수(variable)
# 변수(variable) = 값
# 위 형식으로 변수(variable)에 값을 저장
# = 기호의 뜻과 다르게 단순하게 값이 변수(variable)에 저장됨
# 변수(variable)는 아래의 규칙을 지키면 원하는 대로 가능
# 1. 숫자로 시작 불가능
# 2. 기호 "_"를 제외한 특수문자 불가능
# 3. 띄어쓰기 불가능
# 4. 예약어 불가능


# my_name = "Jeong"



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 자료형(Data type)
# str   -> String       문자    => 따음표로 이루어져 있음(따음표가 있으면 무조건 문자) " "  ' '
# float -> Float        실수    => 따음표가 없고 소수점이 있으면 실수
# int   -> Integer      정수    => 없고 소수따음표가 점도 없으면 정수
# 일상적으로 사용하는 말들(영어, 중국어, 한국어 등)이 따음표가 없다 => 오류

# a = 10      # a라는 변수에 int 자료형인 10 저장
# b = 'cit'   # b라는 변수에 str 자료형인 'cit' 저장


# name = '파이썬'
# age = 20
# height = 178

# print(name)

# name = '파이리'
# print(name)

# name = '파이팅'
# print(name)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print('문자' or 변수 or 숫자)
# print('문자' or 변수 or 숫자) 함수는 괄호안에 있는 '문자', 숫자 또는 변수의 값을 출력한 후 엔터한다.
# 한줄에 여러개를 출력하고 싶으면 콤마(,)를 사용
# 만약 print()를 사용할 경우 빈 한줄이 출력

# name = "파이썬"
# age = 28
# height = 188
# print(name)
# print()         # 빈 한줄 출력
# print(age)
# print(height)
# print("hi")
# print()
# print(5)
# print(5*10)
# print(name, age, height, "hello")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 자료형을 확인하는 방법
# type() => 괄호안에 있는 변수 또는 값의 자료형을 가지고 옴
# type(변수)        <= 이렇게 사용하는 경우 프로그램으로 동작은 하지만 자료형을 눈으로 볼 수 없음
# print(type(변수))
# 위 형식으로 print()안에 넣어서 주로 사용

# int0 = 1                # int0라는 변수에 int 자료형인 1 저장
# float0 = 3.14
# str0 = 'test'
# type(int0)              # 동작을 하지만 자료형을 눈으로 볼 수 없음
# print(type(int0))       # type()을 사용하여 int0의 자료형 출력
# print(type(float0))
# print(type(str0))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 형 변환(casting)
# str(변수 or 값)     => 변수 or 값을 str 자료형으로 변환
# float(변수 or 값)   => 변수 or 값을 float 자료형으로 변환
# int(변수 or 값)     => 변수 or 값을 int 자료형으로 변환
# 단순히 연산할때만 사용하면 원본의 값은 변하지 않음
# 원본의 자료형을 변환 시키기 위해서는 변수에 값을 다시 넣어야 함 [ ex. a = int(a) ]

# var1 = 2
# var2 = '31'
# result = var1 + int(var2)   # result 변수에 var1 변수 + int 자료형으로 변환한 var2변수 저장
# print(result)
# print(type(var2))           # 변수 var2 자료형을 출력, result 변수에는 int 자료형으로 계산이 되었지만
#                             # 실제 변수의 자료형은 변환 안됨
# var2 = int(var2)            # var2 변수에 int 자료형으로 변환한 var2 변수 저장 
# print(type(var2))           # 변수 var2 자료형을 출력


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# input('문자' or 변수)
# '문자' 또는 변수를 출력한 후 엔터키를 누르기 전까지 키보드 입력을 받음
# '문자' 또는 변수는 생략 가능
# 변수 = input('문자' or 변수)
# 위 형식을 주로 사용, input()만 사용했을 경우 입력 값을 저장하지 못함
# input()은 무조건 str 자료형으로 값을 저장함

# var1 = 2
# var2 = input("Insert anything : ")
# print(var2)
# print(type(var2))

# var2 = int(var2)
# print(type(var2))

# sum = var1 + var2
# print(sum)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("안녕하세요. 이름을 입력해주세요.")
# name = input()

# print("환영합니다.", name, "님. 나이를 입력해주세요.")
# age = input()
# age = int(age)
# year = 2025 - age

# print(year, "년에 태어나셨네요! 키를 입력해주세요.")
# height = int(input())           # 입력을 받자마자 int로 변환
# left_hight = 200 - height
# print("2m까지", left_hight, "cm 남았네요.")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# +     더하기
# -     빼기
# *     곱하기
# /     나누기(실수로 나옴)
# //    몫(정수로 나옴)
# %     나머지
# **    제곱

# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print('두 개의 숫자를 입력해주세요')
# num1 = int(input())
# num2 = int(input())

# print('[결과]')
# print(num1 + num2)
# print(num1 - num2)
# print(num1 / num2)
# print(num1 * num2)
# print(num1 // num2)
# print(num1 % num2)