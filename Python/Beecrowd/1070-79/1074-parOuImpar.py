def main():
    N =int(input())

    for _ in range(N):
        valor = int(input())
        if valor == 0:
            print("NULL")
        else:
            paridade = "EVEN" if valor % 2 == 0 else "ODD"
            sinal = "POSITIVE" if valor > 0 else "NEGATIVE"
            print(f"{paridade} {sinal}")

if __name__ == "__main__":
    main()