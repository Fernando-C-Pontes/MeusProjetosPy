def main():
    while True:
        entrada = input().strip()
        N, M = map(int, entrada.split())
        if N == M:
            break
        resposta = "Decrescente" if N < M else "Crescente"
        print(resposta)

if __name__ == "__main__":
    main()