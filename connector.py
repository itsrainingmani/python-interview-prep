import logic

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():
    g1 = logic.AndGate("g1")
    g2 = logic.AndGate("g2")
    g3 = logic.OrGate("g3")
    g4 = logic.NotGate("g4")

    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())

if __name__ == "__main__":
    main()