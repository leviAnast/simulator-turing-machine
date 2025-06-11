from State import State
from Transition import Transition
from Edge import Edge
class Machine: #AFD = (Q, Σ, δ, q0, F)
    def __init__(self, q: State, w: str, _range: int):
        self.q = q
        self.w = w
        self.fita = []
        self.set_fita_space(_range)
        self.init_fita(w)

    def run(self):
        symbol = self.fita[self.current]
        transition: Transition = self.q.transition(symbol)

        if transition is None:
            return False

        edge: Edge = transition.getEdge()
        next_state = transition.getState()

        if edge.getWrite() is not None:
            self.fita[self.current] = edge.getWrite()

        if edge.getDirection() == 'D':
            self.current += 1
        elif edge.getDirection() == 'E':
            self.current -= 1

        self.q = next_state
        return True

    def init_fita(self, w):
        inicio = self.range + 1
        self.current = inicio

        for a in list(w):
            self.fita[self.current] = a
            self.current += 1

        self.current = inicio

    def set_fita_space(self, _range):
        self.range = _range
        self.max = self.range*2

        self.fita.append('#')
        for i in range(1, self.max+2):
            self.fita.append("_")

        self.current = self.range + 1
        self.max = self.max + 1
