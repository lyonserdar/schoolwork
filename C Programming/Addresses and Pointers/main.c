#include <stdio.h>
#include <stdlib.h>

int main()
{
    int age = 30;
    double gpa = 3.4;
    char grade = 'A';

    // Memory Addresses
    printf("age: %d stored at %p\n", age, &age);
    printf("gpa: %f stored at %p\n", gpa, &gpa);
    printf("grade: %c stored at %p\n", grade, &grade);

    // Pointers
    int *pAge = &age;
    double *pGpa = &gpa;
    char *pGrade = &grade;

    printf("pAge: %p\n", pAge);
    printf("pGpa: %p\n", pGpa);
    printf("pGrade: %p\n", pGrade);

    // Dereferencing Pointers
    printf("age: %d stored at %p\n", *pAge, pAge);
    printf("gpa: %f stored at %p\n", *pGpa, pGpa);
    printf("grade: %c stored at %p\n", *pGrade, pGrade);

    // or
    printf("age: %d stored at %p\n", *&age, &age);

    return 0;
}
