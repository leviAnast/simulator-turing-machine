class Edge:
    def __init__(self, read: str, write: str = None, direction: str = None):
        self.read = read
        self.write = write
        self.direction = direction

    def getC(self): return self.read
    def getWrite(self): return self.write
    def getDirection(self): return self.direction

    @staticmethod
    def instance(read: str, write: str = None, direction: str = None):
        return Edge(read, write, direction)

    def equals(self, o):
        if isinstance(o, Edge):
            return Edge.testAB(self.read, o.getC())
        return False

    def __repr__(self):
        return f'[{self.read}->{self.write},{self.direction}]'

    @staticmethod
    def testAB(a: str, b: str):
        return a == b
