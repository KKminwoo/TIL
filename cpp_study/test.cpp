#include <iostream>
const double *f1(const double ar[], int n);
const double *f2(const double [], int);
const double *f3(const double *, int);
int main() {
    using namespace std;
    double av[3] = {112.3,132.1,141.1};
    const double *(*p1)(const double *, int) = f1;
    auto p2 = f2;
    cout << (*p1)(av,3) << ": " << *(*p1)(av,3) << endl;
    cout << p2(av,3) << ": " << *p2(av,3) << endl;
   
    return 0;
 }