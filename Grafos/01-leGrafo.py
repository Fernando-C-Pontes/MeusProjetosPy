def main():
    # Lê a primeira linha da entrada (n = total de vértices, m = total de arcos)
    n, m = map(int, input().split())

    # Inicializa uma lista de adjacência com listas vazias
    adj_list = [[] for _ in range(n)]

    # Lê os pares de inteiros e constrói a lista de adjacência
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)

    # Imprime as listas de adjacência
    for i in range(n):
        print(f"{i}: {' '.join(map(str, adj_list[i]))}")

# Chama a função principal
if __name__ == "__main__":
    main()