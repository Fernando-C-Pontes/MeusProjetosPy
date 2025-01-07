def main():
    cod, quant = map(int, input().split())

    preco = [4, 4.5, 5, 2, 1.5]

    total = quant * preco[cod-1]

    print(f"Total: R$ {total:.2f}")

if __name__ =="__main__":
    main()