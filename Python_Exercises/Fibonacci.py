#Fibonacci Sequence Generator Function
n=int(input())

def fibo(n):
  if n<=1:
    return n
  else:
    return fibo(n-1)+fibo(n-2)
  
if n > 0:
    for x in range(n):
        print(fibo(x))
else: 
    print("Incorrect input, try again!")
 
