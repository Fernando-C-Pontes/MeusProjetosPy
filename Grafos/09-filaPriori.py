# Descrição: Faça um programa que implemente uma fila de prioridade e imprima na tela
# os resultados das operações especificadas na entrada.

def main():
    # o programa recebe dois inteiros n e k: n é o tamanho da fila, k é a quantidade de operações
    n, k = map(int, input().split())

    # segunda linha, temos n chaves
    Q = [0] * n
    chaves = list(map(int, input().split()))

    # terceira linha, temos k operações, uma operação por linha
    for _ in range(k):
        op = input().split()
        comando = op[0]
    
        # - vazio (Q): devolve True se fila vazia, False caso contrário. 
        if comando == "V":
            resultado = all(val == 0 for val in Q)
            print(resultado, Q)
    
        # - insere (Q, i): insere o índice i na fila Q, ou seja, faz Q[i] = 1.
        elif comando == "I":
            i = int(op[1])
            Q[i] = 1
            print(Q)

        # - busca (Q, i): devolve 1 se o índice i estiver na fila, 0 caso contrário (ou seja, devolve Q[i]).
        elif comando == "B":
            i = int(op[1])
            resultado = Q[i]
            print(resultado, Q)

        # - extraiMinimo (Q): remove e devolve o índice de Q com a menor chave. 
        elif comando == "E":
            indices = [idx for idx, val in enumerate(Q) if val == 1]
            if indices:
                minimo = min(indices, key=lambda x: chaves[x])
                Q[minimo] = 0
                print(minimo, chaves[minimo], Q)
            else:
                print("Fila Vazia", Q)
    
        # - minimo (Q): devolve o índice de Q com a menor chave (sem remover).
        elif comando == "M":
            indices = [idx for idx, val in enumerate(Q) if val == 1]
            if indices:
                minimo = min(indices, key=lambda x: chaves[x])
                print(minimo, chaves[minimo], Q)
            else:
                print("Fila vazia", Q)

if __name__ == "__main__":
    main()