# dictionary_.py

# 딕셔너리(dictionaries)란 키와 값으로 이루어진 것
# 딕셔너리는 인덱스에 대한 개념이 없어 값을 가지고 올 때는 키를 이용해서 값을 참조한다.
# dicti = {'brand':'CIT', 'classnumber':4}    # 리스트와 다르게 {}로 되어 있으며, 키와 값은 :로 구분
# print(dicti)

# dicti['classnumber']
# print(dicti['classnumber'])     # 딕셔너리는 값을 참조할 때 키를 이용해서 참조한다

# dicti['classnumber'] = 10       # 값을 바꿀때도 키를 이용해서 바꾼다.
# print(dicti['classnumber'])


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 딕셔너리의 값 삽입과 삭제

# test = {'a':213}
# print(test)
# print()

# 삽입
# 딕셔너리명[키] = 값
# 위 형식으로 값을 추가한다.
# test['class'] = 1
# print(test)
# print()

# 삭제
# 딕셔너리명.pop(키)
# pop 함수를 사용하여 키와 값을 둘다 삭제한다.
# test.pop('class')
# print(test)
# print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("1. 브랜드를 키로, 가격을 값으로 하여 딕셔너리를 만드시오. 단, 변수 이름을 ‘Americano’로 하시오.")
# Americano = {'Starlucks':3700, 'Mollys':4100, 'Emiya':2800, 'FomAFams':4100}
# print('1 :',Americano)
# print()

# print('2. 위에서 만든 딕셔너리에서 다음 데이터를 추가하시오.')
# Americano['Anzelinus'] = 4900
# Americano['Coffeejean'] = 4800
# print('2 :',Americano)
# print()

# print('3. 위에서 만든 딕셔너리에서 Emiya와 FomAFams 브랜드를 삭제하시오.')
# Americano.pop('Emiya')
# Americano.pop('FomAFams')
# print('3 :',Americano)
# print()

# print('4. print(Americano)를 통해 아래처럼 출력되는 지 확인하시오.')
# print('4 :',Americano)
# print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Americano = {'Starlucks': 3700, 'Mollys': 4100, 'Anzelinus': 4900, 'Coffeejean': 4800}
# print(Americano)
# print()

# 딕셔너리 for문의 특징
# 키만 출력
# for i in Americano:
#     print(i)
# print()

# 값만 출력
# for i in Americano.values():
#     print(i)
# print()

# for x in Americano :
# 	print(Americano[x])
# print()

# 키와 값 모두 출력
# for x, y in Americano.items() :
# 	print(x, y)
# print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Americano = {'Starlucks' : 3700, 'Mollys' : 4100, 'Anzelinus' : 4900, 'Coffeejean' : 4800}
# print('1. 모든 브랜드를 출력하시오.')
# print('1 : ', end='')
# for i in Americano:
#     print(i, end=' ')
# print()
# print()

# print('2. 아메리카노 가격의 합을 구하시오.')
# sum = 0
# for i in Americano.values():
#     sum += i        # sum = sum + i 이 코드랑 같은 뜻
# print('2 :', sum)
# print()

# print('3. 아메리카노 가격의 평균을 구하시오.')
# avg = sum / len(Americano)
# print('3 :', avg)
# print()

# print('4. items() 함수를 이용하여 오른쪽과 같이 출력하시오.')
# for x, y in Americano.items() :
# 	print('brand: %-12s price: %d' % (x, y))