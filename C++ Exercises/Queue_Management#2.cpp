/* Add a new functionality to the previous code: 
adding two queues together. The result should be a new queue,
where the elements of the first queue come first, 
followed by the second queue's elements. Given the Queue class,
overload the + operator, so that the code in main works and successfully adds two queues. */


#include <iostream>
using namespace std; 

class Queue { 
	int size; 
	int* queue; 
	int var;
	
	public:
		//Queue() { } //error!
		Queue(int u) : var(u) { };
		//Queue operator+(Queue &obj); //error!
 		Queue() { 
			size = 0;
			queue = new int[100];
		}
		void add(int data) { 
			queue[size] = data; 
			size++;
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
			cout << endl;
		}
		
		//+ operator for combining both classes as a new one
		Queue operator+(Queue &obj) {
			Queue res;
			for(int i=0;i<size;i++) {
            	res.add(queue[i]);
        	}
        	for(int i=0;i<obj.size;i++) {
            	res.add(obj.queue[i]);
        	}
			//res.var= this->var+obj.var;
			return res; 
		}
}; 

int main() { 
	Queue q1; 
	q1.add(42); q1.add(2); q1.add(8);  q1.add(1);
	//q1.print();
	Queue q2;
	q2.add(3); q2.add(66); q2.add(128);  q2.add(5);
	Queue q3 = q1+q2;
	q3.print();

	return 0; 
} 

