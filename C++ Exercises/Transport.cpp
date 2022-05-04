/* A bus can transport 50 passengers at once.
Given the number of passengers waiting in the bus station as input,
calculate and output how many empty seats the last bus will have. */

#include <iostream>
using namespace std;

int main() {
    //your code goes here
    int n;
    cin >> n;
    while (n>50){
        n %= 50;
    }
    cout << 50-n;
    return 0;
}
