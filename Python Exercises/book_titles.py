#A special book categorization program, which assigns each book a special code based on its title.
#The code is equal to the first letter of the book, followed by the number of characters in the title.
dir="/Sample-Codes/books.txt"
file = open(dir, "r")
list=file.readlines()

for x in list:
    if x!=list[len(list)-1]:
        out=x[0]+str(len(x)-1)
    else:
        out=x[0]+str(len(x))
    print(out)
    
file.close()
