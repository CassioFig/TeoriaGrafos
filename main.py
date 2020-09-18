from math import inf

# Grafo
vertice = ['t', 'u', 'x', 'v', 'y']
adj = {'t': ['x', 'u'], 'x': ['u', 'v', 'y'], 'u': ['x', 'v'], 'v': ['y'], 'y': ['v', 't']}
peso = {'tu': 10, 'tx': 5, 'xu': 3, 'ux': 2, 'uv': 1, 'xv': 9, 'xy': 2, 'vy': 4, 'yv': 6, 'yt': 7}

# Tabela
s = []
dist = {}
path = {}


def inicializaListas(v, d):
    # Adiciona o vértice de origem.
    s.append(d)

    # Inicia as listas de dist e path
    dist[d] = 0
    for i in range(len(v)):
        if v[i] not in dist:
            dist[v[i]] = inf

    for i in range(len(v)):
        path[v[i]] = None


def algoritmo_Dijkstra():
    i = 0
    j = s[len(s) - 1]
    t = len(adj[j])

    while i < t:
        if adj[j][i] not in s:
            z = adj[j][i]
            if dist[z] > dist[j] + peso[j + z]:
                dist[z] = dist[j] + peso[j + z]
                path[z] = j
        i += 1

    compara()


def compara():
    aux = 0
    v = ''

    c = 0
    for i in range(len(dist)):
        if vertice[i] not in s:
            if c == 0:
                aux = dist[vertice[i]]
                v = vertice[i]
                c += 1
            elif dist[vertice[i]] < aux:
                aux = dist[vertice[i]]
                v = vertice[i]

    s.append(v)


def menorCaminho(d, p):
    caminho = []

    v = p
    caminho.append(v)
    while v != d:
        v = path[v]
        caminho.append(v)

    caminho.reverse()
    return caminho


def rodaAlgoritmo(v):
    while len(s) != len(v):
        algoritmo_Dijkstra()


def main(v):

    print('---' * 17)
    print('[1] Caminho mais curto para todos os vértices\n[2] Caminho mais curto entre dois vértices.')
    print('---' * 17)
    opc = int(input('>> Digite qual função deseja: '))
    print('---' * 12)

    if opc == 1:
        print(f'Vértices: {v}')
        print('---' * 12)
        de = input('Escolha o vértice de partida: ').lower()
        print('---' * 12)

        inicializaListas(v, de)
        rodaAlgoritmo(v)

        for i in range(len(v)):
            print(f'Menor caminho de {de} para {v[i]}: {menorCaminho(de, v[i])}')

    elif opc == 2:
        print(f'Vértices: {v}')
        print('---' * 12)
        de = input('Escolha o vértice de partida: ').lower()
        para = input('Escolha o vértice de chegada: ').lower()
        print('---' * 12)

        inicializaListas(v, de)
        rodaAlgoritmo(v)

        print(f'Menor caminho de {de} para {para}: {menorCaminho(de, para)}')

    else:
        print('Opção inválida!')


main(vertice)
