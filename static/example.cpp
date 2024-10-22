#include<iostream>

using namespace std;

int fun(int a, int b){return a+b;}

int main(void)
{
 int a , b;
 cin >> a >> b;
 cout << fun(a, b) << endl;
 return 0;
}