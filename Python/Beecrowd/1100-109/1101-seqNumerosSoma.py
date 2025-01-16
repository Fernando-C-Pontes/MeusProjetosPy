def main():
    valores = []
    while True:
        entrada = input().strip()
        N, M = map(int, entrada.split())
        if N <= 0 or M <= 0:            
            break
        valores.append((N, M))
    
    for N, M in valores:
        nMenor = min(N, M)
        nMaior = max(N, M)

        soma = sum(range(nMenor, nMaior + 1))
        seq = list(range(nMenor, nMaior + 1))
        
        print(f"{' '.join(map(str, seq))} Sum={soma}")

if __name__ == "__main__":
    main()