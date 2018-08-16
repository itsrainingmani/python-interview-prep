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

        if type(top) != int or type(bottom) != int:
            raise TypeError("Fraction Arguments should be Integers")

        # Maintain lowest terms from initialization
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    # Class method to provide string representation
    def show(self):
        if self.num < 0 or self.den < 0:
            print("-%i/%i" % (abs(self.num), abs(self.den)))
        elif self.num < 0 and self.den < 0:
            print("%i/%i" % (self.num, self.den))
        else:
            print("%i/%i" % (self.num, self.den))

    # Function to convert the object to a string representation
    # Will allow the object to be printed out
    def __str__(self):
        if self.num < 0 or self.den < 0:
            return "-" + str(abs(self.num)) + "/" + str(abs(self.den))
        elif self.num < 0 and self.den < 0:
            return str(self.num) + "/" + str(self.den)
        else:
            return str(self.num) + "/" + str(self.den)

    # Official String representation of the object
    # The idea of repr is to give a string which contains a series
    # of symbols which we can type in the interpreter and get
    # the same value which was sent as an arg to repr
    def __repr__(self):
        return "Fraction(" + str(self.num) + ", " + str(self.den) + ")"

    # This method provides deep quality where the values of the fractions
    # are compared instead of seeing if they are references
    # to the same object (shallow equality)
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    # This function allows the + operator to understand Fraction operands
    # It overrides the addition method
    def __add__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        newnum = self.num*other.den + self.den*other.num
        newden = self.den*other.den
        # common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    # Function to overload the - operator
    def __sub__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        newnum = self.num*other.den - self.den*other.num
        newden = self.den*other.den
        # common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    # Function to overload the * operator
    def __mul__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        newnum = self.num * other.num
        newden = self.den * other.den
        # common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    # Function to overload the / operator
    def __truediv__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        newnum = self.num * other.den
        newden = self.den * other.num
        # common = gcd(newnum, newden)
        return Fraction(newnum, newden)

    # Function to overload the < operator
    def __lt__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        return (self.num / self.den) < (other.num / other.den)

    # Function to overload the > operator
    def __gt__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        return (self.num / self.den) > (other.num / other.den)

    # Function to overload the >= operator
    def __ge__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        return (self.num / self.den) >= (other.num / other.den)

    # Function to overload the <= operator
    def __le__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        return (self.num / self.den) <= (other.num / other.den)

    # Function to overload the != operator
    def __ne__(self, other):
        if type(other) != Fraction:
            other = Fraction(other, 1)
        return (self.num / self.den) != (other.num / other.den)

    # Reflected Operand arithmetic ops
    # x + 3 calls x._add__(3)
    # but how can we do 3 + x
    # we use r(ops) which is essentially saying
    # x + y is y.__radd__(x)
    def __radd__(self, other):
        return self.__add__(Fraction(other, 1))

    # In Place arithmetic ops
    # x += 3
    def __iadd__(self, other):
        # print(self, other)
        return self.__add__(other)

def main():
    F1 = Fraction(1, 4)
    F2 = Fraction(1, 2)
    F3 = Fraction(1, 2)
    F4 = Fraction(-6, -10)

    print("Add", F1 + 3)
    print("Eq", F3 == F2)
    print("Sub", F2 - F1)
    print("Mult", F4 * F4)
    print("Div", F2 / F4)
    print("LE", F1 <= F2)
    print("GT", F4 > F4)

    F5 = Fraction(3, 1)
    # print(2 + F5)
    print(F5)
    F5 += 2
    print(F5)
    print(repr(F5))
    print(eval(repr(F5)) == F5)

if __name__ == "__main__":
    main()
