#include <stdio.h>

int main(void) {

    int grade;
    
    printf("점수를 입력세요(0-4) : ");
    scanf("%d", &grade);

    switch (grade) {
        case 4:                         // if로 보면 grade == 4 이 조건과 같은 것
            printf("훌륭해요!");
            break;
        case 3:
            printf("좋아요!");
            break;
        case 2:
            printf("평균이네요!");
            break;
        case 1:
            printf("좋지 않아요!");
            break;
        case 0:
            printf("좀 더 노력하세요!");
            break;
        default:                        // if의 else와 유사, 필수 X
            printf("잘못된 학점입니다");
            break;
    }

    return 0;
}