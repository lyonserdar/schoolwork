#include <stdio.h>
#include <stdlib.h>

int main()
{
    int index = 1;

    while (index <= 5)
    {
        printf("%d\n", index);
        index++;
    }

    do
    {
        printf("%d\n", index);
        index++;
    } while (index <= 5);

    int count = 10;

    for (int i = 0; i < count; i++)
    {
        printf("%d\n", i);
    }

    return 0;
}