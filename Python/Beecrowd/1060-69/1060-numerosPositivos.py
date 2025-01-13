def main():

    temp = 0
    for _ in range(6):
        valor = float(input().strip())
        if valor > 0:
            temp += 1

    print(f"{temp} valores positivos")


if __name__ == "__main__":
    main()