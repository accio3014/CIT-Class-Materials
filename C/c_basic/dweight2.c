#include <stdio.h>

int main(void) {
    int height;
    int length;
    int width;
    int volume;
    int weight;

    printf("Enter height of box: ");
    scanf("%d", &height);               // int로 저장하기 때문에 %d를 사용, &의 경우 주소를 뜻함
    printf("Enter length of box: ");
    scanf("%d", &length);
    printf("Enter width of box: ");
    scanf("%d", &width);

    volume = height * length * width;
    weight = (volume + 165) / 166;

    printf("Volume (cubic inches): %d\n", volume);
    printf("Dimensional weight (pounds): %d\n", weight);

    return 0;
}
