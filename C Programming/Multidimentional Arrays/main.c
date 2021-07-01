#include <stdio.h>
#include <stdlib.h>

int main()
{
    int nums[][3] = {{1, 2, 3},
                     {4, 5, 6},
                     {7, 8, 9}};

    printf("%d\n", nums[0][0]);
    printf("%d\n", nums[1][1]);
    printf("\n");

    int i, j;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            printf("%d ", nums[i][j]);
        }
        printf("\n");
    }

    return 0;
}