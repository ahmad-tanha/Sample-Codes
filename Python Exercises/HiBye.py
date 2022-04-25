n = int(input())

#It takes an input n and outputs the numbers from 1 to n.
#For each multiple of 3, print "Hy" instead of the number.
#For each multiple of 5, prints "Bye" instead of the number.
#For numbers which are multiples of both 3 and 5, output "HiBye".

for x in range(1, n):
    if x % 2 == 0:
        continue
    elif x % 3 == 0 and x % 5 == 0:
        print("HiBye")
    elif x % 3 == 0:
        print("Hi")
    elif x % 5 == 0:
        print("Bye") 
    else:
        print(x)
