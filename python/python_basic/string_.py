# string_.py


# string = "cit academy"

# 인덱스 번호를 이용하여 문자열의 하나의 값을 가지고 올 수 있음
# print(string[3])
# print(string[6])

# 슬라이싱을 이용하여 문자열의 일부분의 값을 가지고 올 수 있음
# print(string[1:4])  # string 변수의 문자열 인덱스의 1부터 4까지의 값을 가지고 옴(4는 포함 X)
# print(string[5:9])  # string 변수의 문자열 인덱스의 5부터 9까지의 값을 가지고 옴(9는 포함 X)

# 슬라이싱의 숫자를 생략할 수 있음.
# 생략을 할 경우 처음 또는 끝까지 값을 가지고 옴
# print(string[:3])   # string 변수의 문자열 인덱스의 처음부터 3까지의 값을 가지고 옴(3은 포함 X)
# print(string[8:])   # string 변수의 문자열 인덱스의 8부터 끝까지의 값을 가지고 옴
# print(string[:])    # string 변수의 처음부터 끝까지의 값을 가지고 옴 print(string) 이 코드와 같음


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# string0 = 'cit academy'
# print(string0)

# split(문자열)
# 문자열을 문자열로 나누어 리스트로 리턴
# 만약에 나눌 문자 없을 경우 해당 문자열 전체를 하나의 리스트로 생성
# print("split('a') :",string0.split('a'))

# count(문자열)
# 문자열에서 특정 문자열의 개수를 리턴 => 수를 알고 싶은 문자의 길이는 상관 없음
# 만약에 문자가 없을 경우 0을 리턴
# print("count('a') :",string0.count('a'))

# upper()   => 문자를 전부 대문자로
# lower()   => 문자를 전부 소문자로
# print('upper() :',string0.upper())
# print('lower() :',string0.lower())

# replace(문자1, 문자2)
# 문자1을 문자2로 전부 변경
# 만약에 변경할 문자가 없는 경우 변경 안됨
# print("replace('a', 'A') :",string0.replace('a', 'A'))
# print(string0)
# string0 = string0.replace('a', 'A')   # 이렇게 변수 재지정을 해야 변수에 대한 값이 변경됨
# print(string0)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# bookname = 'hello java'
# number = '20NB1A'
# print(bookname)
# print(number)
# print()

# print('Q1. bookname에서 “java”를 “python”으로 고치시오.')
# bookname = bookname.replace('java', 'python')
# print(bookname)
# print()


# print('Q2. bookname의 문자열 개수를 출력하시오.')
# print(len(bookname))
# print()

# print('Q3. bookname에서 문자열을 모두 대문자로 바꾸시오.')
# bookname = bookname.upper()
# print(bookname)
# print()

# print('Q4. 두 변수에 등장하는 “A”의 총 개수를 출력하시오.')
# sum = bookname.count('A') + number.count('A')
# print(sum)
# print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# name = ["bell", "sona", "rick", "tony", "jade"]
# score = [52, 96, 32, 73, 85]
# print(name)
# print(score)
# print()

# print('Q1. name에서 “sona”를 “kona”로 바꾸시오. replace() 함수 이용')
# if("sona" in name):                                 # 먼저 'sona'가 리스트에 있는지 확인
#     idx = name.index("sona")                        # 값 변경을 위한 'sona'의 인덱스 번호 찾아 idx 변수에 저장
#     name[idx] = name[idx].replace("sona", "kona")   # replace()함수를 이용하여 'sona'를 'kona'로 변경
# else:                                               # 'sona'가 리스트에 없는 경우
#     print("sona 없음")
# print(name)
# print()

# print("Q2. name의 모든 'o'를 \"ecoto\"로 바꾸시오. replace() 함수 이용")
# for i in name:                                      # name 리스트의 값을 전체 반복 하여 변수i에 저장
#     if('o' in i):                                   # i에 'o'가 있을경우 실행, 즉 문자열 안에 'o'가 있으면 실행
#         idx = name.index(i)                         # 값 변경을 위해 'o'가 들어간 문자열의 인덱스 번호를 찾아 idx 변수에 저장
#         name[idx] = i.replace('o', "ecoto")         # replace()함수를 통해 'o'를 "exoto"로 값 변경          
# print(name)
# print()

# print("Q3. name의 원소들을 모두 출력하시오.")
# print(name)
# print()

# print("Q4. name 리스트에서 \"co\"가 있으면 분할하여 name 리스트의 맨 뒤에 추가하시오.")
# for i in name:                                      # name 리스트의 값을 전체 반복 하여 변수i에 저장
#     if("co" in i):                                  # i에 'co'가 있을경우 실행, 즉 문자열 안에 'co'가 있으면 실행
#         idx = name.index(i)                         # 값 삭제 및 변경을 위해 'co'가 들어간 문자열의 인덱스 번호를 찾아 idx 변수에 저장
#         sp = i.split("co")                          # 'co'가 들어간 문자열을 'co'를 기준으로 나눔, 
#                                                     # split()를 사용하면 나눠진 문자열은 리스트 형태로 sp 변수에 저장
#         del(name[idx])                              # 'co'가 들어간 문자열을 리스트에서 삭제
#         # name = name + sp                            # 'co'를 기준으로 나눠진 리스트(sp)와 기존의 리스트(name)를 더함
#                                                     # append를 안하는 이유는 append를 사용할 경우 2중 리스트가 됨
#                                                     # 아래 반복문을 사용하던지, 현재 코드의 리스트의 덧셈을 사용하던지 둘중 하나를 진행해야 함
                                                    
#         for k in sp:                                # 반복문을 사용하여 분할된 문자열이 있는 sp리스트의 값을 name 변수에 저장
#             name.append(k)
# print(name)
# print()


# print('Q5. name의 원소들을 모두 출력하시오.')
# print(name)
# print()

# print('Q6 score의 평균을 구하고 출력하시오.')
# avg = sum(score) / len(score)
# print(avg)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 문자열 합치기
# + 기호를 이용하여 문자열을 합칠 수 있음
# a = "hi"
# b = " hello"
# c = a + b
# print(c)

# 문자와 숫자의 연산
# 문자와 숫자의 경우 곱하기(*)만 가능
# print("hello " * 5)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print('Q1. "abc"를 값으로 가지는 문자열 변수 A1을 만드시오')
# A1 = 'abc'
# print(A1)
# print()

# print('Q2. "ABC"를 값으로 가지는 문자열 변수 A2를 만드시오')
# A2 = 'ABC'
# print(A2)
# print()

# print('Q3. A1과 A2를 합쳐 "abcABC"를 값으로 가지는 문자열 변수 B1을 만드시오')
# B1 = A1 + A2
# print(B1)
# print()

# print('Q4. B1에서 2번째부터 4번째 문자 "cAB"와 "LE"를 합쳐 만든 변수 C1를 만드시오')
# C1 = B1[2:5] + 'LE'
# print(C1)
# print()

# print('Q5. C1의 글자를 대문자로 고치시오')
# C1 = C1.upper()
# print(C1)
# print()

# print('Q6. C1과 "CAR"을 합쳐서 출력하시오')
# print(C1+'CAR')
# print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']    # 숫자를 비교하기 위해 리스트 생성
# num = []
# for i in range(10):
#     num.append(str(i))
#     value = "%s" % i
#     num.append(value)
# print(nums)

# anything = input("Enter anything => ")       # 원본 문자열 입력

# idx = 0
# num_cnt = 0
# change = ""

# while(idx < len(anything)):                     # 입력한 원본 문자열 만큼 만복

#     if(anything[idx].isupper()):                # 만약 현재 인덱스의 값이 대문자이면
#         change += anything[idx].lower()
#     elif(anything[idx].islower()):                # 만약 현재 인덱스의 값이 소문자이면
#         change += anything[idx].upper()
#     elif(anything[idx] in nums):                   # 만약 현재 인덱스의 값이 숫자인지 비교, 리스트를 이용
#         num_cnt += 1                            # 숫자의 수 카운트 1 증가
#         change += anything[idx]
    
#     idx += 1                                    # 반복이 1회 끝났으니, idx 값을 증가하여 다음 인덱스 값 비교

# print('Change string : ' + change)                # 바뀐 문자 출력, 줄바꿈이 안되어야 하므로 end=''
# print('\nNumber of numbers :', num_cnt)         # 입력한 문자에서 숫자의 개수 출력
# print()