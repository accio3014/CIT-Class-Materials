def find_max_two(arr: list[int]) -> list[int]:      # arr : parameter 이름
                                                    # list[int] : arr의 type을 지정
                                                    # -> list[int] : 함수의 리턴 타입
                                                    # 이런 형태를 타입 어노테이션(Type Annotations)이라 함
    if(len(arr) < 2):
        return arr
    
    max1, max2 = arr[:2]

    if(max2 > max1):
        max1, max2 = max2, max1                     # python의 경우 바로 값의 교환이 가능

    for i in arr[2:]:
        if(i > max1):
            max1, max2 = i, max1
        elif(i > max2):
            max2 = i

    return [max1, max2]


# Test code
arr = [[3, -1, 5, 0, 7, 4, 9, 1]]
for a in arr:
    print("%s에서 가장 큰 두 값: %s" % (a, find_max_two(a)))
