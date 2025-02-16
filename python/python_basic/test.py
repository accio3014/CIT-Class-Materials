def unique_letters(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    tmp = []
    for i in s:
        if(i.lower() in alphabet):
            tmp.append(i.lower())
    
    tmp = set(tmp)
    unique = list(tmp)
    
    return unique

print(unique_letters("Happy days are here again!"))
print(unique_letters("Columbia University in the City of New York"))


def unique_letters2(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    unique = list(set([i.lower() for i in s if i.lower() in alphabet]))

    return unique

print(unique_letters2("Happy days are here again!"))
print(unique_letters2("Columbia University in the City of New York"))


def convert_list(input_file, output_file):
    file = open(input_file, 'r')
    output = open(output_file, 'w')

    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    for line in file:           # 파일 내용을 한줄씩 읽어 line 변수에 저장
        # print(line)

        tmp = ""
        no_alphabet = 0
        for i in line[:-1]:     # 파일 내용에 한줄에는 마지막에 안보이는 \n이 있기 때문에 line[:-1]로 \n을 제외하고 반복 
            if(i.lower() in alphabet):
                tmp += i.lower()
            else:               # 특수문자 또는 스페이스바가 있는 경우
                no_alphabet += 1
        tmp += '\n'             # 파일에 복사하기 전 엔터 추가
        # print(tmp)
        if(no_alphabet == 0):   # 특수문자 또는 스페이스바가 없는 경우만 파일에 쓰기
            output.write(tmp)
    
    file.close()
    output.close()

# convert_list('/Users/seokcheon/Downloads/wordlist.txt', 'new_worldlist.txt')


def length_n(file_name,n):
    file = open(file_name, 'r')

    n_list = []
    for line in file:           # 파일 내용을 한줄씩 읽어 line 변수에 저장
        if(n == len(line[:-1])):        # 파일 내용에 한줄에는 마지막에 안보이는 \n이 있기 때문에 line[:-1]로 \n을 제외하고 반복 
            n_list.append(line[:-1])    # 파일 내용에 한줄에는 마지막에 안보이는 \n이 있기 때문에 line[:-1]로 추가
    file.close()

    return n_list
    

# print(length_n('/Users/seokcheon/Downloads/wordlist.txt', 5))

def starts_with(file_name, n, first_letter):
    file = open(file_name, 'r')

    f_n_list = []
    for line in file:                       
        if((n == len(line[:-1])) and (line[0] == first_letter)):
            f_n_list.append(line[:-1])    
    file.close()

    return f_n_list

# print(starts_with('/Users/seokcheon/Downloads/wordlist.txt', 5, 's'))

def contains_letter(file_name, n, included):
    included_len = len(included)
    file = open(file_name, 'r')

    i_n_list = []
    for line in file:                       
        if((n == len(line[:-1])) and (included in line[:-1])):
            if(line[0:included_len] != included):    # included 문자로 시작 안할때
                    i_n_list.append(line[:-1])
    file.close()

    return i_n_list

# print(contains_letter('/Users/seokcheon/Downloads/wordlist.txt', 5, 'sa'))

def vowel_heavy(file_name, n, m):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']     # 모음 리스트 생성
    file = open(file_name, 'r')

    vowel_list = []
    
    for line in file:
        cnt_vowels = 0                      # 모음의 개수를 세기 위해 선언
        if(n == len(line[:-1])):            # 길이가 같은지 비교
            for i in line[:-1]:             # 문자의 처음부터 끝까지 하나씩 i 변수에 넣음
                if(i in vowels):            # 만약 문자 하나씩 비교를 하는데 모음 리스트에 포함된다
                    cnt_vowels += 1         # 모음 개수 하나 증가
        
        if(cnt_vowels >= m):                # 만약 모음의 개수가 m보다 큰 경우
            vowel_list.append(line[:-1])    # 리스트에 해당 문자 추가
    file.close()

    return vowel_list

# print(vowel_heavy('/Users/seokcheon/Downloads/wordlist.txt', 5, 3))