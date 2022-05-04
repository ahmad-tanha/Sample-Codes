/*Given a number N as input, output numbers from N to 1 on separate lines.
Also, when the current countdown number is a multiple of 5, it should output "Beep".*/

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;    
    for (int i=n;i>=1;i--) {
        cout<<i<<"\n";
        if (i%5==0){
            cout<<"Beep"<<"\n";
        }
    }
    return 0;
}

