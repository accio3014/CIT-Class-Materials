# func_.py

# 함수(function)
# 함수란 어떤 기능을 하는 것으로 크게 이미 있는 함수와 직접 만든 함수가 있다.

# def function_name(parameter):
#       codes...
#       return value[variable]

# 위 형식으로 함수를 직접 만들 수 있으며 만든 함수 실행의 경우 아래와 같음
# funcation_name(argument)

# parameter : 함수 내부에서 사용하는 변수
# return    : 함수를 종료하며, 특정 값을 함수를 실행한 곳으로 돌려줄 수 있음
# argument  : 함수를 실행할 때 넘겨주는 값
# parameter, return, argument는 필수가 아님
# 함수를 정의할 때 parameter의 개수와 함수를 실행할때의 argument의 개수는 같아야 함


# def a():                # parameter, return이 없는 경우
#     print("Hello")

# def b(name):            # return이 없는 경우
#     print(name,"Hi")

# def c(a):
#     return a+10

# a()
# b("Jeong")
# var = c(5)              # 보통 return이 있는 함수의 경우 변수랑 같이 사용
# print(var)
# b(var)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 함수를 선언(정의), return을 사용한 경우
# def bmi_return(weight, height):
#     BMI = weight / height / height

#     return BMI

# return 없이 함수를 선언
# def bmi_no_return(weight, height):
#     BMI = weight / height / height

#     print(BMI)

# 함수를 호출(실행)
# print(bmi_return(67, 1.78))
# bmi_no_return(67, 1.78)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# return의 경우 보통 함수끼리 서로 값을 공유할 때 사용

# def check_score(score):     # 점수들 중 50점 이상의 점수를 구분하여 리스트로 리턴
#     over = []
#     for i in score:
#         if(i >= 50):
#             over.append(i)
    
#     return over

# def average(score):         # 평균을 구함
#     print(sum(score) / len(score))


# score = [51, 99, 78, 34, 75, 22, 12]
# over_50 = check_score(score)    # check_score 함수를 통해서 50점 이상인 점수를 over_50 변수에 저장
# print(over_50)
# average(over_50)                # 50점 이상인 점수의 평균을 구함


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def star(n):
#     print("*" + " "*n + "*" + " "*(5-n) + "*")
#     blank = ' '
#     print("*%s*%s*" % (blank*n, blank*(5-n)))

# for i in range(0, 6, 1):
#     star(i)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 변수는 크게 local, global 2가지가 있음
# local 변수    : 함수 내부에서 만들었고 함수 내부에서만 쓰이는 변수
# global 변수   : 함수 밖에서 만들었고 함수 내외부에서 둘다 사용 가능
# 변수의 이름과 local, global은 상관 없으며, 변수는 기본적으로 global 변수를 얘기함

# a = 10          # global 변수

# def test():
#     a = 5       # local 변수
#     b = 20      # local 변수

# test()
# print(a)        # test 함수를 실행해도 a 변수의 값은 변화가 없음
# print(b)        # 변수 b는 test함수에서만 사용하기 때문에 함수 밖에서 참조를 하는 경우 에러 발생



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 함수 밖에 있는 변수의 값을 함수 내부에서 변경하는 방법
# global 변수
# 위 형식으로 함수 내부에서 함수 밖에 있는 변수의 값을 변경할 수 있음
# global을 사용안해도 함수 내부에서 값을 참조는 가능하지만 값 변경은 불가능

# bmi = 0                                   # global 변수

# def BMI(height, weight):
#     global bmi                            # 함수 내부에서 global 사용하여 값을 변경할 수 있음(이거 안쓰면 안됨)
#     # global bmi = 0                    # global 키워드에서 변수에 값을 넣을 수는 없음 (오류)
    
#     height = height / 100
#     bmi = weight / (height * height)

#     return bmi

# print(bmi)
# print(BMI(178, 80))                     # BMI 함수에서 리턴된 값을 출력
# print(bmi)                              # BMI 함수에서 global 키워드를 이용하여 bmi 변수의 값을 변경함


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 재귀함수
# 함수 내부에서 자기자신을 호출하는 함수
# def function() :
#     print('Hello')
#     input()
#     function()        # 자기 자신을 호출

# function()


# 피보나치 수
# https://pythontutor.com/render.html#mode=display
# def fibonacci(a, b) :
#     c = a + b
#     if(a < 100):
#         print(a, end='  ')
#         return fibonacci(b, c)      # return None이 계속 반복되어서 호출된 함수들이 종료 된다.
#     else:
#         return                      # return 하는 값 또는 변수가 없기 때문에 None이 return 됨

# fibonacci(1, 1)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def star(n):
#     sum = n + n
#     if(n <= 16):
#         print('*' * n, end=' ')
#         return star(sum)
#     else:
#         return

# star(1)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def at(a, b):
#     c = b
#     d = a * b
#     if(a <= 4):
#         print('@'*a,end='')
#         print('^'*b,end='')
#         return at(c,d)
#     else:
#         return

# at(1,2)
# print()


# def p(a, b):
#     a += 10
#     b += 5

#     return a, b

# x  = p(10,20)
# print(x)