#include <stdio.h>
#include <stdlib.h>

int main()
{
    int age;
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("You are %d years old.\n", age);

    // This does not work properly
    // Remove the new line char for the string
    char name[20];
    printf("Enter your name: ");
    fgets(name, 20, stdin);
    printf("Your name is %s.\n", name);

    return 0;
}