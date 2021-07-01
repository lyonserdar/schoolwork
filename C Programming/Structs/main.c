#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student
{
    char name[50];
    char major[50];
    int age;
    double gpa;
};

int main()
{
    struct Student student1;
    student1.age = 32;
    student1.gpa = 3.3;
    strcpy(student1.name, "Serdar");
    strcpy(student1.major, "Computer Science");

    printf("%s\n", student1.name);

    return 0;
}