#Simple Calculator
x=input()
y=input()

summ=float(x)+float(y)
diff=float(x)-float(y)
prod=float(x)*float(y)

if float(y)==0:
    div='undefined'
else:
    div=float(x)/float(y)

print('sum is', summ)
print('dif is', diff)
print('prod is', prod)
print('div is', div)
