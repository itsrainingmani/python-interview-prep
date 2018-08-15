''' Python is object oriented. We can use classes to implement an abstract
data type '''


# Function to calculate the greatest common denominator between 2 numbers
def gcd(m, n):
    while (m % n) != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


# Class to implement Fraction functionalilty
class Fraction:
    # This is the constructor method for the class
    # The self parameter is used as a reference back to the object itself
    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    # Class method to provide string representation
    def show(self):
        print("%i/%i" % (self.num, self.den))

    # Function to convert the object to a string representation
    # Will allow the object to be printed out
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # This function allows the + operator to understand Fraction operands
    # It overrides the addition method
    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den*other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    # This method provides deep quality where the values of the fractions
    # are compared instead of seeing if they are references
    # to the same object (shallow equality)
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    # Function to overload the - operator
    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den*other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    # Function to overload the * operator
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    # Function to overload the / operator
    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    # Function to overload the < operator
    def __lt__(self, other):
        return (self.num / self.den) < (other.num / other.den)

    # Function to overload the > operator
    def __gt__(self, other):
        return (self.num / self.den) > (other.num / other.den)


F4 = Fraction(3, 5)
print(F4)

print("I ate", F4, "of the pizza")

F1 = Fraction(1, 4)
F2 = Fraction(1, 2)
F3 = Fraction(1, 2)

print(F1 + F2)
print(F3 == F2)
print(F2 - F1)
print(F4 * F4)
print(F2 / F1)
print(F3 < F2)
print(F4 > F2)
