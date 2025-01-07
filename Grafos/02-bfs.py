def main():
    # Leitura de n, m, s
    # n = total de vértices; m = total de arcos; s = vértice inicial
    n, m, s = (int(temp) for temp in input().split(" "))

    # Construção da lista de adjacência
    # Inicializa uma lista de adjacência com listas vazias
    adj_list = [[] for _ in range(n)]
    # Lê os pares de inteiros e constrói a lista de adjacência
    for _ in range(m):
        u, v = (int(temp) for temp in input().split(" "))
        adj_list[u].append(v)

    # Inicialização de distâncias e fila
    distancia = [-1]*n
    visitado = [1]*n

    distancia[s] = 0
    visitado[s] = 2

    # Inicialização de fila
    fila = [s]
    
    # Execução do BFS
    while fila:
        j = fila.pop(0)
        for i in adj_list[j]:
            if visitado[i] == 1:
                distancia[i] = distancia[j] + 1
                visitado[i] = 2
                fila.append(i)
        visitado[j] = 3

    # Impressão do vetor de distâncias
    print(f"{s}: " + " ".join(map(str, distancia)))

# Chama a função principal
if __name__ == "__main__":
    main()