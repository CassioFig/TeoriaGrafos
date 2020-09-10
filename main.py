
# grafo = {1: [2, 3], 2: [5, 4], 3: [1, 4], 4: [3, 5, 6], 5: [2, 4], 6: [4, 7, 8], 7: [6, 8], 8: [7, 6]}

grafo = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [3, 2]}


# Printa o grafo por lista de adjacência.
def printaGrafo(g):
    for i in range(len(g)):
        print(f'{i + 1}: {g[i + 1]}')


# Método que verifica se todos os vértices possuem o mesmo grau.
def ehRegular(g):
    regular = False
    aux = len(g[1])

    for i in g:
        if len(g[i]) != aux:
            regular = False
            break
        else:
            regular = True

    return regular


# Método para escolher o vértice.
def escolha():
    parametro = int(input(f"\nEscolha um vértice (de 1 a {len(grafo)}): "))
    while parametro < 1 or parametro > 12:
        print("\nOpa, errado. Tente novamente!!\n")
        parametro = int(input(f"Escolha um vértice (de 1 a {len(grafo)}): "))
    return parametro


# Método para retornar os vértices adjacentes do vértice escolhido.
def getAdjacentes(g, num):
    for j in range(len(g)):
        if num == j + 1:
            print(g[j + 1])


# Método que adiciona os vértices do grafo em uma lista.
def listaVertices(g):
    v = []
    for x in g:
        v.append(x)
    return v


# Função que verifica se todos os vértices são adjacentes entre si.
def ehCompleto(g):
    v = listaVertices(g)
    completo = False

    i = 1
    j = 0
    v.remove(i)
    while i <= len(g):
        if j < len(g[i]):
            if v[j] not in g[i] or len(g[i]) < len(g[1]):
                completo = False
                break
            else:
                completo = True
            j += 1

        elif i == len(g):
            break
        else:
            v.append(i)
            j = 0
            i += 1
            v.remove(i)

    return completo


# Verifica se existe um caminho entre cada par de vértice.
def ehConexo(g):
    v = listaVertices(g)
    conexo = False
    pilha = []
    visitado = []
    explorado = []

    visitado.append(v[0])
    pilha.append(v[0])

    i = 0
    while len(pilha) > 0:
        w = g[pilha[len(pilha) - 1]]
        while w[i] not in visitado and w[i] in g[pilha[len(pilha) - 1]]:
            visitado.append(w[i])
            pilha.append(w[i])
            w = g[pilha[len(pilha) - 1]]
            i = 0

        if len(w) - 1 > i:
            i += 1
            continue

        explorado.append(pilha[len(pilha) - 1])
        pilha.pop()
        i = 0

    if len(pilha) == 0:
        if len(explorado) == len(v):
            conexo = True
        else:
            conexo = False

    return conexo


printaGrafo(grafo)
getAdjacentes(grafo, escolha())
print('--' * 10)
print("É regular: ", ehRegular(grafo))
print("\nÉ completo: ", ehCompleto(grafo))
print("\nÉ conexo: ", ehConexo(grafo))
print('--' * 10)
