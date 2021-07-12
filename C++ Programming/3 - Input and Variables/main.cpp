#include <iostream>
using namespace std;

int main()
{
    // bool: true, false
    // char: -128 to 127 or 'a', 'b',...
    // short: -32,767 to 32,767
    // int: -2,147,483,648 to 2,147,483,647
    // long int(long): ±9,223,372,036,854,775,808
    // float: 10^-38 to 10^38 accurate to 7 digits
    // double: 10^-308 to 10^308 accurate to 15 digits
    // long double: 10^-4932 to 10^4932 accurate to 19 digits

    int age;
    cout << "Enter age: ";
    cin >> age;
    cout << age << endl;

    char name[256];
    cout << "Enter name: ";
    cin >> name;
    cout << name << endl;

    cout << "Age, name: ";
    cin >> age >> name;
    cout << age << name << endl;

    char text[256];
    cout << "Enter text: ";
    cin.getline(text, 256);
    cout << text << endl;

    return 0;
}