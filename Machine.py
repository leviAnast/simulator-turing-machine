from State import State
from Transition import Transition
from Edge import Edge
class Machine: #AFD = (Q, Σ, δ, q0, F)
    def __init__(self, q: State, w: str, _range: int):
        self.q = q
        self.w = w
        self.fita = []

        #Ideia para Turing Machine abaixo, onde _range*2 eh o tamanho da fita da maquina:
        self.set_fita_space(_range)
        self.init_fita(w)
        print(f'Fita: {self.fita}')

    # OBS: a self.fita ja esta pronta com os dados.
    # Por exemplo, voce pode usar o self.current como o indice de self.fita[self.current]. Como ficaria?
    def run(self):
        if(self.q is None or self.w is None):
            return False
        
        while True:
            symbol = self.fita[self.current]
            transition: Transition = self.q.transition(symbol)

            if transition is None:
                break

            edge: Edge = transition.getEdge()
            next_state = transition.getState()

            if edge.getDirection() == 'D':
                self.current += 1
            elif edge.getDirection() == 'E':
                self.current -= 1
            
            self.q = next_state
            self.print_fita()

        return self.print_result()

    def print_result(self):
        """ Print and Return True (ok) or False (no ok)"""
        if(self.q.isFinal):
            print(f'reconheceu: {self.w}')
        else:
            print(f'Não reconheceu: {self.w}')
        return self.q.isFinal

    def print_fita(self):
        fita = ''.join([x if x is not None else '_' for x in self.fita])
        pointer = ' ' * self.current + '^'
        print(f'Fita: {fita}')
        print(f'       {pointer}')
        print(f'Estado: {self.q.getName()}')
        print('-'* 40)
        
    #Ideia para Turing Machine abaixo:
    def init_fita(self, w):
        for a in list(w):
            self.fita[self.current] = a
            self.current += 1

        self.current = self.range+1

        #print(f'{self.fita}\nLEN: {len(self.fita)}\nMAX: {self.max}')
        #print(f'current -> {self.fita[self.current]}')

    def set_fita_space(self, _range):
        self.range = _range
        self.max = self.range*2

        self.fita.append('#')
        for i in range(1, self.max+2):
            self.fita.append(None)

        self.current = self.range+1
        self.max = self.max+1
