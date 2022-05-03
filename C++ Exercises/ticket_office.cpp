/*A ticket costs $10.
The office is running a discount campaign: each group of 5 people is getting a discount, 
which is determined by the age of the youngest person in the group.
You need to create a program that takes the ages of all 5 people as input and outputs 
the total price of the tickets.*/

#include <iostream>
using namespace std;

//function for finding smallest value of a given array
int findSmallestElement(int arr[], int n){
   int temp = arr[0];
   for(int i=0; i<n; i++) {
      if(temp>arr[i]) {
         temp=arr[i];
      }
   }
   return temp;
}

int main() {
    int ages[5];
    for (int i = 0; i < 5; i++) {
        cin >> ages[i];
    }
    //your code goes here
    int min =  findSmallestElement(ages, 5);
    //cout << min;
    cout << 50*double(100-min)/double(100);
    
    return 0;
}
