#A valid phone number has exactly 8 digits and starts with 2, 7 or 3. Output is "Valid" if the number is valid and is "Invalid", if it is not.
import re
num=input()

num1=r"2"
num2=r"7"
num3=r"3"

if len(num)==8:
    if re.match(num1, num) or re.match(num2, num) or re.match(num3, num):
        print('Valid')
    else:
        print('Invalid')
else:
    print('Invalid')

            
