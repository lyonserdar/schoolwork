#include <iostream> // for cout
#include <iomanip>  // for setw()
using namespace std;

int main()
{
    cout.setf(ios::fixed);     // no scientific notation
    cout.setf(ios::showpoint); // always show decimal
    cout.precision(2);         // two digits after the decimal

    cout << 3.14159 << endl;
    cout << setw(8) << 3.14159 << endl;

    cout << "This "
         << "is a long "
         << "String!"
         << endl;

    return 0;
}