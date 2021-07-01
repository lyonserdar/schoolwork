#include <stdio.h>
#include <stdlib.h>

void sayHi(char name[]);
double cube(double num);

int main()
{
    char name[] = "Serdar";
    sayHi(name);

    printf("Answer: %f\n", cube(3.0));

    return 0;
}

void sayHi(char name[])
{
    printf("Hello %s!\n", name);
}

double cube(double num)
{
    return num * num * num;
}