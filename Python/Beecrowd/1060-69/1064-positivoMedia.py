def main():

    numP = 0
    media = 0
    for _ in range(6):
        valor = float(input().strip())
        if valor > 0:
            media += valor
            numP += 1

    print(f"{numP} valores positivos")
    print(f"{media/numP:.1f}")


if __name__ == "__main__":
    main()