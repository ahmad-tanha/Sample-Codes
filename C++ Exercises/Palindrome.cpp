/* A palindromic number is a number (such as 626) that remains the same when its digits are reversed.
The "isPalindrome" function returns true if a given number is a palindrome, and false, if it is not. */

#include <iostream>
using namespace std;

int reverse(int n) {
    int reverse=0, rem;       
    cin>>n;    
    while(n!=0) {
        rem=n%10; //remainder in each step    
        reverse=reverse*10+rem; //reverse number in each step   
        n/=10; //quotient in each step
    }    
    //cout<<"Reversed Number: "<<reverse<<endl;     
    return reverse;  
}

bool isPalindrome(int x) {
    if (reverse(x)==x) {
        return true;
    }    
    else {
        return false;
    }
}

int main() {
    int n;
    cin >>n;
    if(isPalindrome(n)) {
        cout <<n<< " is a palindrome";
    }
    else {
        cout <<n<< " is NOT a palindrome";
    }
    return 0;
}
