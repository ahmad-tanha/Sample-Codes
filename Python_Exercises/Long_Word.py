#Outputs the longest word of the given text
txt = input()
list_=txt.split()
l=[]
for x in list_:
    l.append(len(x))
#print(l)    
m=max(l)
id=l.index(m)    
w=list_[id]
print(w)
