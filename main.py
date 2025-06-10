from State import State
from Machine import Machine
def ler_arquivo(caminho):
    fita = ''
    estados = {}
    transicoes = []
    estado_inicial = None
    estados_finais = set()

    with open(caminho, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith('@') or linha.startswith('#'):
                continue
            if linha.startswith('fita'):
                fita = linha.split()[1]
            elif linha.startswith('init'):
                estado_inicial = linha.split()[1]
            elif linha.startswith('accept'):
                estados_finais.add(linha.split()[1])
            else:
                transicoes.append(linha)

    #cria os objetos de estado
    for transicao in transicoes:
        origem, simbolo, destino, novo_simbolo, direcao = map(str.strip, transicao.split(','))
        if origem not in estados:
            estados[origem] = State(origem)
        if destino not in estados:
            estados[destino] = State(destino)
        estados[origem].addTransition(estados[destino], simbolo, novo_simbolo, direcao)

    #marca os estados finais
    for f in estados_finais:
        if f in estados:
            estados[f].setFinal()

    return estados[estado_inicial], fita

if __name__ == "__main__":
    caminho = "Entrada_Multiplo3.txt" #"Entrada_Par.txt" , "Entrada_Contem0.txt" , "Entrada_Multiplo3.txt"
    estado_inicial, fita = ler_arquivo(caminho)
    mt = Machine(estado_inicial, fita, 30)  
    mt.run()
