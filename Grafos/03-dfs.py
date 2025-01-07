def dfs(u, adj_list, visitado, tempo, descoberta, finaliza):
    #Função recursiva para a DFS
    visitado[u] = True
    tempo[0] += 1
    # Instante de descoberta
    descoberta[u] = tempo[0]

    # Explora todos os vizinhos de u
    for v in adj_list[u]:
        # Visita vértices ainda não visitados
        if not visitado[v]:  
            dfs(v, adj_list, visitado, tempo, descoberta, finaliza)

    tempo[0] += 1
    finaliza[u] = tempo[0]  # Define o instante de finalização


def main():
    #Entrada
    n, m = map(int, input().split())
    # lista de adjacência
    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)

    # Estruturas auxiliares
    visitado = [False] * n
    descoberta = [-1] * n
    finaliza = [-1] * n
    tempo = [0]

    # DFS
    for i in range(n):
        if not visitado[i]:
            dfs(i, adj_list, visitado, tempo, descoberta, finaliza)
    
    # saida
    print(descoberta)
    print(finaliza)

if __name__ == "__main__":
    main()