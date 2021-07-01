#include <stdio.h>
#include <stdlib.h>

int main()
{
    // Create a new file or override
    FILE *fpointer = fopen("employees.txt", "w");
    fprintf(fpointer, "Serdar, Engineer\nMary, Director\n");
    fclose(fpointer);

    // Append to file
    fpointer = fopen("employees.txt", "a");
    fprintf(fpointer, "Auri, CEO\n");
    fclose(fpointer);

    // Read file
    char line[255];
    fpointer = fopen("employees.txt", "r");
    fgets(line, 255, fpointer);
    fgets(line, 255, fpointer);
    printf("%s", line);
    fclose(fpointer);

    return 0;
}