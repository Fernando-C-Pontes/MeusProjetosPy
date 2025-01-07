# Descrição: Faça um programa que leia um grafo ponderado e calcule uma árvore geradora mínima pelo algoritmo de Kruskal.
# - findSet (S, x): devolve um representante de S_x.
def findSet (S, x):
    for i in range (len(S)):
        for j in S[i]:
            if j == x:
                return i
    return -1

# - makeSet (S, x): cria um novo conjunto com um único elemento x.
def makeSet (S, x):
    S.append([x])

# - union (S, x, y): une dois conjuntos S_x e S_y.
def union (S, x, y):
    i = findSet (S, x)
    j = findSet (S, y)
    if i != j:
        S[i] += S[j]
        S[j].clear()


def kruskal(n, arestas):
    S = []
    for j in range(n):
        makeSet(S, j)

    # Ordena arestas por peso crescente
    arestas.sort(key=lambda x: x[2])

    # Algoritmo de Kruskal
    arvMin = []
    for i, f, p in arestas:
        if findSet(S, i) != findSet(S, f):
            union(S, i, f)
            arvMin.append([i, f, p])
    return arvMin

def main():
    #Recebe n, m; n é o total de vértices, m o total de arcos.
    n, m, _ = map(int,input().split())
    # m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
    arestas = []
    for _ in range(m):
        i, f, p = map(int, input().split())
        arestas.append((i, f, p))
    
    print(kruskal(n, arestas))

if __name__ == "__main__":
    main()