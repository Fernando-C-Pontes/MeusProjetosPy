def somaImpares(inicio, fim):
    soma = 0
    for i in range(inicio+1, fim):
        if i % 2 != 0:
            soma += i
    
    return soma


def main():
    N = int(input())

    for _ in range(N):
        X, Y = map(int, input().split())
        if X > Y:
            X, Y = Y, X    
        print(somaImpares(X, Y))

if __name__ == "__main__":
    main()