#include <stdio.h>
#include <stdlib.h>

int main()
{
    int luckyNumbers[] = {4, 8, 16, 24};
    luckyNumbers[2] = 13;
    printf("%d\n", luckyNumbers[2]);

    int unluckyNumbers[10];
    unluckyNumbers[0] = 7;
    printf("%d\n", unluckyNumbers[0]);

    return 0;
}