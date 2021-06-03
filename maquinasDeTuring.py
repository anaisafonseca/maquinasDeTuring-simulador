# 11811ECP012 - Anaísa Forti da Fonseca

n = input()                          # número de estados
sigma = input()                      # conjunto de símbolos terminais
gama = input()                       # conjunto de símbolos de fita
estados = input()                    # conjunto de estados de aceitação
nTransicoes = input()                # número de transições do autômato

t = []                               # lista de transições
while len(t) < int(nTransicoes):     # recebendo todas as transições
    transicao = input()
    transicao = transicao.split(' ')
    t.append(transicao)

c = input()                          # número de cadeias que serão avaliadas
cadeias = []                         # lista de cadeias a serem avaliadas
while len(cadeias) < int(c):         # recebendo todas as cadeias
    cad = input()
    cad = list(cad)
    cadeias.append(cad)

sigma = sigma.split(' ')             # separando os símbolos terminais
nSimbolos = sigma[0]                 # quantidade de símbolos terminais
simbolos = sigma[1:]                 # lista de símbolos terminais

gama = gama.split(' ')               # separando os símbolos da pilha
nSimbolosPilha = gama[0]             # quantidade de símbolos da pilha
simbolosPilha = gama[1:]             # lista de símbolos da pilha

estados = estados.split(' ')         # separando os estados de aceitação
aceitacao = list(map(int,estados))   # transformando estados de aceitação em inteiros


# função recursiva para percorrer cada cadeia de entrada
def percorreCadeia(fita,posicaoFita,estadoAtual):
    # verifica se o estado atual é um de aceitação e para a máquina
    if (estadoAtual in aceitacao):
        return True

    simboloAtual = fita[posicaoFita]
    # laço com recursividade para percorrer as transições
    for i in range(len(t)):
        transicaoAtual = t[i]
        estadoInicialT = int(transicaoAtual[0])
        simboloT = transicaoAtual[1]

        # verifica se a transição é válida
        if((estadoInicialT == estadoAtual) and (simboloT == simboloAtual)):
            # muda o estado atual
            estadoNovo = int(transicaoAtual[2])
            # escreve na fita 
            fita[posicaoFita] = transicaoAtual[3]

            # move o cursor (muda a posição da fita)
            if(transicaoAtual[4] == 'D'):
                # confere se ele está no último símbolo da fita criada (B)
                # se sim, adiciona outro símbolo em branco
                if(simboloAtual == 'B' and len(fita) == (posicaoFita + 1)):
                    fita.append('B')
                posicaoNova = posicaoFita + 1
                if(percorreCadeia(fita,posicaoNova,estadoNovo)):
                    return True
            # confere se ele pode ir para a esquerda (se não está na posição 0)
            if(transicaoAtual[4] == 'E' and posicaoFita != 0):
                    posicaoNova = posicaoFita - 1
                    if(percorreCadeia(fita,posicaoNova,estadoNovo)):
                        return True
    return False


# aceitação ou rejeição de cada cadeia de entrada
for j in range(int(c)):
    cadeiaAtual = cadeias[j]
    # "insere" a cadeia na fita seguida de um símbolo em branco
    fita = cadeiaAtual + ['B']
    # percorre cada cadeia (o estado 0 é sempre o estado inicial)
    if(percorreCadeia(fita,0,0)):
        print('aceita')
    else:
        print('rejeita')