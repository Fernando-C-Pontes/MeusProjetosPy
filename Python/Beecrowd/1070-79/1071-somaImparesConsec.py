def somaImpares(inicio, fim):
    soma = 0
    for i in range(inicio+1, fim, 1):
        if i % 2 != 0:
            soma += i
    
    return soma

def main():
    X, Y = int(input()), int(input())

    if X > Y:
        print(somaImpares(Y, X))
    else:
        print(somaImpares(X, Y))

if __name__ == "__main__":
    main()