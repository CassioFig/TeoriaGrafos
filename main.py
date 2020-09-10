
# grafo = {1: [2, 3], 2: [5, 4], 3: [1, 4], 4: [3, 5, 6], 5: [2, 4], 6: [4, 7, 8], 7: [6, 8], 8: [7, 6]}

grafo = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [3, 2]}


# Printa o grafo por lista de adjacência.
def printaGrafo(g):
    for i in range(len(g)):
        print(f'{i + 1}: {g[i + 1]}')


printaGrafo(grafo)
