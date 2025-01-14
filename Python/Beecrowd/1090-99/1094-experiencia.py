def main():
    N = int(input())
    totalCobaias = 0
    soma = {"C" : 0, "R" : 0, "S" : 0}
    tipoCoabia = {"C": "coelhos", "R": "ratos", "S": "sapos"}

    for _ in range(N):
        quantidade, cobaia = input().split()
        quantidade = int(quantidade)
        totalCobaias += quantidade

        if cobaia in soma:
            soma[cobaia] += quantidade
    
    print(f"Total: {totalCobaias} cobaias")

    for chave,tipoCoabia_chave in tipoCoabia.items():
        print(f"Total de {tipoCoabia_chave}: {soma[chave]}")
    
    for chave,tipoCoabia_chave in tipoCoabia.items():
        print(f"Percentual de {tipoCoabia_chave}: {(soma[chave]*100)/totalCobaias:.2f} %")


if __name__ == "__main__":
    main()