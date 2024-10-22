#include<iostream>

using namespace std;

double div(double a, double b){return a / b;}

int main()
{
 double a, b;
 cin >> a >> b;
 cout << div(a, b) << endl;
 return 0;
}