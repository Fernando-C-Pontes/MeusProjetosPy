def main():

    numPares = 0
    for _ in range(5):
        valor = float(input().strip())
        if valor % 2 == 0:
            numPares += 1

    print(f"{numPares} valores pares")


if __name__ == "__main__":
    main()