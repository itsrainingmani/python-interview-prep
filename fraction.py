#Python is object oriented. We can use classes to implement an abstract
#data type

def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        
        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    #This is the constructor method for the class
    #The self parameter is used as a reference back to the object itself
    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def show(self):
        print("%i/%i" %(self.num, self.den))
    
    #Function to convert the object to a string representation
    #Will allow the object to be printed out
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    #This function allows the + operator to understand Fraction operands
    #It overrides the addition method
    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    #This method provides deep quality where the values of the fractions
    #are compared instead of seeing if they are references to the same object (shallow equality)
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    


myf = Fraction(3,5)
print(myf)

print("I ate", myf, "of the pizza")

f1 = Fraction(1,4)
f2 = Fraction(1,2)

print(f1+f2)