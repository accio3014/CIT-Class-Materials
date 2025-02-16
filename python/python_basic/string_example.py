# num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']    # 숫자를 비교하기 위해 리스트 생성
# anything = input("Insert any string => ")                   # 원본 문자열 입력

# idx = 0                                                     # 문자 하나씩 비교를 위한 인덱스 번호
# num_cnt = 0
# print('Change string : ',end='')                            # 바뀐 문자 출력, 줄바꿈이 안되어야 하므로 end=''

# Case 1, using while loop
# while(idx < len(anything)):                                 # 입력한 원본 문자열 만큼 만복

#     if(anything[idx].isupper()):                            # 만약 현재 인덱스의 값이 대문자이면
#         print(anything[idx].lower(), end='')                # 소문자로 출력
#     elif(anything[idx].islower()):                          # 만약 현재 인덱스의 값이 소문자이면
#         print(anything[idx].upper(), end='')                # 대문자로 출력
#     elif(anything[idx] in num):                             # 만약 현재 인덱스의 값이 숫자인지 비교, 리스트를 이용
#         num_cnt += 1                                        # 숫자의 수 카운트 1 증가
#         print(anything[idx], end='')                        # 숫자는 그대로 출력
    
#     idx += 1                                                # 반복이 1회 끝났으니, idx 값을 증가하여 다음 인덱스 값 비교


# Case 2, using for loop
# for text in anything :
    
#     if(text.isupper()) :
#         print(text.lower(), end='')
#     elif(text.islower()) :
#         print(text.upper(), end='')
#     elif(text in num) :
#         num_cnt += 1
#         print(text, end='')


# print()
# print('Number of numbers :', num_cnt)                     # 입력한 문자에서 숫자의 개수 출력
# print()