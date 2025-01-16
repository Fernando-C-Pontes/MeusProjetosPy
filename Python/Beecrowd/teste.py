def main():
    valores = []
    
    # Leitura de pares até encontrar um par com número menor ou igual a 0
    while True:
        entrada = input().strip()
        if not entrada:  # Se a entrada for vazia, continua
            continue
        
        try:
            N, M = map(int, entrada.split())
            if N <= 0 or M <= 0:  # Condição de parada
                break
            valores.append((N, M))
        except ValueError:
            print("Entrada inválida! Insira dois números inteiros.")

    # Processamento dos pares lidos
    for N, M in valores:
        nMenor = min(N, M)
        nMaior = max(N, M)

        soma = sum(range(nMenor, nMaior + 1))
        seq = list(range(nMenor, nMaior + 1))

        print(f"{' '.join(map(str, seq))} Sum={soma}")

if __name__ == "__main__":
    main()