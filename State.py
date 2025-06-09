from Transition import Transition
from Edge import Edge

class State:
    def __init__(self, name: str):
        self.name = name
        self.isFinal = False
        self.transitions = []

    def getName(self): return self.name
    def setFinal(self): self.isFinal = True

    def addTransition(self, state, read: str, write: str = None, direction: str = None):
        return self.addTransitions(state, Edge.instance(read, write, direction))

    def addTransitions(self, state, *edges):
        for edge in edges:
            transition = Transition(state, edge)
            if transition in self.transitions:
                continue
            self.transitions.append(transition)
        return self

    def transition(self, _c: str):
        for t in self.transitions:
            e = t.getEdge()
            if e.getC() == _c:
                return t
        return None

    def equals(self, s):
        if isinstance(s, State):
            return s.getName() == self.getName()
        return False

    def hashCode(self):
        return hash(self.getName())
