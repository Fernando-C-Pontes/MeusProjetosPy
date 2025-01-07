# busca em largura
def bfs(n, inicio, adj_list):
    distancia = [-1] * n
    distancia[inicio] = 0
    fila = [inicio]

    while fila:
        atual = fila.pop(0)
        for i in adj_list[atual]:
            if distancia[i] == -1:
                distancia[i] = distancia[atual] + 1
                fila.append(i)

    return distancia

def main():
    n, m = map(int, input().split())

    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)

    for i in range(n):
        print(f"{i}: " + " ".join(map(str, bfs(n, i, adj_list))))

if __name__ == "__main__":
    main()