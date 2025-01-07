# Descrição: Faça um programa que leia um grafo ponderado e calcule uma árvore geradora mínima pelo algoritmo de Prim.
def prim(n, r, adjList):
    # Inicializa vetores
    chave = [float('inf')] * n  # Menores pesos conhecidos
    pai = [-1] * n              # Pais na árvore geradora mínima
    visitado = [False] * n      # Rastreia os vértices incluídos na árvore

    chave[r] = 0

    # Busca pelo vértice de menor chave ainda não visitado
    for _ in range(n):
        u = -1
        menor_chave = float('inf')
        for v in range(n):
            if not visitado[v] and chave[v] < menor_chave:
                menor_chave = chave[v]
                u = v
        visitado[u] = True

        # Atualiza os vizinhos de u
        for v, peso in adjList[u]:
            if not visitado[v] and peso < chave[v]:
                chave[v] = peso
                pai[v] = u
    return chave, pai
 
def main():
    n, m, r = map(int,input().split())
    arcos = []
    for _ in range(m):
        i,f, p = map(int, input().split())
        arcos.append((i, f, p))
    adjList = [[] for _ in range(n)]
    for i, f, p in arcos:
        adjList[i].append((f, p))
    
    chave, pai = prim(n, r, adjList)
    
    # Saída: Imprime dois vetores. 
    print(chave) # Na primeira linha, o vetor das "chaves". 
    print(pai) # Na segunda linha, o vetor de "pai" (para representar a árvore).

if __name__ =="__main__":
    main()