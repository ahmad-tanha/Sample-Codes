#Function for concatenating arbitrary number of input arguments separated by dash from each other
def concatenate(*argv):
    output=""
    l=0
    for arg in argv:
        l+=1  
        if l<len(argv):
            output+=arg+"-" 
        elif l==len(argv):
            output+=arg
    return output    

print(concatenate("I", "love", "Python", "!"))
