#include <stdio.h>
#include <stdlib.h>

int max(int num1, int num2);
void gradeOutput(char grade);

int main()
{
    printf("%d\n", max(3, 5));
    gradeOutput('A');
    return 0;
}

int max(int num1, int num2)
{
    if (num1 > num2)
        return num1;
    else
        return num2;
}

void gradeOutput(char grade)
{
    switch (grade)
    {
    case 'A':
        printf("Good Job!\n");
        break;
    default:
        printf("Work Harder!\n");
    }
}