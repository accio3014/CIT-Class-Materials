#include <stdio.h>

int main() {

    // C언어에서 변수 만들기
    // type variable = value;
    // 위 형식으로 사용
    // type의 종류는 char, int, float 등이 있음
    // char         문자 1개
    // int          정수
    // float        실수

    // variable print
    // variable을 출력할 때는 문자열 포맷팅을 사용
    // char     %c      문자 한개
    // char     %s      문자열
    // int      %d
    // float    %f
    // %c, %s, %d, %f는 포맷팅 기호로 따음표 안에 들어가며 포맷팅 기호 자리에 variable의 값이 들어감

    // char name = 'J';            // char의 경우 문자 1개를 저장함
    // char name_2[6] = "Jeong";   // 문자열을 저장하고 싶은 경우에는 variable[문자열의길이 + 1]로 저장 가능
    // int age = 10;
    // float pi = 3.14;

    // printf("%c\n", name);       // name variable에는 문자 1개가 저장되었기 때문에 %c
    // printf("%s\n", name_2);     // name_2 variable에는 문자열이 저장되어 있기 때문에 %s
    // printf("%d %f\n", age, pi);


    ///////////////////////////////////////////////////////////////////////////////////////////////////


    // Keyboard typing(= input)
    // C언어에서는 키보드 입력을 받기 위해 scanf()함수를 사용
    // scanf("%d", &variable);
    // 위 형식으로, 포맷팅 기호와 같이 사용함

    // int i = 0;              // 키보드 입력을 저장할 변수 초기화(Initializaion)
    // scanf("%d", &i);        // %d 이기 때문에 정수를 입력 받음
    // printf("%d\n", i);

    // char anything[101] = "";
    // printf("최대 100자리의 문자를 입력하세요 : ");
    // scanf("%s", anything);          // 문자열의 경우 &는 사용 안함
    // printf("%s \n", anything);


    return 0;
}