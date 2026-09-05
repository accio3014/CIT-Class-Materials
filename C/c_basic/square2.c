#include <stdio.h>

int main(void) {
    int i, n;

    printf("This program prints a table of squares.\n");
    printf("Enter number of entries in table: ");
    scanf("%d", &n);

    for(i = 1; i <= n; i++) {              // for 반복의 경우 (초기화 ; 조건 ; 증감) 이렇게 들어감
        printf("%10d%10d\n", i, i * i);
    }

    return 0;
}
