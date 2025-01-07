# Descrição: Faça um programa que implemente as operações com Conjuntos Disjuntos e imprima os resultados correspondentes.

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

def main():
    # Inicialmente, S é vazio.
    S = []
    # A primeira linha contém n, o total de operações com S.
    n = int(input())
    # As linhas a seguir, temos n linhas, cada uma com uma operação: 
    for _ in range(n):
        entrada = input().split(" ")
        op = entrada[0]
        arg = entrada[1]
        if op == "F":
            print (findSet (S, arg), S)
        elif op == "M":
            makeSet(S, arg)
            print(S)
        elif op == "U":
            argComp = entrada[2]
            union(S, arg, argComp)
            print(S)

if __name__ == "__main__":
    main()