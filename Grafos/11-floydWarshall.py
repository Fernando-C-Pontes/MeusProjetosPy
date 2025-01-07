# Descrição: Faça um programa que faz a leitura de um grafo ponderado. 
# O programa deve imprimir na tela a matriz de distâncias e a matriz "PI" dos caminhos mínimos obtidos pelo algoritmo de Floyd-Warshall
import numpy as np

def floydWarsh(n, arresta):
    nInicializado = float('inf')
    dist = [[nInicializado] * n for _ in range(n)]
    pred = [[-1] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for i, f, p in arresta:
        dist[i][f] = p
        pred[i][f] = i
    
    # Algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred

def main():
    n, m = map(int, input().split())

    arresta = []
    for _ in range(m):
        i, f, p = map(int, input().split())
        arresta.append((i, f, p))
    
    dist, pred = floydWarsh(n, arresta)
    
    print(np.array(dist, dtype=int))
    print(np.array(pred, dtype=int))

if __name__ == "__main__":
    main()