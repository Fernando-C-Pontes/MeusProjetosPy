def main():
    maior = 0
    posicao = 0
    for i in range(100):
        valor = int(input())
        if valor > maior:
            maior = valor
            posicao = i+1
    
    print(maior)
    print(posicao)

if __name__ == "__main__":
    main()