/* Create the class to hold the queue data, which are customer IDs (integers).
Make a Queue class, which has a size attribute, and an array, to hold the data of the queue.
The class has a remove() method to remove the front item of the queue (or shift to left in the queue), a print() method to output the queue.
Then create an add() method for the Queue class, that will take an item and add it to the end of the queue.
The code needs to be fully working, so that the Queue declaration and manipulation code in main() works. */

#include <iostream>
using namespace std; 

class Queue { 
	int size; 
	int* queue; 
	
	public:
	Queue() {
		size = 0;
		queue = new int[100];
	}
	void remove() { 
		if (size == 0) { 
			cout << "Queue is empty"<<endl; 
			return; 
		} 
		else { 
			for (int i = 0; i < size - 1; i++) { 
				queue[i] = queue[i + 1]; 
			} 
			size--; 
		} 
	} 
	void print() { 
		if (size == 0) { 
			cout << "Queue is empty"<<endl; 
			return; 
		} 
		for (int i = 0; i < size; i++) { 
			cout<<queue[i]<<" <- ";
		} 
		cout <<endl;
	}
	void add(int x) {
		for (int i = size; i >= 0; i--) { 
			if (i == size){
				queue[i]=x;
				size += 1;
			}
		} 
	}
}; 

int main() { 
	Queue q; 
	q.add(42); q.add(2); q.add(8); q.add(1); 
	q.print();
	q.remove(); 
	q.add(128); 
	q.print(); 
	q.remove(); 
	q.remove(); 
	q.print(); 

	return 0; 
} 
