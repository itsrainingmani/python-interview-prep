class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        # Always initialize data items from parent class
        LogicGate.__init__(self, n)

        # Move on to child class unique items
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()
     
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: No Empty Pins")

class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: No Empty Pins")

class AndGate(BinaryGate):

    def __init__(self, n):
        super(AndGate, self).__init__(n)
    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class NandGate(BinaryGate):

    def __init__(self, n):
        super(NandGate, self).__init__(n)
    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 0
        else:
            return 1

class OrGate(BinaryGate):
    
    def __init__(self, n):
        super(OrGate, self).__init__(n)
    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NorGate(BinaryGate):
    
    def __init__(self, n):
        super(NorGate, self).__init__(n)
    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 1
        else:
            return 0

class XorGate(BinaryGate):
    
    def __init__(self, n):
        super(XorGate, self).__init__(n)
    
    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        if a == b:
            return 0
        else:
            return 1

class NotGate(UnaryGate):

    def __init__(self, n):
        super(NotGate, self).__init__(n) 

    def performGateLogic(self):

        p = self.getPin()

        if p == 1:
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def halfadder():
    g1 = AndGate("g1")
    g2 = XorGate("g2")

    ta = NotGate("ta")
    tb = NotGate("tb")
    a = NotGate("a")
    b = NotGate("b")

    c1 = Connector(a, ta)
    c2 = Connector(b, tb)
    c3 = Connector(ta, g1)
    c4 = Connector(tb, g1)
    c5 = Connector(ta, g2)
    c6 = Connector(tb, g2)

    s =  g2.getOutput()
    c = g1.getOutput()

    print("Sum: %i, Carry: %i" % (s, c))

def main():
    g1 = AndGate("g1")
    g2 = AndGate("g2")
    g3 = OrGate("g3")
    g4 = NotGate("g4")

    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())

if __name__ == "__main__":
    halfadder()