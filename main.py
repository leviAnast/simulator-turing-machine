from State import State
from Machine import Machine
import tkinter as tk
from MTvisual import MTVisual

def criar_maquina():
    q0 = State('q0')
    q1 = State('q1')
    q2 = State('q2')
    q0.setFinal()

    q0.addTransition(q0, '0', '0', 'D')
    q0.addTransition(q1, '1', '1', 'D')
    q1.addTransition(q0, '1', '1', 'D')
    q1.addTransition(q2, '0', '0', 'D')
    q2.addTransition(q2, '1', '1', 'D')
    q2.addTransition(q1, '0', '0', 'D')

    return Machine(q0, '0000110', 20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simulador de Máquina de Turing")
    mt = criar_maquina()
    interface = MTVisual(root, mt)
    root.mainloop()
