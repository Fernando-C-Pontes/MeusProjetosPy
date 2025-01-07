# Descrição: Faça um programa que faz a leitura de um grafo ponderado e imprime na tela 
# as suas listas de adjacências com os pesos de cada arco.

def main():
    n, m = map(int, input().split())

    arcos = []
    for _ in range(m):
        i, f, p = map(int, input().split())
        arcos.append((i, f, p))

    adjList = [[] for _ in range(n)]
    for i, f, p in arcos:
        adjList[i].append((f, p))
        
    for i in range(len(adjList)):
        adjacentes = " ".join(f"{f}({p})" for f, p in adjList[i])
        print(f"{i}: {adjacentes}")

if __name__ == "__main__":
    main()