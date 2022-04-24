#Enabling and adding of two Juice objects of class Juice, resulting in a new Juice object with the combined capacity and names of the two juices being added.
class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')
    
    def __add__(self,newJuice):
        self.name += "&" + newJuice.name
        self.capacity += newJuice.capacity 
        return self.__str__

a = Juice('Apple', 2.5)
b = Juice('Banana', 1.5)

print(a.__add__(b)())
