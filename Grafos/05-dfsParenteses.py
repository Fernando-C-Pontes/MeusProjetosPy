def dfsP(u, adj_list, visitado, resultado):
    visitado[u] = True
    resultado.append(f"({u}")

    # Explora todos os vizinhos de u
    for v in adj_list[u]:
        # Visita vértices ainda não visitados
        if not visitado[v]:  
            dfsP(v, adj_list, visitado, resultado)
    
    resultado.append(f"{u})")


def main():
    # Le valores de n (vértices), de m (arestas) e constroi a lista de adjacência.
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)
    
    # Inicialização
    visitado = [False] * n
    resultado = []

    #dfs
    for i in range(n):
        if not visitado[i]:
            dfsP(i, adj_list, visitado, resultado)
    
    print(" ".join(resultado))

if __name__ == "__main__":
    main()