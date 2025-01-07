# Descrição: Faça um programa que faz a leitura de um grafo ponderado e um vértice inicial. 
# O programa deve imprimir na tela os caminhos mínimos obtidos pelo algoritmo de Dijkstra.

def dijkstra(n, adj, s):
    # Inicializa distâncias com infinito e predecessores com -1
    dist = [float('inf')] * n
    prev = [-1] * n
    # Lista para marcar vértices já processados
    visited = [False] * n
    # A distância do vértice inicial para ele mesmo é 0
    dist[s] = 0

    for _ in range(n):
        # Encontra o vértice não visitado com a menor distância
        u = -1
        min_dist = float('inf')
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                u = i
                min_dist = dist[i]

        # Se não há mais vértices alcançáveis, encerra
        if u == -1:
            break

        # Marca o vértice como visitado
        visited[u] = True

        # Relaxa as arestas do vértice u
        for v, peso in adj[u]:
            if not visited[v] and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                prev[v] = u

    return dist, prev

def main():
    # Recebe n, m e s; n é o total de vértices, m o total de arcos e s é o vértice inicial.
    n, m, s = map(int, input().split())

    # m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
    adjList = [[] for _ in range(n)]
    for _ in range(m):
        i, f, p = map(int, input().split())
        adjList[i].append((f, p))

    dist, prev = dijkstra(n, adjList, s)

    print(dist)
    print(prev)

if __name__ == "__main__":
    main()
